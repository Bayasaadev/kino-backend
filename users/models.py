from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    # Additional fields
    avatar = models.ImageField(upload_to='avatars/', null=True, blank=True)
    bio = models.TextField(blank=True)
    social = models.URLField(blank=True)
    
    # Role field
    ROLE_CHOICES = (
        ('admin', 'Admin'),
        ('staff', 'Staff'),
        ('user', 'User'),
    )
    role = models.CharField(max_length=10, choices=ROLE_CHOICES, default='user')
    
    def __str__(self):
        return self.username
