from django.contrib.auth.models import BaseUserManager
from django.utils.translation import ugettext_lazy as _

class CustomUserManager(BaseUserManager): #import to models.py
    def create_user(self, email, password, **kwargs):
        """
        Creates and saves a User with the given email, date of
        birth and password.
        """
        if not email:
            raise ValueError(_('Users must have an email address'))

        user = self.model(
            email=self.normalize_email(email),
            **kwargs
        )

        user.set_password(password)
        user.save(using=self._db)
        return user
    
    def create_staffuser(self, email, password, **kwargs):
        """
        Creates and saves a staff user with the given email and password.
        """
        if not email:
            raise ValueError(_('Users must have an email address'))
        
        user = self.create_user(
            email,
            password=password,
            **kwargs
        )
        user.is_staff = True
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password, **kwargs):
        """
        Creates and saves a superuser with the given email, date of
        birth and password.
        """
        if not email:
            raise ValueError(_('Users must have an email address'))
        
        user = self.create_user(
            email,
            password=password,
            **kwargs
        )
        user.is_admin = True
        user.is_staff = True
        user.save(using=self._db)
        return user