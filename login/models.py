from django.db import models
from django.contrib.auth.models import User
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey


class UserProfile(models.Model):
    user = models.OneToOneField(User, primary_key=True)
    phone_number = models.CharField(max_length=20, null=True, blank=True)
    content_type = models.ForeignKey(ContentType, null=True, blank=True)
    object_id = models.PositiveIntegerField(null=True, blank=True)
    company = GenericForeignKey('content_type', 'object_id')
