from django.db import models
from .managers import UserManager
from django.contrib.auth.models import AbstractUser
import uuid
# Create your models here.

class User(AbstractUser):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=244, unique=False)
    email = models.EmailField(max_length=86, unique=True)
    cpf = models.CharField(max_length=11)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name']

    objects = UserManager()

    def __str__(self):
        return self.name

class Address(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    road = models.CharField(max_length=144)
    city = models.CharField(max_length=84)
    number = models.IntegerField()
    cep = models.CharField()

class Role(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=244)

    def __str__(self):
        return self.name