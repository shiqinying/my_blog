1,安装好依赖包后需要  python manage.py makemigrations 会报错
需要pip uninstall xadmin
然后通过git 安装  pip install https://github.com/the5fire/django-xadmin/archive/0.6.1.tar.gz
或者pip install git+git://github.com/sshwsfc/xadmin.git
(首先通过pip install xadmin安装再卸载能解决依赖包问题)

2,创建数据库 CREATE DATABASE my_blog DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci
3,通过设置系统环境变量MY_BLOG_PROFILE来控制settings配置
  设置方法export MY_BLOG_PROFILE=product/develop 


