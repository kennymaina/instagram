from django import forms
from .models import Image, Profile
from django.contrib.auth.models import User

class UploadForm(forms.ModelForm):
    class Meta:
        model = Image
        fields = ('pic', 'description')


class ProfileEditForm(forms.ModelForm):

   class Meta:
      model = Profile
      fields = ['pic','bio']
      widgets = {
         'bio': forms.Textarea(attrs={'placeholder': 'Enter the bio..'})
      }


class UserEditForm(forms.ModelForm):
   first_name = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'First Name'}))
   last_name = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Last Name'}))
   class Meta:
      model = User
      fields = ['first_name','last_name']