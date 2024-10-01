# Generated by Django 5.1.1 on 2024-10-01 15:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_alter_product_price'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='product_images/'),
        ),
        migrations.AddField(
            model_name='product',
            name='skin_type',
            field=models.CharField(default=1, max_length=50),
            preserve_default=False,
        ),
    ]
