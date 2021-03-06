#!/usr/bin/env python
import os
import sys

if __name__ == "__main__":

    #通过读取系统环境变量MY_BLOG_PROFILE来控制django加载不同的settings文件
    profile = os.environ.get('MY_BLOG_PROFILE', 'product')
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "my_blog.settings.%s" % profile)
    try:
        from django.core.management import execute_from_command_line
    except ImportError:
        # The above import may fail for some other reason. Ensure that the
        # issue is really that Django is missing to avoid masking other
        # exceptions on Python 2.
        try:
            import django
        except ImportError:
            raise ImportError(
                "Couldn't import Django. Are you sure it's installed and "
                "available on your PYTHONPATH environment variable? Did you "
                "forget to activate a virtual environment?"
            )
        raise
    execute_from_command_line(sys.argv)
