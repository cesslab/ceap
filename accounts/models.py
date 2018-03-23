from django.db import models
from django.contrib.auth.models import (
    BaseUserManager, AbstractBaseUser, PermissionsMixin)


class UserManager(BaseUserManager):
    def create_user(self, email, first_name, last_name, password=None, is_active=True,
                    is_researcher=False, is_student=False, is_admin=False,
                    is_confirmed=True):
        if not email:
            raise ValueError("User must have an email address")
        if not password:
            raise ValueError("User must have a password")
        if not first_name:
            raise ValueError("User must have a first_name")
        if not last_name:
            raise ValueError("User must have a last_name")

        user = self.model(
            email=self.normalize_email(email), first_name=first_name,
            last_name=last_name)
        user.set_password(password)
        user.is_active = is_active
        user.is_researcher = is_researcher
        user.is_student = is_student
        user.is_admin = is_admin
        user.is_confirmed = is_confirmed
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password, first_name, last_name):
        user = self.create_user(
            email,
            password=password,
            is_admin=True,
            is_researcher=True,
            first_name=first_name,
            last_name=last_name
        )

        user.save(using=self._db)
        return user

    def create_admin(self, email, password=None):
        self.create_user(email, password, is_admin=True)

    def create_researcher(self, email, password=None):
        self.create_user(email, password, is_researcher=True)

    def create_student(self, email, password=None):
        self.create_user(email, password, is_student=True)


class User(AbstractBaseUser):
    # First Name and Last Name do not cover name patterns
    # around the globe.
    email = models.EmailField(max_length=255, unique=True)
    first_name = models.CharField(max_length=255, blank=False, null=False)
    last_name = models.CharField(max_length=255, blank=False, null=False)
    is_active = models.BooleanField(default=False)
    is_researcher = models.BooleanField(default=False)
    is_student = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)
    is_confirmed = models.BooleanField(default=False)
    confirmed_date = models.DateTimeField(auto_now=True)
    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name']

    def __str__(self):
        return self.email

    # def get_absolute_url(self):
    #     return reverse('users:detail', kwargs={'username': self.username})

    def get_full_name(self):
        return self.first_name + " " + self.last_name

    def get_short_name(self):
        return self.email

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True

    @property
    def is_staff(self):
        return self.is_admin
