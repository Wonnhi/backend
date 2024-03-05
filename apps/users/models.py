from django.db import models

class User(models.Model):
    first_name = models.CharField(
        max_length=255,
       blank=True,
    )
    work_email = models.EmailField(
        max_length=255,
        blank=True, null=True,
    )
    phone_number = models.CharField(
        max_length=255,
        blank=True, null=True,
    )
    password = models.CharField(
        max_length=255,
        blank=True, null=True,
    )
    address = models.CharField(
        max_length=255,
        blank=True, null=True,
    )
    city = models.CharField(
        max_length=255,
        blank=True, null=True,
    )
    country = models.CharField(
        max_length=255,
        blank=True, null=True,
    )
    zip_code = models.CharField(
        max_length=255,
        blank=True, null=True,
    )



   
