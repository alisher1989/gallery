from django.contrib import admin
from webapp.models import Photo, Comment


class PhotoAdmin(admin.ModelAdmin):
    list_display = ['pk', 'image', 'signature', 'created_at', 'like_amount', 'author']
    list_filter = ['created_at']
    search_fields = ['signature', 'created_at']
    fields = ['image', 'signature', 'created_at', 'like_amount', 'author']
    readonly_fields = ['created_at']


admin.site.register(Photo, PhotoAdmin)
admin.site.register(Comment)