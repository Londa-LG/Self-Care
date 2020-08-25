from django.urls import path
from .views import HomeView, PostView

app_name = 'main'

urlpatterns =[
    path('', HomeView,name='Home'),
    path('Post/', PostView, name='Post'),
]