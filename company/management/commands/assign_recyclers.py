from django.core.management.base import BaseCommand
from company.models import ProductBatch
import random


class Command(BaseCommand):
    def handle(self, *args, **options):
        batches = ProductBatch.objects.filter(recycer__isnull=True)
        for batch in batches:
            batch.recycler = random.sample(list(batch.product.recyclers.all()))
            batch.save()
