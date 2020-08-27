from django.contrib import admin
from .models import BlogPost, PostCard, MetaInfo, Category, SubCategory

admin.site.register(BlogPost)
admin.site.register(PostCard)
admin.site.register(MetaInfo)
admin.site.register(Category)
admin.site.register(SubCategory)


