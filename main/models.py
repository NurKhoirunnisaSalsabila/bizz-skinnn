import uuid
from django.db import models
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError

class Product(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=255)
    price = models.IntegerField()
    description = models.TextField()
    skin_type = models.CharField(max_length=50)
    # image = models.ImageField(upload_to='product_images/', blank=True, null=True)

    def clean(self):
        if self.price <= 0:
            raise ValidationError('Price must be greater than 0')
        
    def __str__(self):
        return self.name