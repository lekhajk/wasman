from django.contrib import admin


class WorkedOnFilter(admin.SimpleListFilter):

    title = 'Worked On'
    parameter_name = 'worked_on'

    def lookups(self, request, model_admin):
        return ((0, 'False'),
                (1, 'True'))

    def queryset(self, request, queryset):
        if self.value() == '1':
            return queryset.filter(product_batch__recycler__isnull=False)
        elif self.value() == '0':
            return queryset.filter(product_batch__recycler__isnull=True)
