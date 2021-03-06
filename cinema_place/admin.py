from django.contrib import admin
from cinema_place.models import Cinema, Area, Film, FilmCinema, Brand,  Genre, Actor, Director
from django.contrib.gis import admin as geoadmin
from django.contrib.gis.db import models
from mapwidgets.widgets import GooglePointFieldWidget

@admin.register(Area)
class AreaAdmin(admin.ModelAdmin):
    formfield_overrides = {
        models.PointField: {"widget": GooglePointFieldWidget}
    }

@admin.register(Film)
class RateAdmin(admin.ModelAdmin):
    readonly_fields = ('rate','slug')

@admin.register(Genre,Actor,Director,Cinema,FilmCinema)
class CinemaPlaceAdmin(admin.ModelAdmin):
    pass
@admin.register(Brand)
class BrandAdmin(admin.ModelAdmin):
    fields =  ('name','image','image_url')
    readonly_fields = ('image_url',)
