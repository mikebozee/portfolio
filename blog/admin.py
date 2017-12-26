from django.contrib import admin

from .models import Post


class PostAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,        {'fields': ['title', 'content_text', 'featured_image']}),
        ('Date info', {'fields': ['date']}),
    ]


admin.site.register(Post, PostAdmin)

