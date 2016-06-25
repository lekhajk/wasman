from django.contrib import admin
from company.models import Product, ProductBatch, Recycler
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


class ProductBatchAdmin(admin.ModelAdmin):
    fields = ('batch_id', 'product', 'recycler', 'auditor', )
    list_display = ('batch_id', 'product', 'recycler', 'auditor', )

    def get_queryset(self, request):
        qs = super(ProductBatchAdmin, self).get_queryset(request)
        if request.user.is_superuser:
            return qs
        return qs.filter(product__manufacturer=request.user.userprofile.company)

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == 'product':
            kwargs["queryset"] = Product.objects.filter(manufacturer=request.user.userprofile.company)
        return super(ProductBatchAdmin, self).formfield_for_foreignkey(db_field, request, **kwargs)

 
class RecyclerAdmin(admin.ModelAdmin):
    fields = ('name', 'state', 'capacity', 'raw_address')
    list_display = ('name', 'state', 'capacity', 'raw_address')


admin.site.register(Product, ProductAdmin)
admin.site.register(ProductBatch, ProductBatchAdmin)
admin.site.register(Recycler, RecyclerAdmin)