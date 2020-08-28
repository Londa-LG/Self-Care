from django.urls import path
from .views import HomeView, PostView, Style

app_name = 'main'

urlpatterns =[
    path('', HomeView,name='Home'),
    path('Post/<int:id>/', PostView, name='Post'),
]
