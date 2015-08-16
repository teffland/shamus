from django.contrib import admin
from django import forms
from django.db import models
from solo.admin import SingletonModelAdmin

# Register your models here.
from .models import MenuItem, ItemOption, MenuType, MenuCategory, SliderImage, StaticPage, FrontPageBlurb, MaintenanceMode

# Define the Admin Classes for managing in the admin site
class ItemOptionAdmin(admin.ModelAdmin):
    formfield_overrides = { models.TextField: {'widget': forms.Textarea(attrs={'class':'ckeditor'})}, }

    class Media:
        js = ('ckeditor/ckeditor.js',) # The , at the end of this list IS important.

    class Meta:
        model = ItemOption

class ItemOptionInline(admin.StackedInline):
    model = ItemOption
    extra = 1 # only one blank in form set

class MenuItemAdmin(admin.ModelAdmin):
    # formfield_overrides = { models.TextField: {'widget': forms.Textarea(attrs={'class':'ckeditor'})}, }

    # class Media:
    #     js = ('ckeditor/ckeditor.js',) # The , at the end of this list IS important.
    inlines = [ ItemOptionInline ]
    ordering = ('menu_category__order_affinity',)
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

class FrontPageBlurbAdmin(admin.ModelAdmin):
    formfield_overrides = { models.TextField: {'widget': forms.Textarea(attrs={'class':'ckeditor'})}, }

    class Media:
        js = ('ckeditor/ckeditor.js',) # The , at the end of this list IS important.

    class Meta:
        model = FrontPageBlurb



# Register the Admin models to the admin site
admin.site.register(MenuItem, MenuItemAdmin)
admin.site.register(ItemOption, ItemOptionAdmin)
admin.site.register(MenuType, MenuTypeAdmin)
admin.site.register(MenuCategory, MenuCategoryAdmin)
admin.site.register(SliderImage, SliderImageAdmin)
admin.site.register(StaticPage, StaticPageAdmin)
admin.site.register(FrontPageBlurb, FrontPageBlurbAdmin)
admin.site.register(MaintenanceMode, SingletonModelAdmin)