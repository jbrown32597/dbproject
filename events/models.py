from django.db import models
from django.contrib.auth.models import AbstractUser
from django.urls import reverse, reverse_lazy

# Create your models here.
class University(models.Model):
    name = models.CharField(max_length=20, unique=True)
    location = models.CharField(max_length=100)
    desc = models.TextField()
    num_students = models.IntegerField()

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('events:universities')

class User(AbstractUser):
    PERM_LEVELS = (
        ('Student', 'Student'),
        ('Admin', 'Admin'),
        ('Superadmin', 'Superadmin'),
    )
    
    university = models.ForeignKey(University, on_delete=models.CASCADE, default='', null=True, blank=True)
    rsos = models.ManyToManyField('RSO', blank=True)
    name = models.CharField(max_length=20)
    email = models.EmailField()
    perm_level = models.CharField(max_length=10, choices=PERM_LEVELS, null=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('events:viewUser', kwargs={'pk': self.pk})

class RSO(models.Model):
    name = models.CharField(max_length=20, unique=True)
    num_students = models.IntegerField()
    university = models.ForeignKey(University, on_delete=models.CASCADE, default='')
    admin = models.ForeignKey(User, on_delete=models.CASCADE)
    is_active = models.BooleanField(default=False)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('events:viewRSO', kwargs={'pk': self.pk})

class Event(models.Model):
    CATEGORIES = (
        ('Social', 'Social'),
        ('Educational', 'Educational'),
        ('Food', 'Food'),
        ('Fun', 'Fun'),
    )

    EVENT_TYPES = (
        ('RSO', 'RSO'),
        ('Private', 'Private'),
        ('Public', 'Public'),
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
    host_rso = models.ForeignKey(RSO, on_delete=models.CASCADE, default='', blank=True, null=True)
    event_type = models.CharField(max_length=7, choices=EVENT_TYPES, null=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('events:viewEvent', kwargs={'pk': self.pk})

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
    rating = models.IntegerField(choices=RATINGS)

    created_by = models.ForeignKey(User, on_delete=models.CASCADE, editable=False)
    event = models.ForeignKey(Event, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.text

    def get_absolute_url(self):
        return reverse('events:home')