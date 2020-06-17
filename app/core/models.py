from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from app.constants import EMAIL_IS_REQUIRED


class UserManager(BaseUserManager):
    def create_user(self, email, name, password=None):
        if not email:
            raise ValueError(EMAIL_IS_REQUIRED)
        email = self.normalize_email(email)
        user = self.model(email=email, name=name, password=password)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, name, password):
        user = self.create_user(email=email, password=password, name=name)
        user.is_staff = True
        user.is_superuser = True
        return user


class UserModel(AbstractBaseUser, PermissionsMixin):
    name = models.CharField(max_length=255)
    email = models.CharField(max_length=255, unique=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    objects = UserManager()
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ['name']
