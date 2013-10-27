from django.contrib import admin
from modeltranslation.admin import TranslationAdmin
from django.utils.translation import ugettext_lazy as _
from .models import *


# ==================================================
#  ADMIN ACTIONS
# ==================================================

def make_approved(modeladmin, request, queryset):
    queryset.update(status='a')
make_approved.short_description = _("Mark selected as approved")


def make_rejected(modeladmin, request, queryset):
    queryset.update(status='r')
make_rejected.short_description = _("Mark selected as rejected")

def make_red(modeladmin, request, queryset):
        queryset.update(wineType='r')
make_red.short_description = _("Mark selected as Red")

def make_white(modeladmin, request, queryset):
        queryset.update(wineType='w')
make_white.short_description = _("Mark selected as White")

# ==================================================
#  STYLING CLASSES
# ==================================================

class CepageInline(admin.TabularInline):
    model = Wine.cepage.through


# ==================================================
#  ADMIN CLASSES
# ==================================================

# -------------------------------------------
class AcidityAdmin(admin.ModelAdmin):
    """ 
    Manage the Acidity fields
    """
    fields = ('acidity', 'order')
    list_display = ['acidity', 'order',  'last_modified', 'created']
    ordering = ['order']


# -------------------------------------------
class AppelationAdmin(admin.ModelAdmin):
    fields =('appelation', 'status')
    list_display = ('appelation', 'is_approved',  'last_modified', 'created')
    ordering = ['status']


# -------------------------------------------
class AromaAdmin(admin.ModelAdmin):
    """ Manage the Aroma fields """
    fields = ('aroma', 'order')
    list_display = ['aroma', 'order',  'last_modified', 'created']
    ordering = ['order']


# -------------------------------------------
class CepageAdmin(admin.ModelAdmin):
    list_display = ['cepage', 'wineType', 'is_approved', 'last_modified', 'created']
    list_filter = ['status']
    actions = [make_rejected, make_approved]
    actions = [make_red, make_white]


# -------------------------------------------
class CountryAdmin(TranslationAdmin):
    """ Manage Countries """
    fields = ('country', 'status')
    list_display = ['country_fr','country_en','is_approved', 'last_modified', 'created']
    list_filter = ['status']
    actions = [make_rejected, make_approved]


# -------------------------------------------
class ProducerAdmin(admin.ModelAdmin):
    fields =('producer', 'status')
    list_display = ('producer', 'is_approved', 'last_modified', 'created')
    ordering = ['status']


# -------------------------------------------
class RegionAdmin(admin.ModelAdmin):
    fields =('region', 'status')
    list_display = ('region', 'is_approved', 'last_modified', 'created')
    ordering = ['status']


# -------------------------------------------
class TeintAdmin(admin.ModelAdmin):
    """ Manage the Teint fields """
    fields = ('teint', 'wineType', 'order')
    list_display = ['teint', 'wineType', 'order', 'last_modified', 'created']
    list_filter = ['wineType']    
    ordering = ['wineType', 'order']
    actions = [make_red, make_white]

# -------------------------------------------
class TasteAdmin(admin.ModelAdmin):
    """ Manage the Taste fields """
    fields = ('taste', 'order')
    list_display = ['taste', 'order', 'last_modified', 'created']
    list_filter = ['taste']    
    ordering = ['order']
    actions = [make_red, make_white]


# -------------------------------------------
class WineAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ('wineType','name','year')}
    list_display = ['name', 'wineType', 'producer', 'appelation', 'list_cepage', 'region', 'country', 'year','code_saq', 'price', 'alcool','rating']
    list_filter = ['producer','wineType', 'country', 'cepage', 'region','appelation']
    search_fields = ['name','producer','appelation','cepage','region','code_saq']
    fieldsets = (
        ('Fiche', {
            'fields': (
                ('name', 'slug', 'producer', 'year'),
                ('appelation','region', 'country'),
                ('cepage','tag'),
                ('date','code_saq', 'alcool', 'price', 'rating'),
            )
        }),
        ('Eye', {
            'fields': ('wineType', 'teint')
        }),
        ('Nose', {
            'fields': ('nose_intensity', 'aroma')
        }),
        ('Mouth', {
            'fields': ('mouth_intensity', 'persistance', 'taste', 'acidity', 'tanin')
        }),
    )


# -------------------------------------------
class TaninAdmin(admin.ModelAdmin):
    list_display = ['tanin','order', 'last_modified', 'created']
    list_filter = ['tanin']
    ordering = ['order']


# -------------------------------------------
class TagAdmin(admin.ModelAdmin):
    list_display = ['tag', 'wineType', 'is_approved', 'last_modified', 'created']
    list_filter = ['status']
    actions = [make_rejected, make_approved]



# ==================================================
#  ADMIN REGISTRATION
# ==================================================

admin.site.register(Acidity, AcidityAdmin)

admin.site.register(Appelation, AppelationAdmin)

admin.site.register(Aroma, AromaAdmin)

admin.site.register(Cepage, CepageAdmin)

admin.site.register(Country, CountryAdmin)

admin.site.register(Producer, ProducerAdmin)

admin.site.register(Region, RegionAdmin)

admin.site.register(Tag, TagAdmin)

admin.site.register(Tanin, TaninAdmin)

admin.site.register(Taste, TasteAdmin)

admin.site.register(Teint, TeintAdmin)

admin.site.register(Wine, WineAdmin)
