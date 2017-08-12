import os
from django.conf import settings
from django.utils.translation import ugettext_lazy as _

def get_directory_contents(base_dir=settings.BASE_DIR, directory='data'):
    if base_dir != settings.BASE_DIR:
        root_path = os.path.abspath(os.path.join(base_dir))
    else:
        root_path = os.path.abspath(os.path.join(base_dir, os.pardir))
    
    directory_contents = []
    contents = None

    try:
        target_path = os.path.join(root_path, directory)
        contents = os.listdir(target_path)
    except FileNotFoundError:
        print (_('directory not found'))

    if contents is not None:
        for file in contents:
            if not file.startswith('.'):
                directory_contents.append(file)

    return target_path, directory_contents
