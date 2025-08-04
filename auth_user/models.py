from django.db import models
from .managers import UserManager
from django.contrib.auth.models import AbstractUser
import uuid
# Create your models here.

class User(AbstractUser):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=244)
    email = models.EmailField(max_length=86, unique=True)
    cpf = models.CharField(max_length=11)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name']

    objects = UserManager()

    def __str__(self):
        return self.name
    
class Role(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=244)

    def __str__(self):
        return self.name
    
class UserRole(models.Model):
    fk_user = models.ForeignKey(User, related_name='user_atrib_role', on_delete=models.CASCADE)
    fk_role = models.ForeignKey(Role, related_name='role_atrib_role', on_delete=models.CASCADE)

class Permission(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=84)

class UserPermissions(models.Model):
    fk_user = models.ForeignKey(User, related_name='user_atrib_perm', on_delete=models.CASCADE)
    fk_role = models.ForeignKey(Role, related_name='role_atrib_perm', on_delete=models.CASCADE)