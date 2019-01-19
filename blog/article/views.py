from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from article.models import Article,Comment
from article.forms import ArticleForm

def article(request):
    '''
    Render the article page
    '''
    articles = {}
    for article in Article.objects.all():
        articles.update({article:Comment.objects.filter(article=article)})
    context = {'articles':articles}
    return render(request, 'article/article.html', context)

def articleCreate(request):
    '''
    Create a new article instance
        1. If method is GET, render an empty form
        2. If method is POST, perform form validation and display error messages if the form is invalid
        3. Save the form to the model and redirect the user to the article page
    '''
    template = 'article/articleCreate.html'
    if request.method == 'GET':
        return render(request, template, {'articleForm':ArticleForm()})
    
    #post
    articleForm = ArticleForm(request.POST)
    if not articleForm.is_valid():
        return render(request, template, {'articleForm':articleForm})
    
    articleForm.save()
    messages.success(request, '文章已新增')
    return redirect('article:article')

def articleRead(request, articleId):
    '''
    Read an article
        1. Get the "article" instance using "articleId"; redirect to the 404 page if not found
        2. Render the articleRead template with the article instance and its
           associated comments
    '''
    article = get_object_or_404(Article, id=articleId)
    context = {
        'article':article,
        'comments': Comment.objects.filter(article=article)
    }
    return render(request, 'article/articleRead.html', context)