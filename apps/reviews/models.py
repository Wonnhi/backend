from django.db import models

class Reviews(models.Model):
    title = models.CharField(
        max_length=255,
        verbose_name = 'Title'
    )
    image = models.ImageField(
        upload_to="reviews_image",
        verbose_name="Photo"
    )
    description = models.TextField(
        max_length=255,
        verbose_name = 'Description'
    )
    created_at = models.DateTimeField(
        auto_created = True,
        verbose_name = 'Created at'
    )

class Meta(models.Model):
    verbose_name = 'Review'
    verbose_name_plural = 'Reviews'

def __str__(self):
    return self.title    