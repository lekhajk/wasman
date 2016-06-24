from django.contrib.auth.models import Group


#Don't change this string'
manufacturer_group_name = 'manufacturer_group'
try:
    manufacturer_group = Group.objects.get(name=manufacturer_group_name)
except Group.DoesNotExist:
    manufacturer_group= None

activation_domain = 'localhost:8000'