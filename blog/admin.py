from django.contrib import admin

from blog.models import BlogRecord


@admin.register(BlogRecord)
class BlogRecordAdmin(admin.ModelAdmin):
    list_display = ("id", "title", "description", "is_published", "count_views")
    list_filter = ("is_published",)
    search_fields = ("title", "description")