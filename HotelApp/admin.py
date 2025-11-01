from django.contrib import admin
from .models import Hotel,HotelImages,Amenities,HotelBooking
# Register your models here.
class HotelAdmin(admin.ModelAdmin):
    filter_horizontal = ('amenities',) 


admin.site.register(HotelImages)
admin.site.register(Amenities)
admin.site.register(HotelBooking)
admin.site.register(Hotel,HotelAdmin)