from django.db import models
import uuid

# Create your models here.
class Supplier(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=244)
    cnpj = models.CharField(max_length=18)
    phone = models.CharField(max_length=11)
    email = models.CharField(max_length=244)