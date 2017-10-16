from django.http import Http404
from django.shortcuts import render

from blog.models import Blog, Category


# Create your views here.
def index(request):
    latest_articles_list = Blog.objects.order_by('-created')
    if len(latest_articles_list) > 5:
        latest_articles_list = latest_articles_list[-5:]
    category_list = Category.objects.order_by('-name')
    context = {
        'latest_blog_list' : latest_articles_list,
        'category_list' : category_list,
    }
    return render(request,'blog/index.html',context)

def article(request,article_id):
    try:
        article = Blog.objects.get(pk=article_id)
        tags = article.tags.all()
    except Blog.DoesNotExist:
        raise Http404("Article does not exist")
    return render(request, 'blog/article.html', {'article': article,'tags':tags})