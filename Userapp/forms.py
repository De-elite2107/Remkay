from django import forms
from .models import *

class UserfeedbackForm(forms.ModelForm):
	class Meta:
		model = UserFeedback
		fields = "__all__"

class UploadConfirmationForm(forms.ModelForm):
	USERNAME = forms.CharField(label = "", widget = forms.HiddenInput())
	BALANCE = forms.CharField(label = "", widget = forms.HiddenInput())
	class Meta:
		model = UserPaymentConfirmUpload
		fields = "__all__"

class BlogForm(forms.ModelForm):
	class Meta:
		model = Blog
		fields = "__all__"