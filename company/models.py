from django.db import models
from wasman.models import WasmanBase
from cities.models import Country, Region, City, PostalCode
from company.localsettings import max_rec_aud_pairs
import random



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
        if self.code:
            return '%s - %s' %(self.name, self.code)
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
    capacity = models.IntegerField(null=True, blank=True)


class Dismantler(CompanyBase):
    product_types = models.ManyToManyField(ProductType)


class Refurbisher(CompanyBase):
    product_types = models.ManyToManyField(ProductType)


class Auditor(CompanyBase):
    pass


class GovernmentAgency(CompanyBase):
    industry = models.ForeignKey(Industry, null=True, blank=True)


class WasteType(WasmanBase):
    name = models.CharField(max_length = 120)
    is_hazardous = models.BooleanField(default=False)

    def __unicode__(self):
        return self.name


class Product(WasmanBase):
    name = models.CharField(max_length=120)
    type = models.ForeignKey(ProductType, null=True, blank=True, on_delete=models.SET_NULL)
    waste_types = models.ManyToManyField(WasteType, blank=True)
    manufacturer = models.ForeignKey(Manufacturer, null=True, blank=True)
    recyclers = models.ManyToManyField(Recycler, blank=True)
    auditors = models.ManyToManyField(Auditor, blank=True)

    def __unicode__(self):
        return self.name


class ProductBatch(WasmanBase):
    batch_id = models.CharField(max_length=120)
    product = models.ForeignKey(Product)
    recycler = models.ForeignKey(Recycler, null=True, blank=True)
    auditor = models.ForeignKey(Auditor, null=True, blank=True)

    def __unicode__(self):
        return '%s | %s' % (unicode(self.product), self.batch_id)
    
    def save(self, *args, **kwargs):
        created = not bool(self.pk)
        super(ProductBatch, self).save(*args, **kwargs)
        if created:
            ProductBatchEph.create_product_batch_eph(self)


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


class RecAudPair(WasmanBase):
    recycler = models.ForeignKey(Recycler)
    auditor = models.ForeignKey(Auditor)

    def __unicode__(self):
        return '%s | %s' % (self.recycler, self.auditor)

    @property
    def pair(self):
        return (self.recycler, self.auditor)


class ProductBatchEph(WasmanBase):
    product_batch = models.OneToOneField(ProductBatch)
    rec_aud_pairs = models.ManyToManyField(RecAudPair, blank=True)

    def __unicode__(self):
        return unicode(self.product_batch)

    @classmethod
    def create_product_batch_eph(cls, product_batch):
        recyclers = product_batch.product.recyclers.all()
        auditors = product_batch.product.auditors.all()
        pairs_count = min([len(recyclers), len(auditors), max_rec_aud_pairs])
        if pairs_count:
            batch_eph = cls.objects.create(product_batch=product_batch)
            pairs = zip(random.sample(recyclers, pairs_count), random.sample(auditors, pairs_count))
            for pair in pairs:
                ra_pair, _ = RecAudPair.objects.get_or_create(recycler=pair[0], auditor=pair[1])
                batch_eph.rec_aud_pairs.add(ra_pair)
