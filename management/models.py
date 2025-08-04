from django.db import models
from company.models import Company
from auth_user.models import User
import uuid

# Create your models here.
class Role(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=244)

    def __str__(self):
        return self.name
    
class UserRole(models.Model):
    fkUser = models.ForeignKey(User, related_name='user_atrib_role', on_delete=models.CASCADE)
    fkRole = models.ForeignKey(Role, related_name='role_atrib_role', on_delete=models.CASCADE)
    fkCompany = models.ForeignKey(Company, related_name='company_atrib_role', on_delete=models.CASCADE)

class Permission(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=84)

class UserPermissions(models.Model):
    fkUser = models.ForeignKey(User, related_name='user_atrib_perm', on_delete=models.CASCADE)
    fkRole = models.ForeignKey(Role, related_name='role_atrib_perm', on_delete=models.CASCADE)
    fkCompany = models.ForeignKey(Company, related_name='company_atrib_perm', on_delete=models.CASCADE)