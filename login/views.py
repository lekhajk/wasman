#views.py
from login.forms import *
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.views.decorators.csrf import csrf_protect
from django.shortcuts import render_to_response, render
from django.http import HttpResponseRedirect
from django.template import RequestContext
from .models import UserProfile
from company.models import Manufacturer, Recycler
from django.views.generic import DetailView, UpdateView
from django.contrib.contenttypes.models import ContentType
from login.localsettings import manufacturer_group


COMPANY_TYPE_DICT = {'ma': Manufacturer,
                     're': Recycler}

@csrf_protect
def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = User.objects.create_user(
            username=form.cleaned_data['username'],
            password=form.cleaned_data['password1'],
            email=form.cleaned_data['email']
            )
            print form.cleaned_data['password1']

            type = form.cleaned_data['type']
            company_model = COMPANY_TYPE_DICT[type]
            new = company_model.objects.create()
            _ = UserProfile.objects.get_or_create(user=user,
                                                  content_type=ContentType.objects.get_for_model(company_model),
                                                  object_id=new.id)

            if company_model == Manufacturer:
                user.groups.add(manufacturer_group)

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


@login_required
def profile_home(request):
    if type(request.user.userprofile.company) == Manufacturer:
        return render_to_response('login/manufacturer_profile_home.html')
    elif type(request.user.userprofile.company) == Recycler:
        return render_to_response('login/recycler_profile_home.html')


class UserProfileDetail(DetailView):
    model = UserProfile


class UserProfileUpdate(UpdateView):
    model = UserProfile
    fields = ('phone_number',)

    def get_object(self, queryset=None):
        return self.request.user.userprofile
