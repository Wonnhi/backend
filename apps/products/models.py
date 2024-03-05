from django.db import models

from apps.categories.models import Category


class Product(models.Model):
    class Currency(models.TextChoices):
        som="C"
        dollar="$"
    title = models.CharField(
        max_length=255,
        verbose_name='Title'
    )
    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE,
        verbose_name='Category'
    )
    price= models.PositiveSmallIntegerField(
        verbose_name='Price' 
    )
    currency = models.CharField(
        max_length=100,
        choices=Currency.choices,
        default=Currency.dollar,
        verbose_name='Currency'
    )
    description = models.TextField(
        max_length=255,
        verbose_name='Description'
    )
    color = models.CharField(
        max_length=255,
        verbose_name='Color'
    )
    photo = models.ImageField(
        verbose_name='Photo'
    )


    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'

    def __str__(self):
        return self.title 
    
 
