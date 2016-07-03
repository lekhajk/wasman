from django.contrib import admin
from company.models import Product, ProductBatch, Recycler, WasteType,\
    ProductBatchEph, RecAudPair
from django import forms
from company.filters import WorkedOnFilter
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
    readonly_fields = ('recycler', 'auditor', )
    list_display = ('batch_id', 'product', 'recycler', 'auditor', )

    def get_queryset(self, request):
        qs = super(ProductBatchAdmin, self).get_queryset(request)
        if request.user.is_superuser:
            return qs
        return qs.filter(product__manufacturer=request.user.userprofile.company)

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        try:
            if db_field.name == 'product':
                kwargs["queryset"] = Product.objects.filter(manufacturer=request.user.userprofile.company)
            return super(ProductBatchAdmin, self).formfield_for_foreignkey(db_field, request, **kwargs)
        except:
            return super(ProductBatchAdmin, self).formfield_for_foreignkey(db_field, request, **kwargs)

 
class RecyclerAdmin(admin.ModelAdmin):
    fields = ('name', 'state', 'capacity', 'raw_address')
    list_display = ('name', 'state', 'capacity', 'raw_address')


class WasteTypeAdmin(admin.ModelAdmin):
    fields = ('name', 'is_harzardous')
    list_display = ('name', 'is_hazardous')


class ProductBatchEphForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(ProductBatchEphForm, self).__init__(*args, **kwargs)
        pairs = self.instance.rec_aud_pairs.all()
        choices = [(a.id, a) for a in pairs]
        self.fields['recycler_auditor_pair'] = forms.ChoiceField(choices = choices)

    
    recycler_auditor_pair = forms.CharField()

    class Meta:
        model = ProductBatchEph
        fields = ('recycler_auditor_pair', )


class ProductBatchEphAdmin(admin.ModelAdmin):
    form = ProductBatchEphForm
    list_display = ('id', )
    list_filter = (WorkedOnFilter, )

    def save_model(self, request, obj, form, change):
        super(ProductBatchEphAdmin, self).save_model(request, obj, form, change)
        if form.cleaned_data['recycler_auditor_pair']:
            rec_aud_pair = RecAudPair.objects.get(id=form.cleaned_data['recycler_auditor_pair'])
            obj.product_batch.recycler = rec_aud_pair.recycler
            obj.product_batch.auditor = rec_aud_pair.auditor
            obj.product_batch.save()


admin.site.register(Product, ProductAdmin)
admin.site.register(ProductBatch, ProductBatchAdmin)
admin.site.register(Recycler, RecyclerAdmin)
admin.site.register(WasteType, WasteTypeAdmin)
admin.site.register(ProductBatchEph, ProductBatchEphAdmin)