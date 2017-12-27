from django.contrib import admin

from .models import Post, Tag


class TagInline(admin.StackedInline):
    model = Tag
    extra = 2


class PostAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,        {'fields': ['title', 'content_text', 'featured_image']}),
        ('Date info', {'fields': ['date'], 'classes': ['collapse']}),
    ]
    # inlines = [TagInline]


class TagAdmin(admin.ModelAdmin):
    fields = ['name']


admin.site.register(Post, PostAdmin)
admin.site.register(Tag, TagAdmin)

