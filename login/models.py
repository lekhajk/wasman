from django.db import models
from django.contrib.auth.models import User
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey
from login.localsettings import activation_domain
from django.core.mail import send_mail


class UserProfile(models.Model):
    user = models.OneToOneField(User, primary_key=True)
    phone_number = models.CharField(max_length=20, null=True, blank=True)
    content_type = models.ForeignKey(ContentType, null=True, blank=True)
    object_id = models.PositiveIntegerField(null=True, blank=True)
    company = GenericForeignKey('content_type', 'object_id')
    activation_key = models.CharField(max_length=40)

    def send_activation_mail(self):
        link = "http://%s/activate/%s" % (activation_domain, self.activation_key)
        message = 'Use the following link to activate your account'
        subject = 'Activation of your secondshub user account'
        message = '%s \n %s' % (message, link)
        send_mail(subject, message, '', [self.user.email, ])