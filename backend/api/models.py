from django.core.validators import MinLengthValidator, MinValueValidator
from django.db import models

from backend.api.common.validators import MaxFileSizeValidator


class ProductCategory(models.Model):

    CATEGORY_NAME_MAX_LEN = 50
    CATEGORY_MIN_LEN = 5
    SHORT_DESC_MAX_LEN = 100

    name = models.CharField(
        default='unknown',
        null=False,
        blank=False,
        max_length=CATEGORY_NAME_MAX_LEN,
        validators=(MinLengthValidator(CATEGORY_MIN_LEN),),
    )
    description = models.TextField(
        max_length=SHORT_DESC_MAX_LEN, validators=(MinLengthValidator(CATEGORY_MIN_LEN),)
    )

class Product(models.Model):
    """The main product model for the online shop"""

    PRODUCT_NAME_MAX_LEN = 50
    PRODUCT_MIN_LEN = 5
    SHORT_DESC_MAX_LEN = 255

    createdTimestamp = models.DateTimeField(auto_now_add=True)
    updatedTimestamp = models.DateTimeField(auto_now_add=True)

    name = models.CharField(
        default='unknown',
        null=False,
        blank=False,
        max_length=PRODUCT_NAME_MAX_LEN,
        validators=(MinLengthValidator(PRODUCT_MIN_LEN),),
    )
    brand = models.CharField(default='unknown',
                             null=False,
                             blank=False,
                             max_length=PRODUCT_NAME_MAX_LEN,
                             validators=(MinLengthValidator(PRODUCT_MIN_LEN),),
                             )

    price = models.FloatField(default=0.00,
                              null=False,
                              blank=False,
                              validators=(MinValueValidator(0.01),),
                              )

    product_SSN = models.CharField(max_length=100)

    category = models.ForeignKey(ProductCategory,
                                 on_delete=models.CASCADE,
                                 )

    description = models.TextField(
        max_length=SHORT_DESC_MAX_LEN, validators=(MinLengthValidator(PRODUCT_MIN_LEN),)
    )

    image = models.ImageField(
        upload_to="products",
        validators=(MaxFileSizeValidator(5),)
    )

    rating = models.FloatField(default=0.1,
                               blank=False,
                               null=False,
                               validators=(MinValueValidator(0.0),)
                               )

    countInStock = models.IntegerField(default=0,
                                       blank=False,
                                       null=False,
                                       validators=(MinValueValidator(0),),
                                       )

    numReviews = models.IntegerField(default=0,
                                     blank=False,
                                     null=False,
                                     validators=(MinValueValidator(0),)
                                     )
