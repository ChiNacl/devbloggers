from django.db import models
from users.models import Profile
import uuid

# Create your models here.
class Activity(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    activity_post = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)

    def __str__(self):
        return self.profile.user.username
    
    class Meta:
        ordering = ['-created']
