# from django.db import models
# import uuid

# import sys
# sys.path.append("..")

# from accounts.models import Profile

# class Product(models.Model):
#     """ Model representing a product. """
    
#     id = models.UUIDField(primary_key=True, default = uuid.uuid4)
#     name = models.CharField(max_length=100)
#     description = models.TextField(max_length=500)
#     created_by = models.ForeignKey(Profile, on_delete=models.CASCADE)
#     created_at = models.DateTimeField(auto_now_add=True)
#     last_modified = models.DateTimeField(auto_now=True)
    
#     AVAILABILITY = [
#         ('PR', 'Preorder'),
#         ('MA', 'Maintenance'),
#         ('SO', 'Sold Out'),
#         ('RS', 'Releasing Soon'),
#         ('AN', 'Available Now'),
#     ]
    
#     status = models.CharField(max_length=2, choices=AVAILABILITY, default='MA')
    
#     class Meta:
#         ordering = ['-last_modified']
    
#     def __str__(self):
#         return self.name