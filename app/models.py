
# Create your models here.
from django.db import models


class Role(models.Model):
    name = models.CharField(max_length=50, unique=True)


class User(models.Model):
    username = models.CharField(max_length=100, unique=True)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=255)
    roles = models.ManyToManyField(Role, through="UserRole")


class UserRole(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    role = models.ForeignKey(Role, on_delete=models.CASCADE)
    assigned_at = models.DateTimeField(auto_now_add=True)


class Customer(models.Model):
    name = models.CharField(max_length=150)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=15, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)


class Lead(models.Model):
    STATUS_CHOICES = [
        ("NEW", "New"),
        ("IN_PROGRESS", "In Progress"),
        ("WON", "Won"),
        ("LOST", "Lost"),
    ]
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    description = models.TextField()
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default="NEW")
    created_at = models.DateTimeField(auto_now_add=True)


class Interaction(models.Model):
    INTERACTION_TYPES = [
        ("CALL", "Call"),
        ("EMAIL", "Email"),
        ("MEETING", "Meeting"),
    ]
    lead = models.ForeignKey(Lead, on_delete=models.CASCADE)
    interaction_type = models.CharField(max_length=20, choices=INTERACTION_TYPES)
    notes = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)
