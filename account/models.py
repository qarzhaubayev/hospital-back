from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin

# Create your models here.
class UserCreate(BaseUserManager):
    use_in_migrations = True
    def _create_user(self, iin_num, password, is_superuser, is_staff, **extra_fields):
        if not iin_num:
            raise ValueError('The given iin must be set')
        user = self.model(iin_num=iin_num, is_superuser=is_superuser, is_staff=is_staff, is_active=True, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, iin_num, password=None, **extra_fields):
        return self._create_user(iin_num, password, False, False, **extra_fields)

    def create_superuser(self, iin_num, password, **extra_fields):
        return self._create_user(iin_num, password, True, True, **extra_fields)


class User(AbstractBaseUser, PermissionsMixin):
    # any fields you would like to add
    join_date = models.DateTimeField(auto_now_add=True)
    last_login_date  = models.DateTimeField(null=True)
    is_staff    = models.BooleanField(default=False)
    is_active   = models.BooleanField(default=True)
    iin_num         = models.CharField(max_length=12, primary_key=True)

    USERNAME_FIELD = 'iin_num'
    REQUIRED_FIELDS = []

    objects = UserCreate()
