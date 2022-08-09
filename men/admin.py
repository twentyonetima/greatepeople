from django.contrib import admin
from django import forms
from django.utils.safestring import mark_safe

from .models import *
# Register your models here.


from ckeditor_uploader.widgets import CKEditorUploadingWidget


class MenAdminForm(forms.ModelForm):
    content = forms.CharField(label='Description', widget=CKEditorUploadingWidget())

    class Meta:
        model = Men
        fields = '__all__'


@admin.register(Men)
class MenAdmin(admin.ModelAdmin):
    list_display = ('id', 'full_name', 'get_image', 'time_create',
                    'time_update', 'is_published')
    list_display_links = ('id', 'full_name')
    search_fields = ('full_name', 'content', 'cat__name')
    list_filter = ('cat',)
    list_editable = ('is_published',)
    form = MenAdminForm
    fieldsets = (
        ("Full name", {
            "fields": (('name', 'last_name'),)
        }),
        (None, {
            "fields": (('photo', 'get_image'),)
        }),
        ("Content", {
            'classes': ('collapse',),
            "fields": (('content',),)
        }),
        ("Time alive", {
            "fields": (('year_of_birth', 'year_of_death', 'age'),)
        }),
        ("Options", {
            "fields": (('is_published', 'cat', 'slug'),)
        }),
    )

    def get_image(self, obj):
        return mark_safe(f'<img src={obj.photo.url} width="50" height="60"')

    get_image.short_description = 'Image'

    readonly_fields = ('get_image',)


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'url')
    list_display_links = ('id', 'name')
    readonly_fields = ('description',)
    prepopulated_fields = {'url': ('name',)}


admin.site.site_title = 'Greate men'
admin.site.site_header = 'Greate men'
