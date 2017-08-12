import os
from django.core.management.base import BaseCommand
from consumption.utils import get_directory_contents


class Command(BaseCommand):
    help = 'import data'

    def add_arguments(self, parser):
        parser.add_argument(
            'foldername',
            nargs='*',
            type=str,
            help='Folder name',
        )

    def handle(self, *args, **options):
        print("Implement me!")
        folders = []
        
        if options['foldername']:
            files = get_directory_contents(options['foldername'][0])
        else:
            files = get_directory_contents()

        for file in files:
            is_folder = os.path.isdir(file)
            
            if is_folder:
                folders.append(file)
            else:
                