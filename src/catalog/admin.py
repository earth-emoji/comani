from django.contrib import admin
from django.utils.translation import ugettext_lazy as _

from .models import Category, Product, Reservation, Dog, DogBreed

# Register your models here.
admin.site.register(Category)
admin.site.register(Dog)
admin.site.register(DogBreed)
admin.site.register(Reservation)


class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'vendor', 'acl', 'is_dog')

    def vendor(self, obj):
        return obj.vendor.business_name

    def acl(self, obj):
        return obj.acl.name

admin.site.register(Product, ProductAdmin)