from django.contrib import admin
from django.urls import path, include, re_path
from main import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('main/', include('main.urls', namespace='main')),
    path('article/', include('article.urls', namespace='article')),
    re_path('.*', views.main),
]