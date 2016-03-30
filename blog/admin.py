from django.contrib import admin
from .models import Post, Blog, Category

class BlogAdmin(admin.ModelAdmin):
    exclude = ['posted']
    prepopulated_fields = {'slug': ('title',)}

class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}

# Register your models here.

admin.site.register(Post)
admin.site.register(Blog, BlogAdmin)
admin.site.register(Category, CategoryAdmin)
