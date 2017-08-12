from django.core.management.base import BaseCommand
from consumption.utils import get_directory_contents



class Command(BaseCommand):
    help = 'import data'       

    def handle(self, *args, **options):
        print("Implement me!")
        contents = get_directory_contents()