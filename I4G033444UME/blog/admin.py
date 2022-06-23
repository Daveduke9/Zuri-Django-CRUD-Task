from django.contrib import admin
from django.forms import SlugField
from .models import Post

class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'status', 'publish',)
    list_filter = ("status",)
    search_fields = ['title', 'content']
    prepopulated_fields = {'slug': ('title',)}
# Register your models here.
admin.site.register(Post, PostAdmin)
