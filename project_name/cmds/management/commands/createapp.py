import os
import sys
from django.core.management import call_command
from django.conf import settings
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    help = 'Generates a new app and adds it to INSTALLED_APPS'

    def add_arguments(self, parser):
        parser.add_argument('app_name', type=str, help='The name of the new app')

    def handle(self, *args, **options):
        app_name = options['app_name']
        
        self.stdout.write(f"Generating app: {app_name}")
        call_command('startapp', app_name)

        app_config_code = f"""
from django.apps import AppConfig

class {app_name.capitalize()}Config(AppConfig):
    name = '{app_name}'
    def ready(self):
        if self.name not in settings.INSTALLED_APPS:
            settings.INSTALLED_APPS.append(self.name)
"""
        apps_py_path = os.path.join(app_name, 'apps.py')
        with open(apps_py_path, 'w') as f:
            f.write(app_config_code)
        
        self.stdout.write(f"Added AppConfig to {apps_py_path}")
        self._add_app_to_installed_apps(app_name)
        
        self.stdout.write(self.style.SUCCESS(f"App '{app_name}' created and added to INSTALLED_APPS"))

    def _add_app_to_installed_apps(self, app_name):
        settings_file = os.path.join(os.getcwd(), 'config', 'settings.py')

        with open(settings_file, 'r') as file:
            settings_content = file.read()

        installed_apps_index = settings_content.find('INSTALLED_APPS = [')
        installed_apps_end_index = settings_content.find(']', installed_apps_index)
        installed_apps_block = settings_content[installed_apps_index:installed_apps_end_index + 1]

        if f"'{app_name}'" not in installed_apps_block:
            settings_content = settings_content[:installed_apps_end_index] + f"\n    '{app_name}'," + settings_content[installed_apps_end_index:]
            
            with open(settings_file, 'w') as file:
                file.write(settings_content)

        self.stdout.write(self.style.SUCCESS(f"Added {app_name} to INSTALLED_APPS in settings.py"))
