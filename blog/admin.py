from django.contrib import admin

# Register your models here.
from .models import Author,Post,Tag, Comment

class PostAdmin(admin.ModelAdmin):
    list_filter = ("author", "tags", "date")
    list_display = ("title", "date", "author")
    prepopulated_fields = {"slug": ("title",)}

class CommentAdmin(admin.ModelAdmin):
    list_display = ("username", "post")
    
admin.site.register(Author)
admin.site.register(Post, PostAdmin)
admin.site.register(Tag)
admin.site.register(Comment, CommentAdmin)