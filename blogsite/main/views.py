from django.shortcuts import render
from .models import BlogPost, PostCard

def HomeView(request):
    cards = PostCard.objects.all()
    content = {'cards': cards}
    return render(request,'main/home.html',content)

def PostView(request,id):
    post = BlogPost.objects.filter(id=id)
    content = {'post': post}
    return render(request, 'main/post.html', content)
