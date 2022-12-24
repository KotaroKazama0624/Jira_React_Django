from django.core.management.utils import get_random_secret_key

import sys

secret_key = get_random_secret_key()
text = 'SECRET_KEY = \'{0}\''.format(secret_key)
print(text,file=sys.stderr)