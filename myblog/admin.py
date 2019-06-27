from django.contrib import admin
from myblog.models import Post
from myblog.models import Category


class PostAdmin(admin.ModelAdmin):
    pass
    
class CategoryAdmin(admin.ModelAdmin):
    pass


admin.site.register(Post)
admin.site.register(Category)
