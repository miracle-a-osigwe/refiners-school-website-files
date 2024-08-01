import datetime
from django.db import models
from django.utils import timezone
from django.contrib import admin
from django.contrib.auth.models import (
    BaseUserManager, AbstractBaseUser, PermissionsMixin
)

class CustomUserManager(BaseUserManager):
    """
    Manages user creation
    """

    def create_user(self, username, firstname, lastname, gender, role, password=None):
        """
        Creates and saves a User with the provided registration number and password
        """
        if not username:
            raise ValueError("User must have a registration number.")
        
        user = self.model(
            username = username,
            firstName = firstname,
            lastName = lastname
            )
        user.set_password(password)
        user.save(using=self._db)
        return user
    
    def create_superuser(self, **kwargs):
        """
        Create a superuser
        """
        password = kwargs.get('password')
        del kwargs['password']
        user = self.model(**kwargs)
        user.set_password(password)
        user.is_superuser = True
        user.save(using=self._db)
        return user

class User(AbstractBaseUser, PermissionsMixin):
    """
    A user model for the app.
    """
    firstName = models.CharField(
        verbose_name='First name',
        max_length=30,
    )
    lastName = models.CharField(
        verbose_name='Last name',
        max_length=30,
    )
    username = models.CharField(
        verbose_name = 'Registration number',
        max_length=20,
        unique=True,
        )
    gender_choices = [
        ('M', 'Male'),
        ('F', 'Female'),
    ]
    gender = models.CharField(verbose_name='Gender', choices=gender_choices, max_length=10)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=True)  # a staff
    
    user_role = [
        (1, "Student"),
        (2, "Staff"),
        (3, "Admin"),
        (4, "SuperAdmin"),
        (5, "Owner")
    ]

    role = models.IntegerField(verbose_name="User role", choices=user_role)

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['firstName', 'lastName', 'password', 'gender', 'role'] 

    def get_full_name(self):
        # The user is identified by their first and last name.
        name = self.firstName + ' ' + self.lastName
        return name
    
    def get_short_name(self):
        # The user has a surname
        return self.lastName

    def __repr__(self) -> str:
        return f"RHS Staff Number -> {self.username} for {self.firstName}"
    
    def __str__(self) -> str:
        return str(self.username)
    
    @property
    def user_role(self):
        # User role
        return self.role
    
    objects = CustomUserManager()