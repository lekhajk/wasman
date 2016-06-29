#views.py
from login.forms import *
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.views.decorators.csrf import csrf_protect
from django.shortcuts import render_to_response, render
from django.http import HttpResponseRedirect
from django.template import RequestContext
from .models import UserProfile
from company.models import Manufacturer, Recycler, Auditor,\
    GovernmentAgency
from django.views.generic import DetailView, UpdateView
from django.contrib.contenttypes.models import ContentType
from login.localsettings import manufacturer_group, government_agency_group
from django.db import transaction
import random
import hashlib


COMPANY_TYPE_DICT = {'ma': Manufacturer,
                     're': Recycler,
                     'ga': GovernmentAgency,
                     'au': Auditor}


@csrf_protect
@transaction.atomic
def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = User.objects.create_user(
            username=form.cleaned_data['username'],
            password=form.cleaned_data['password1'],
            email=form.cleaned_data['email']
            )
            user.is_active = False
            user.save()

            type = form.cleaned_data['type']
            company_model = COMPANY_TYPE_DICT[type]
            new = company_model.objects.create()

            k = hashlib.sha1(str(random.randint(10000000, 99999999)) + form.cleaned_data['username']).hexdigest()
            phone_number = form.cleaned_data['phone_number']
            up = UserProfile.objects.create(user=user,
                                            content_type=ContentType.objects.get_for_model(company_model),
                                            object_id=new.id,
                                            activation_key=k,
                                            phone_number=phone_number)
            
            up.send_activation_mail()
            if company_model == Manufacturer:
                user.is_staff = True
                user.groups.add(manufacturer_group)
                user.save()
            if company_model == GovernmentAgency:
                user.is_staff = True
                user.groups.add(government_agency_group)

            return HttpResponseRedirect('/register/success/')
    else:
        form = RegistrationForm()
    variables = RequestContext(request, {
    'form': form
    })
 
    return render_to_response(
    'registration/register.html',
    variables,
    )

 
def register_success(request):
    return render_to_response(
    'registration/success.html',
    )

 
def logout_page(request):
    logout(request)
    return HttpResponseRedirect('/')


@login_required
def home(request):
    return render_to_response(
    'home.html',
    { 'user': request.user }
    )


def activation(request, activation_key):
    up = UserProfile.objects.get(activation_key=activation_key)
    user = up.user
    user.is_active = True
    user.save()
    return render_to_response('registration/activation_success.html')
    
@login_required
def profile_home(request):
    if type(request.user.userprofile.company) == Manufacturer:
        return render_to_response('login/manufacturer_profile_home.html')
    elif type(request.user.userprofile.company) == GovernmentAgency:
        return render_to_response('login/ga_profile_home.html')
    elif type(request.user.userprofile.company) == Recycler or\
         type(request.user.userprofile.company) == Auditor:
        return render_to_response('login/recycler_profile_home.html')


class UserProfileDetail(DetailView):
    model = UserProfile


class UserProfileUpdate(UpdateView):
    model = UserProfile
    fields = ('phone_number',)

    def get_object(self, queryset=None):
        return self.request.user.userprofile
