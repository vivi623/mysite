from django.http import Http404
from django.shortcuts import render

from blog.models import Article, ArticleCategory


# Create your views here.
def index(request):
    latest_articles_list = Article.objects.order_by('-pubtime')
    # if len(latest_articles_list) > 5:
    #     latest_articles_list = latest_articles_list[-5:]
    category_list = ArticleCategory.objects.order_by('-name')
    context = {
        'latest_blog_list' : latest_articles_list,
        'category_list' : category_list,
    }
    return render(request,'blog/index.html',context)

def article(request,article_id):
    try:
        article = Article.objects.get(pk=article_id)
    except Article.DoesNotExist:
        raise Http404("Article does not exist")
    return render(request, 'blog/article.html', {'article': article})