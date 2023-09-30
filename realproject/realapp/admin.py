from django.contrib import admin

# Register your models here.
from realapp.models import House
from realapp.models import LandPlot
from realapp.models import Car

# Register your models here.
class HouseAdmin(admin.ModelAdmin):
  list_display = ("category", "price", "address",)
admin.site.register(House,HouseAdmin)

class LandPlotAdmin(admin.ModelAdmin):
  list_display = ("category", "price", "address",)
admin.site.register(LandPlot,LandPlotAdmin)

class CarAdmin(admin.ModelAdmin):
  list_display = ("category", "use", "price")
admin.site.register(Car, CarAdmin)