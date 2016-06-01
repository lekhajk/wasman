from django.db import models
from wasman.models import WasmanBase
from cities.models import Country, Region, City, PostalCode



class Industry(WasmanBase):
    name = models.CharField(max_length=120, null=True, blank=True, unique=True)
    parent = models.ForeignKey("self", blank=True, null=True)
    is_primary = models.BooleanField(default=True)

    def __unicode__(self):
        return self.name

    def save(self, *args, **kwargs):
        if self.parent:
            self.is_primary = False
        super(Industry, self).save(*args, **kwargs)



class CompanyBase(WasmanBase):
    name = models.CharField(max_length=120)
    website = models.URLField(null=True, blank=True)
    #Address fields
    country = models.ForeignKey(Country, null=True, blank=True)
    state = models.ForeignKey(Region, null=True, blank=True)
    city = models.ForeignKey(City, null=True, blank=True)
    city_text = models.CharField(max_length=120, null=True, blank=True)
    zip_code = models.ForeignKey(PostalCode, null=True, blank=True)
    raw_address = models.CharField(max_length=300, null=True, blank=True)
    street_address = models.CharField(max_length=300, null=True, blank=True)
    phone_number = models.CharField(max_length=50, null=True, blank=True)

    class Meta:
        abstract = True

    def __unicode__(self):
        return self.name

class Producer(CompanyBase):
    industry = models.ForeignKey(Industry, null=True, blank=True)
    stock_ticker = models.CharField(max_length=120)

    def primary_industry(self):
        if not self.industry:
            return None
        elif self.industry.is_primary:
            return self.industry.name
        else:
            return self.industry.parent.name


class Recycler(CompanyBase):
    pass


class Auditor(CompanyBase):
    pass


class Product(models.Model):
    name = models.CharField(max_length=120)
    type = models.CharField(max_length=120)
    producer = models.ForeignKey(Producer)
