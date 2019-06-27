from django.contrib import admin
from myblog.models import Post
from myblog.models import Category


class CategoryInline(admin.TabularInLine):
    model = Category


class PostAdmin(admin.ModelAdmin):
    inlines = [
        CategoryInline
    ]

    
class CategoryAdmin(admin.ModelAdmin):
    pass


admin.site.register(Post)
admin.site.register(Category)
