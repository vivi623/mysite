# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from __future__ import unicode_literals

from django.db import models

# 文章与标签多对多关联表
class ArticlTaglinks(models.Model):
    id = models.BigAutoField(primary_key=True)
    tagid = models.BigIntegerField()
    articleid = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = 'articl_taglinks'
        app_label = 'blog'

# 文章表
class Article(models.Model):
    id = models.BigAutoField(primary_key=True)
    cateid = models.BigIntegerField()
    catename = models.CharField(max_length=50, blank=True, null=True)
    authorid = models.BigIntegerField(blank=True, null=True)
    author = models.CharField(max_length=50, blank=True, null=True)
    title = models.CharField(max_length=150, blank=True, null=True)
    url = models.CharField(max_length=200, blank=True, null=True)
    content = models.TextField(blank=True, null=True)
    abstract = models.CharField(max_length=500, blank=True, null=True)
    status = models.IntegerField()
    isrecommend = models.IntegerField(blank=True, null=True)
    isupstairs = models.IntegerField(blank=True, null=True)
    articleflag = models.IntegerField(blank=True, null=True)
    pubtime = models.DateTimeField(blank=True, null=True)
    createtime = models.DateTimeField(auto_now_add=True)
    modifytime = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'article'
        app_label = 'blog'

#文章分类表
class ArticleCategory(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=50)
    articlenum = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'article_category'
        app_label = 'blog'

# 文章标签表
class ArticleTags(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=50, blank=True, null=True)
    articlenum = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'article_tags'
        app_label = 'blog'
