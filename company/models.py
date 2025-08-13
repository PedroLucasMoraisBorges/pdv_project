from django.db import models
from auth_user.models import User, Address, Role
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
    colaborators = models.IntegerField(default=0)
    dt_creation = models.DateField(auto_now_add=True, null=True)
    
    fkUser = models.ForeignKey(User, related_name='user_company', on_delete=models.CASCADE)

class CompanyUser(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    company = models.ForeignKey(Company, related_name='employees', on_delete=models.CASCADE)
    user = models.ForeignKey(User, related_name='companies', on_delete=models.CASCADE)
    is_active = models.BooleanField(default=True)
    joined_at = models.DateField(auto_now_add=True)

    class Meta:
        unique_together = ('company', 'user')

class UserRoles(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    fkUser = models.ForeignKey(User, related_name='user_role', on_delete=models.CASCADE)
    fkRole = models.ForeignKey(Role, related_name='type_role', on_delete=models.CASCADE)
    fkCompany = models.ForeignKey(Company, related_name='company_role', on_delete=models.CASCADE)

class Permission(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=84)

class UserPermissions(models.Model):
    fkUser = models.ForeignKey(User, related_name='user_atrib_perm', on_delete=models.CASCADE)
    fkRole = models.ForeignKey(Role, related_name='role_atrib_perm', on_delete=models.CASCADE)
    fkCompany = models.ForeignKey(Company, related_name='company_atrib_perm', on_delete=models.CASCADE)