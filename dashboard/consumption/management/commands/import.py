import os

from django.core.management.base import BaseCommand
from django.db import transaction
from django.utils.translation import ugettext_lazy as _

from tablib import Dataset

from consumption.models import Consumption, UserData
from consumption.utils import get_directory_contents


class Command(BaseCommand):
    help = 'import data'

    def add_arguments(self, parser):
        parser.add_argument(
            'foldername',
            nargs='*',
            type=str,
            help=_('Folder name'),
        )

    @staticmethod
    def open_csv_file(path, filename):
        """Return contents of csv file"""
        file = path + '/' + filename
        with open(file, 'r') as csv_file:
            contents = csv_file.read()
        return contents

    def create_user_data(self, path, file):
        contents = self.open_csv_file(path, file)
        dataset = Dataset().load(contents)
        with transaction.atomic():
            for user_id, area, tariff in dataset:
                UserData.objects.update_or_create(
                    user_id=user_id,
                    area=area,
                    tariff=tariff
                )

    def create_consumption_data(self, path, file):
        contents = self.open_csv_file(path, file)
        dataset = Dataset().load(contents)
        with transaction.atomic():
            for datetime, consumption in dataset:
                user_id = file.replace('.csv','')
                user = UserData.objects.get(user_id=user_id)
                if user:
                    Consumption.objects.create(
                        user=user,
                        datetime=datetime,
                        consumption=int(float(consumption)),
                    )

    def handle(self, *args, **options):
        folders = []     
        if options['foldername']:
            path, files = get_directory_contents(directory=options['foldername'][0])
        else:
            path, files = get_directory_contents()

        for file in files:
            is_folder = os.path.isdir(file)
            if is_folder:
                folders.append(file)
            elif '.csv' in file:
                self.create_user_data(path, file)

        for folder in folders:
            folder_path, folder_files = get_directory_contents(
                base_dir=path + '/',
                directory=folder,
            )

            for file in folder_files:
                if '.csv' in file:
                    self.create_consumption_data(folder_path, file)

        print(_('Import Finished'))
                