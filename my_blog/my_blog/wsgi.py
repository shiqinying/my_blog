"""
WSGI config for my_blog project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.11/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

# 通过读取系统环境变量MY_BLOG_PROFILE来控制django加载不同的settings文件
profile = os.environ.get('MY_BLOG_PROFILE', 'develop')
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "my_blog.settings.%s" % profile)

application = get_wsgi_application()
