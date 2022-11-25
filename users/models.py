from django.db import models
from django.contrib.auth.models import (BaseUserManager, AbstractBaseUser)
import store
import ImageStorage
from django.utils import timezone
class UserManager(BaseUserManager):
    def create_user(self, email, username, phone_number, address, password=None):
        if not email:
            raise ValueError('Users must have an email address')

        user = self.model(
            email=self.normalize_email(email),
            username = username,
            phone_number = phone_number,
            address = address
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, username=None, address=None, password=None, phone_number=None):
        user = self.create_user(
            email,
            password=password,
            phone_number=phone_number,
            username=username,
            address=address

        )
        user.is_admin = True
        user.save(using=self._db)
        return user


class User(AbstractBaseUser):
    email = models.EmailField(
        verbose_name='email address',
        max_length=255,
        unique=True,
    )
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    username = models.CharField(max_length=100, null=True)
    phone_number = models.IntegerField(blank=True, null=True)
    address = models.CharField(max_length=100, null=True)
    filter= models.ManyToManyField('store.Filter', related_name="filter_user")

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return True

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True

    @property
    def is_staff(self):
        "Is the user a member of staff?"
        # Simplest possible answer: All admins are staff
        return self.is_admin

class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    filter = models.ForeignKey('store.Filter', on_delete=models.CASCADE)
    filter_option = models.ForeignKey('store.Filter_option', on_delete=models.CASCADE, default=0)
    image = models.ForeignKey('ImageStorage.Image', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now = True)

