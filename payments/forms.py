from django import forms
from .models import *

class UserWalletForm(forms.ModelForm):
	class Meta:
		model = UserWallet
		fields = "__all__"


class PaymentForm(forms.ModelForm):
	class Meta:
		model = Payment
		fields = "__all__"