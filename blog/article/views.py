from django.shortcuts import render

from article.models import Article,Comment


def article(request):
    '''
    Render the article page
    '''
    articles = {}
    for article in Article.objects.all():
        articles.update({article:Comment.objects.filter(article=article)})
    context = {'articles':articles}
    return render(request, 'article/article.html', context)