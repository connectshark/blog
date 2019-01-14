from django.shortcuts import render

# Create your views here.
def article(request):
    '''
    Render the article page
    '''
    return render(request, 'article/article.html')