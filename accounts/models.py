from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser


class UserManager(BaseUserManager):
    def create_user(self, email, password=None, active=True,
                    is_researcher=False, is_student=False, is_admin=False,
                    confirmed=True):
        if not email:
            raise ValueError("User must have an email address")
        if not password:
            raise ValueError("User must have a password")

        user = self.model(email=self.normalize_email(email))
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password):
        user = self.create_user(
            email,
            password=password,
            is_admin=True,
            is_researcher=True,
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
    active = models.BooleanField(default=False)
    is_researcher = models.BooleanField(default=False)
    is_student = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)
    confirmed = models.BooleanField(default=False)
    confirmed_date = models.DateTimeField(auto_now=True)
    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.first_name + " " + self.last_name

    def get_absolute_url(self):
        return reverse('users:detail', kwargs={'username': self.username})
