from .base import *  # NOQA

DEBUG = True

ALLOWED_HOSTS = []

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    },
}

# 配置性能分析工具django-debug-toolbar
INSTALLED_APPS += [
    'debug_toolbar',
    'pympler',
    'debug_toolbar_line_profiler',

    # 性能分析silk
    'silk',

]

MIDDLEWARE += [
    'debug_toolbar.middleware.DebugToolbarMiddleware',

    'silk.middleware.SilkyMiddleware',
]

INTERNAL_IPS = ['127.0.0.1']

DEBUG_TOOLBAR_PANELS = [
    'debug_toolbar.panels.versions.VersionsPanel',
    'debug_toolbar.panels.timer.TimerPanel',
    'debug_toolbar.panels.settings.SettingsPanel',
    'debug_toolbar.panels.headers.HeadersPanel',
    'debug_toolbar.panels.request.RequestPanel',
    'debug_toolbar.panels.sql.SQLPanel',
    'debug_toolbar.panels.staticfiles.StaticFilesPanel',
    'debug_toolbar.panels.templates.TemplatesPanel',
    'debug_toolbar.panels.cache.CachePanel',
    'debug_toolbar.panels.signals.SignalsPanel',
    'debug_toolbar.panels.logging.LoggingPanel',
    'debug_toolbar.panels.redirects.RedirectsPanel',

    # 第三方插件
    # 'djdt_flamegraph.FlamegraphPanel',  # 不可用
    'pympler.panels.MemoryPanel',
    'debug_toolbar_line_profiler.panel.ProfilingPanel'

]
