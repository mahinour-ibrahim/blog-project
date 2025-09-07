from django.contrib import admin
from .models import Post

class PostAdmin(admin.ModelAdmin):
    list_display = ("title", "author", "created_at", "updated_at", "is_published")
    list_filter = ("is_published", "created_at", "author")
    search_fields = ("title", "content", "author")

admin.site.register(Post, PostAdmin)