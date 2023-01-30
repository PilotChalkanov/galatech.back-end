from django.db import models

from django.contrib.auth import models as auth_models, password_validation
from django.core.validators import MinLengthValidator, MinValueValidator, MaxValueValidator
from django.db import models

from backend.api.common.validators import MaxFileSizeValidator
from backend.auth_app.managers import GalaTechUserManager, GalaTechProfileManager


class GalaTechUser(auth_models.AbstractBaseUser, auth_models.PermissionsMixin):
    """Main Galatech user model for authorization and authentication process"""

    USERNAME_MAX_LEN = 50
    USERNAME_MIN_LEN = 5
    email = models.EmailField(unique=True, null=False, blank=False)

    staff_id = models.IntegerField(
        null=True,
        blank=True,
    )

    createdTimestamp = models.DateTimeField(auto_now_add=True)

    updatedTimestamp = models.DateTimeField(auto_now_add=True)

    is_staff = models.BooleanField(
        default=False,
    )

    # use email for username
    USERNAME_FIELD = "email"

    # using GalaTechUserManager for user creation
    objects = GalaTechUserManager()


class GalaTechProfile(models.Model):
    """Main Galatech profile model"""

    first_name = models.CharField(
        max_length=100,
        validators=(MinLengthValidator(3),),
    )
    last_name = models.CharField(
        max_length=100,
        validators=(MinLengthValidator(3),),
    )
    age = models.IntegerField(validators=(MinValueValidator(16),))
    address = models.CharField(
        max_length=1000,
    )

    user = models.OneToOneField(
        GalaTechUser, on_delete=models.CASCADE, primary_key=True
    )

    photo = models.ImageField(
        upload_to="profiles",
        default="profiles/avatar.png",
        validators=(MaxFileSizeValidator(5),),
    )


class GalaTechEmployeeInitAuthCode(models.Model):
    employee_id = models.CharField(max_length=256)

