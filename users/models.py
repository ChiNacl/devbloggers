from django.db import models
from django.contrib.auth.models import User
import uuid

# Create your models here.
class Profile(models.Model):
    GENDER_CHOICES = ( 
        ('M', 'Male'), 
        ('F', 'Female') 
    )

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    dev_name = models.CharField(max_length=100, null=True, blank=True)
    profile_image = models.ImageField(upload_to='profiles/', null=True, blank=True, default='profiles/default.png')
    email = models.EmailField(max_length=200)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    bio = models.TextField(null=True, blank=True)
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    location = models.CharField(max_length=300, null=True, blank=True)
    occupation = models.CharField(max_length=300, null=True, blank=True)
    stack = models.ManyToManyField('Stack', blank=True)
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)

    def __str__(self):
        return self.user.username
    
    @property
    def official_name(self):
        return f"{self.first_name} {self.last_name}"


class Stack(models.Model):
    name = models.CharField(max_length=200)
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)

    def __str__(self):
        return self.name


class Social(models.Model):
    github_url = models.URLField(max_length=500, blank=True, null=True)
    x_url = models.URLField(max_length=500, blank=True, null=True)
    facebook_url = models.URLField(max_length=500, blank=True, null=True)
    instagram_url = models.URLField(max_length=500, blank=True, null=True)
    youtube_url = models.URLField(max_length=500, blank=True, null=True)
    linkedin_url = models.URLField(max_length=500, blank=True, null=True)
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)

    def __str__(self):
        return self.profile.official_name
