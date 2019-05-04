from .base import *  # NOQA

DEBUG = True

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

THEME = 'bootstrap'
# THEME = 'default'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'themes', THEME, 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

STATIC_ROOT = '/tmp/static'

STATIC_URL = '/static/'

STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'themes', THEME, 'static')
]

# 配置django-debug-toolbar
INSTALLED_APPS += [
    'debug_toolbar',
    'pympler',
    'debug_toolbar_line_profiler',

    'silk',
]

MIDDLEWARE += [
    'debug_toolbar.middleware.DebugToolbarMiddleware',

    'silk.middleware.SilkyMiddleware',
]

INTERNAL_IPS = ['127.0.0.1']
# DEBUG_TOOLBAR_PANELS = [
#     # 'djdt_flamegraph.FlamegraphPanel',#不可用
#     'pympler.panels.MemoryPanel',
#     'debug_toolbar_line_profiler.panel.ProfilingPanel'
# ]

#配置silk
