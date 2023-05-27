from django.db import models
from django.contrib.auth.models import AbstractBaseUser,BaseUserManager 


# Create your models here.

class AccountManager(BaseUserManager):
    def create_user(self,email,username,first_name,last_name,password=None):
        if not email:
            raise ValueError('Users must have an email address')
        if not username:
            raise ValueError('Users must have a username')
        user = self.model(
            email=self.normalize_email(email),
            username=username,
            first_name=first_name,
            last_name=last_name,
        )
        user.set_password(password)
        user.save(using=self._db)
        return user
    # create account for admin 
    def create_superuser(self,email,username,first_name,last_name,password):
        user = self.create_user(
            email=self.normalize_email(email),
            username=username,
            first_name=first_name,
            last_name=last_name,
            password=password,
        )
        user.is_staff = True
        user.is_admin = True
        user.is_active = True
        user.is_superuser = True
        user.save(using=self._db)
        return user

class Account(AbstractBaseUser):
    first_name = models.CharField(max_length=40)
    last_name = models.CharField(max_length=40)
    username = models.CharField(max_length=20,unique=True   )
    email = models.EmailField(unique=True) 
    phone_number = models.CharField(max_length=15)

    #required 
    date_joined = models.DateTimeField(auto_now_add=True)
    last_login = models.DateTimeField(auto_now=True)
    is_admin = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=False) 
    is_superuser = models.BooleanField(default =False) 
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name','last_name','username']

    def __str__(self):
        return self.email 
    #permission
    def has_perm(self, perm,obj=None):
        return self.is_admin 
    def has_module_perms(self, app_label):
        return True

    objects = AccountManager()