from .partials import *

INSTALLED_APPS += [
        'debug_toolbar',
]

MIDDLEWARE += [
        'debug_toolbar.middleware.DebugToolbarMiddleware',
]
