from django.forms import ModelForm
from .models import Profile, Social, Stack

class ProfileForm(ModelForm):
    class Meta:
        model = Profile
        exclude = ['user']

    def __init__(self, *args, **kwargs):
        super(ProfileForm, self).__init__(*args, **kwargs)

        for name, field in self.fields.items():
            field.widget.attrs.update({'class': 'form-control bg-light text-dark', 'placeholder': name.replace('_', ' ').title()})


class SocialForm(ModelForm):
    class Meta:
        model = Social
        exclude = ['profile']

    def __init__(self, *args, **kwargs):
        super(SocialForm, self).__init__(*args, **kwargs)

        for name, field in self.fields.items():
            field.widget.attrs.update({'class': 'form-control bg-light text-dark', 'placeholder': name.replace('_', ' ').title()})

