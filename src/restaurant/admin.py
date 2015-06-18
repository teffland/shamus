from django.contrib import admin
from django import forms
from django.db import models

# Register your models here.
from .models import MenuItem, MenuType, MenuCategory, SliderImage, StaticPage

# Define the Admin Classes for managing in the admin site
class MenuItemAdmin(admin.ModelAdmin):
    formfield_overrides = { models.TextField: {'widget': forms.Textarea(attrs={'class':'ckeditor'})}, }

    class Media:
        js = ('ckeditor/ckeditor.js',) # The , at the end of this list IS important.

    class Meta:
        model = MenuItem

class MenuTypeAdmin(admin.ModelAdmin):
    formfield_overrides = { models.TextField: {'widget': forms.Textarea(attrs={'class':'ckeditor'})}, }

    class Media:
        js = ('ckeditor/ckeditor.js',) # The , at the end of this list IS important.

    class Meta:
        model = MenuType

class MenuCategoryAdmin(admin.ModelAdmin):
    formfield_overrides = { models.TextField: {'widget': forms.Textarea(attrs={'class':'ckeditor'})}, }

    class Media:
        js = ('ckeditor/ckeditor.js',) # The , at the end of this list IS important.

    class Meta:
        model = MenuCategory

class SliderImageAdmin(admin.ModelAdmin):
    formfield_overrides = { models.TextField: {'widget': forms.Textarea(attrs={'class':'ckeditor'})}, }

    class Media:
        js = ('ckeditor/ckeditor.js',) # The , at the end of this list IS important.

    class Meta:
        model = SliderImage

class StaticPageAdmin(admin.ModelAdmin):
    formfield_overrides = { models.TextField: {'widget': forms.Textarea(attrs={'class':'ckeditor'})}, }

    class Media:
        js = ('ckeditor/ckeditor.js',) # The , at the end of this list IS important.

    class Meta:
        model = StaticPage

# Register the Admin models to the admin site
admin.site.register(MenuItem, MenuItemAdmin)
admin.site.register(MenuType, MenuTypeAdmin)
admin.site.register(MenuCategory, MenuCategoryAdmin)
admin.site.register(SliderImage, SliderImageAdmin)
admin.site.register(StaticPage, StaticPageAdmin)
