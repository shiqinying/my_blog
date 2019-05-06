安装好依赖包后需要  python manage.py makemigrations 会报错
需要pip uninstall xadmin
然后通过git 安装  pip install https://github.com/the5fire/django-xadmin/archive/0.6.1.tar.gz
或者pip install git+git://github.com/sshwsfc/xadmin.git
(首先通过pip install xadmin安装再卸载能解决依赖包问题)
