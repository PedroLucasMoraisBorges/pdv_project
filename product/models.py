from django.db import models
from auth_user.models import User
from company.models import *
import uuid

choices = [
    ('g', 'Grama'),
    ('kg', 'Quilo'),
    ('un', 'Unidade'),
    ('ml', 'Mililitro'),
    ('l', 'Litro')
]

# Create your models here.
class Product(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=244)
    description = models.TextField()
    sku = models.CharField(max_length=244)
    barcode = models.CharField(max_length=13)
    unit = models.CharField(choices=choices, max_length=2)
    created_at = models.ForeignKey(User, related_name='product_created_at_user', on_delete=models.RESTRICT)

class StockEntries(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    fk_product = models.ForeignKey(Product, related_name='product_entries', on_delete=models.RESTRICT)
    quantity = models.IntegerField()
    price = models.FloatField()
    fkSupplier = models.ForeignKey(Supplier, related_name='responsability_supplier', on_delete=models.RESTRICT)
    date = models.DateTimeField()

class StockOutputs(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    fk_product = models.ForeignKey(Product, related_name='product_outputs', on_delete=models.RESTRICT)
    quantity = models.IntegerField()
    reason = models.TextField()
    date = models.DateTimeField()