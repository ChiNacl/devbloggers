from django.contrib import admin
from .models import Profile, Stack, Social

# Register your models here.
admin.site.register(Profile)
admin.site.register(Stack)
admin.site.register(Social)