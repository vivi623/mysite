from django.contrib import admin

# 注册博客的实体
import blog.models as models

class BlogAdmin(admin.ModelAdmin):
    list_display = ('title','author','pubtime')

admin.site.register(models.Article, BlogAdmin)

