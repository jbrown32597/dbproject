from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class University(models.Model):
    name = models.CharField(max_length=20)
    location = models.CharField(max_length=100)
    desc = models.TextField()
    num_students = models.IntegerField()

class User(AbstractUser):
    university = models.ForeignKey(University, on_delete=models.CASCADE, default='')

class Admin(User):
    pass

class SuperAdmin(User):
    pass

class RSO(models.Model):
    name = models.CharField(max_length=20)
    num_students = models.IntegerField()
    university = models.ForeignKey(University, on_delete=models.CASCADE, default='')
    admin = models.ForeignKey(Admin, on_delete=models.CASCADE)

class Student(User):
    rsos = models.ManyToManyField(RSO)

class Event(models.Model):
    CATEGORIES = (
        ('Social', 'Social'),
        ('Educational', 'Educational'),
        ('Food', 'Food'),
        ('Fun', 'Fun'),
    )
    
    host = models.ForeignKey(Admin, on_delete=models.CASCADE, related_name='host')
    time = models.DateTimeField(unique=True)
    location = models.CharField(max_length=100, unique=True)
    name = models.CharField(max_length=20)
    category = models.CharField(max_length=15, choices=CATEGORIES)
    desc = models.TextField()
    contact_phone = models.CharField(max_length=20)
    contact_email = models.EmailField()
    commenters = models.ManyToManyField(User, through='Comment')

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

class RSOEvent(Event):
    belongs_to = models.ForeignKey(RSO, on_delete=models.CASCADE)

class PrivateEvent(Event):
    pass

class PublicEvent(Event):
    pass
