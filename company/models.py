from django.db import models
from auth_user.models import User, Address
import uuid

# Create your models here.
class Supplier(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=244)
    cnpj = models.CharField(max_length=18)
    phone = models.CharField(max_length=11)
    email = models.CharField(max_length=244)

class Company(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=244)
    description = models.TextField()
    cnpj = models.CharField(max_length=18)
    phone = models.CharField(max_length=11)
    email = models.CharField(max_length=244)
    
    fkUser = models.ForeignKey(User, related_name='user_company', on_delete=models.CASCADE)