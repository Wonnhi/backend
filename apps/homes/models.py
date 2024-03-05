from django.db import models


class Cosmetics(models.Model):
    title = models.CharField(
        max_length=255,
        verbose_name = 'About Us'
    )
    description = models.TextField(
        max_length=255,
        verbose_name = 'Description'  
    )
    photo = models.ImageField(
        verbose_name='Photo'
    )
    price = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        verbose_name='Price'
    )

    def str(self):
        return self.title
    
    class Meta:
        verbose_name = 'Services'
        verbose_name_plural = 'Services"'