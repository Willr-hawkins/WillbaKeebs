from django.contrib import admin
from .models import Category, Post

class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        'friendly_name',
        'name',
    )

class PostAdmin(admin.ModelAdmin):
    list_display = (
        'category',
        'title',
        'main_image',
        'description',
    )


admin.site.register(Category, CategoryAdmin)
admin.site.register(Post, PostAdmin)