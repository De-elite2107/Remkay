from  django.contrib  import  admin
from .models  import  *

class  PaymentAdmin(admin.ModelAdmin):
    list_display  = ["id", "ref", 'amount', "verified", "date_created"]

admin.site.register(Payment, PaymentAdmin)
admin.site.register(UserWallet)