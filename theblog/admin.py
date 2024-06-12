# blog/admin.py
from django.contrib import admin
from .models import Post, Comment, Category

class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'title_tag', 'author', 'created_at', 'updated_at', 'is_public')
    list_filter = ('is_public', 'created_at', 'updated_at', 'author')
    search_fields = ('title', 'body')
    date_hierarchy = 'created_at'
    ordering = ('-created_at',)
    fields = ('title', 'title_tag', 'author', 'body', 'is_public', 'password', 'image', 'media_link')

    def save_model(self, request, obj, form, change):
        if not obj.pk:  # Check if this is a new object
            obj.author = request.user
        super().save_model(request, obj, form, change)

class CommentAdmin(admin.ModelAdmin):
    list_display = ('author', 'post', 'created_at', 'approved')
    list_filter = ('approved', 'created_at', 'author')
    search_fields = ('body', 'author__username')
    actions = ['approve_comments']

    def approve_comments(self, request, queryset):
        queryset.update(approved=True)
    approve_comments.short_description = "Approve selected comments"

admin.site.register(Post, PostAdmin)
admin.site.register(Comment, CommentAdmin)
admin.site.register(Category)
