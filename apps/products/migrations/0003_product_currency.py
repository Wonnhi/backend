# Generated by Django 5.0.2 on 2024-03-04 10:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_alter_product_options'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='currency',
            field=models.CharField(choices=[('C', 'Som'), ('$', 'Dollar')], default='$', max_length=100, verbose_name='Currency'),
        ),
    ]
