from django.contrib import admin


from renovation.models import Scene, Package, Furniture_category, Furniture

# Register your models here.

admin.site.register(Scene) 
admin.site.register(Package) 
admin.site.register(Furniture_category) 
admin.site.register(Furniture)