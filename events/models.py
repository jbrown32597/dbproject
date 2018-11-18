from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class University(models.Model):
    name = models.CharField(max_length=20)
    location = models.CharField(max_length=100)
    desc = models.TextField()
    num_students = models.IntegerField()

class User(AbstractUser):
    university = models.ForeignKey(University, on_delete=models.CASCADE, default='', null=True)
    rsos = models.ManyToManyField('RSO')
    name = models.CharField(max_length=20)
    email = models.EmailField()
    is_student = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    is_superadmin = models.BooleanField(default=False)

class RSO(models.Model):
    name = models.CharField(max_length=20)
    num_students = models.IntegerField()
    university = models.ForeignKey(University, on_delete=models.CASCADE, default='')
    admin = models.ForeignKey(User, on_delete=models.CASCADE)

class Event(models.Model):
    CATEGORIES = (
        ('Social', 'Social'),
        ('Educational', 'Educational'),
        ('Food', 'Food'),
        ('Fun', 'Fun'),
    )
    
    host = models.ForeignKey(User, on_delete=models.CASCADE, related_name='host')
    time = models.DateTimeField()
    location = models.CharField(max_length=100)
    name = models.CharField(max_length=20)
    category = models.CharField(max_length=15, choices=CATEGORIES)
    desc = models.TextField()
    contact_phone = models.CharField(max_length=20)
    contact_email = models.EmailField()
    commenters = models.ManyToManyField(User, through='Comment')
    host_rso = models.ForeignKey(RSO, on_delete=models.CASCADE, default='')
    is_rso = models.BooleanField(default=False)
    is_private = models.BooleanField(default=False)
    is_public = models.BooleanField(default=True)

    class Meta:
        unique_together = ('time', 'location')

class Comment(models.Model):
    RATINGS = (
        (1, 1),
        (2, 2),
        (3, 3),
        (4, 4),
        (5, 5),
    )
    
    text = models.TextField()
    time = models.DateTimeField()
    rating = models.IntegerField(choices=RATINGS)

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    event = models.ForeignKey(Event, on_delete=models.CASCADE)