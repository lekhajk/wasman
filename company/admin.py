from django.contrib import admin
from company.models import Manufacturer, Product
# 
# Register your models here.
#

class ProductAdmin(admin.ModelAdmin):
    fields = ('name', 'type', 'waste_types', 'recyclers', 'auditors')
    list_display = ('name', )

    def get_queryset(self, request):
        qs = super(ProductAdmin, self).get_queryset(request)
        if request.user.is_superuser:
            return qs
        return qs.filter(manufacturer=request.user.userprofile.company)
    
    def save_model(self, request, obj, form, change):
        super(ProductAdmin, self).save_model(request, obj, form, change)
        if not obj.manufacturer:
            obj.manufacturer = request.user.userprofile.company
            obj.save()

admin.site.register(Manufacturer)
admin.site.register(Product, ProductAdmin)