import uuid
from django.db import models

# Create your models here.
class Product(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=255)
    price = models.IntegerField()
    description = models.TextField()
    # skin_type = models.CharField(max_length=50)
    # stock = models.IntegerField()
    # rating = models.DecimalField(max_digits=3, decimal_places=2)
    # user = models.ForeignKey(User, on_delete=models.CASCADE)  # Relasi ke User
