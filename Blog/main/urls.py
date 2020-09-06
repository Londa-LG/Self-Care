from django.urls import path, include
from .views import Home, BlogPosts, ViewedPost, Search, Categories_View

app_name= 'main'

urlpatterns = [
    path('', Home, name='home'),
    path('blog/', BlogPosts, name='blog'),
    path('post/<int:id>/', ViewedPost, name='post'),
    path('search/', Search, name='search_results'),
    path('categories/<int:id>/', Categories_View, name='categories'),
]
