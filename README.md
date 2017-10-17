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

