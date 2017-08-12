import os
from django.conf import settings
from django.utils.translation import ugettext_lazy as _

def get_directory_contents(base_dir=settings.BASE_DIR, directory='data'):
    root_path = os.path.abspath(os.path.join(base_dir, os.pardir))
    directory_contents = None
    try:
        target_path = os.path.join(root_path, directory)
        directory_contents = os.listdir(target_path)
    except FileNotFoundError:
        print (_('directory not found'))
    
    return target_path, directory_contents
