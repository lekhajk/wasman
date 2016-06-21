from django.shortcuts import render
from django.views.generic.edit import UpdateView
from company.models import Manufacturer, Recycler
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse


def company_profile(request):

    class CompanyUpdate(UpdateView):
        fields = ['name', 'website', 'country', 'state', 'phone_number', 'raw_address']
        model = type(request.user.userprofile.company)
        if model == Recycler:
            fields.append('recyclable_types')

        def get_object(self, query_set=None):
            return self.request.user.userprofile.company

    return CompanyUpdate.as_view(success_url='.')(request)


def product_management(request):
    return HttpResponseRedirect(reverse('admin:index'))