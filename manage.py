#!/usr/bin/env python

import os
import site
import sys


ROOT = os.path.dirname(os.path.abspath(__file__))

path = lambda *a: os.path.join(ROOT, *a)

prev_sys_path = list(sys.path)

site.addsitedir(path('apps'))
site.addsitedir(path('lib'))
site.addsitedir(path('vendor'))

# Move the new items to the front of sys.path. (via virtualenv)
new_sys_path = []
for item in list(sys.path):
    if item not in prev_sys_path:
        new_sys_path.append(item)
        sys.path.remove(item)
sys.path[:0] = new_sys_path

from django.core.management import execute_manager
try:
    import settings_local as settings
except ImportError:
    try:
        import settings
    except ImportError:
        import sys
        sys.stderr.write("Error: Can't find the file 'settings.py' in the directory containing %r. It appears you've customized things.\nYou'll have to run django-admin.py, passing it your settings module.\n(If the file settings.py does indeed exist, it's causing an ImportError somehow.)\n" % __file__)
        raise

if __name__ == "__main__":
    execute_manager(settings)
