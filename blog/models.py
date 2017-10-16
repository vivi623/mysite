from django.db import models

# Create your models here.

class Category(models.Model):
    name = models.CharField('name',max_length=16)


class Tag(models.Model):
    name = models.CharField('name',max_length=16)


class Blog(models.Model):
    title = models.CharField('title',max_length=100)
    author = models.CharField('author',max_length=50)
    content = models.TextField('content')
    created= models.DateTimeField('pubdate',auto_now_add=True)
    category = models.ForeignKey(Category,verbose_name='category')
    tags = models.ManyToManyField(Tag,verbose_name='name')

    # class Meta: 自定义数据库表中的名称 命令：python manage.py inspectdb --database=databasecopy
    #     managed = False
    #     db_table = 'Blog'

class Comment(models.Model):
    blog = models.ForeignKey(Blog,verbose_name='blog')

    name = models.CharField('Name',max_length=50)
    email = models.EmailField('Email')
    content = models.CharField('Content',max_length=250)

    created = models.DateTimeField('pubdate',auto_now_add=True)



