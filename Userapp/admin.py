from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(UserFeedback)
admin.site.register(UserPaymentConfirmUpload)
admin.site.register(Blog)