import json
from os import path

from django.conf import settings


# Methods in this class should remain non-static as later there might be some instance level cache here.
class Encore:
    # noinspection PyMethodMayBeStatic
    def load_json(self):
        entry_points_path = settings.ENCORE_BUILD_DIR / 'entrypoints.json'
        if not path.isfile(entry_points_path):
            raise RuntimeError('Missing entry points - %s' % entry_points_path)

        with open(entry_points_path) as it:
            return json.load(it)

    def get_js(self, entrypoint):
        data = self.load_json()

        if 'entrypoints' not in data:
            raise RuntimeError('Invalid entry points manifest')

        manifest = data['entrypoints']

        if entrypoint not in manifest:
            raise RuntimeError('Unknown entrypoint - %s' % entrypoint)

        if 'js' not in manifest[entrypoint]:
            return []

        return manifest[entrypoint]['js']

    def get_css(self, entrypoint):
        data = self.load_json()

        if 'entrypoints' not in data:
            raise RuntimeError('Invalid entry points manifest')

        manifest = data['entrypoints']

        if entrypoint not in manifest:
            raise RuntimeError('Unknown entry point - %s' % entrypoint)

        if 'css' not in manifest[entrypoint]:
            return []

        return manifest[entrypoint]['css']
