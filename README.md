# mysite
python+django学习
### 常用命令
1.同步数据库
~~~
python manage.py makemigrations appname #生成模型  blog是app名
python manage.py migrate appname  #同步数据库
~~~
2.根据数据库已有表生成Model
~~~
python manage.py inspectdb --database=dbname
~~~
3.创建一个app
~~~
python manage.py startapp appname
~~~
4.启动服务
~~~
python manage.py runserver 0.0.0.0:8000
~~~
5.静态文件手机
~~~
python manage.py collectstatic
~~~
### 环境准备
1.numpy,scipy,pandas
~~~
http://www.lfd.uci.edu/~gohlke/pythonlibs/
~~~
