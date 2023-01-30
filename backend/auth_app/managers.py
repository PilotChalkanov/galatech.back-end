from django.contrib.auth import base_user as auth_base
from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.hashers import make_password


class GalaTechUserManager(BaseUserManager):
    def _create_user(self, email, password, **extra_fields):
        """
        Create and save a user with the given  email, and password.
        """
        if not email:
            raise ValueError("Email is mandatory")
        email = self.normalize_email(email)
        # Lookup the real model class from the global app registry so this
        # manager method can be used in migrations. This is fine because
        # managers are by definition working on the real model.
        user = self.model(email=email, **extra_fields)
        user.password = make_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email, staff_id=None, password=None, **extra_fields):
        if staff_id is not None:
            extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_staff", False)
        extra_fields.setdefault("is_superuser", False)
        if not email:
            raise ValueError("Email is mandatory")
        return self._create_user(email, password, **extra_fields)

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)

        if extra_fields.get("is_staff") is not True:
            raise ValueError("Superuser must have is_staff=True.")
        if extra_fields.get("is_superuser") is not True:
            raise ValueError("Superuser must have is_superuser=True.")

        return self._create_user(email, password, **extra_fields)


class GalaTechProfileManager(BaseUserManager):
    pass
