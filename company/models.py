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


class ProductType(WasmanBase):
    name = models.CharField(max_length=120)
    code = models.TextField(blank=True, null=True)

    def __unicode__(self):
        return self.name


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

class Manufacturer(CompanyBase):
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
    recyclable_types = models.ManyToManyField(ProductType)


class Dismantler(CompanyBase):
    product_types = models.ManyToManyField(ProductType)


class Refurbisher(CompanyBase):
    product_types = models.ManyToManyField(ProductType)


class Auditor(CompanyBase):
    pass


class GovernmentAgeny(CompanyBase):
    industry = models.ForeignKey(Industry, null=True, blank=True)


class WasteType(WasmanBase):
    name = models.CharField(max_length = 120)


class Product(WasmanBase):
    name = models.CharField(max_length=120)
    type = models.ForeignKey(ProductType, null=True, blank=True)
    waste_types = models.ManyToManyField(WasteType)
    manufacturer = models.ForeignKey(Manufacturer, null=True, blank=True)
    recyclers = models.ManyToManyField(Recycler)
    auditors = models.ManyToManyField(Auditor)


class ProductBatch(WasmanBase):
    batch_id = models.CharField(max_length=120)
    product = models.ForeignKey(Product)
    recycler = models.ForeignKey(Recycler, null=True, blank=True)
    auditor = models.ForeignKey(Auditor, null=True, blank=True)


class Producer(CompanyBase):
    products = models.ManyToManyField(Product)
    is_extended_producer = models.BooleanField(default=False)

    RETAILER = 're'
    ETAILER = 'et'
    DEALER = 'de'
    producer_types = ((RETAILER, 'Retailer'),
                      (ETAILER, 'Etailer'),
                      (DEALER, 'Dealer'),
                      )
    type = models.CharField(choices=producer_types, max_length=2, null=True, blank=True)
