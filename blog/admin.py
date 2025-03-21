from django.contrib import admin
from .models import Post

# Register your models here.
@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_at', 'slug')
    search_fields = ('title', 'content')
    list_filter = ('created_at',)
    prepopulated_fields = {'slug': ('title',)}
