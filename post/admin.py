from django.contrib import admin
from .models import Post, UpdateImage

# Register your models here.
@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    """
    Admin interface to control the posting of document based on user privileges.
    """
    model = Post
    list_display = ['title', 'content', 'img', 'url', 'date_published', 'published']
    list_filter = ['published']
    search_fields = ['title', 'content']
    actions = ['publish_posts', 'unpublish_posts']

    def publish_posts(self, request, queryset):
        queryset.update(published=True)

    def unpublish_posts(self, request, queryset):
        queryset.update(published=False)

    publish_posts.short_description = "Publish selected posts"
    unpublish_posts.short_description = "Unpublish selected posts"

@admin.register(UpdateImage)
class ImageUpdateAdmin(admin.ModelAdmin):
    """
    Admin interface to control the upload and updating of images.
    """
    model = UpdateImage
    list_display = ['img_title', 'img_tag', 'img', 'date_published', 'published']
    list_filter = ['published']
    search_fields = ['img_tag']
    actions = ['publish_images', 'unpublish_images']

    def publish_images(self, request, queryset):
        queryset.update(published=True)

    def unpublish_images(self, request, queryset):
        queryset.update(published=False)

    publish_images.short_description = "Publish selected images"
    unpublish_images.short_description = "Unpublish selected images"
