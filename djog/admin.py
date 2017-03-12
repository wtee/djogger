from django.contrib import admin

from . import models

class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'created')
    prepopulated_fields = {'slug': ('title',)}

class TagAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('tag',)}

class PageAdmin(admin.ModelAdmin):
    list_display = ('title',)
    prepopulated_fields = {'slug': ('title',)}

admin.site.register(models.Post, PostAdmin)
admin.site.register(models.Tag, TagAdmin)
admin.site.register(models.Page, PageAdmin)