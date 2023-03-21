from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

# Create your models here.
class UserFeedback(models.Model):
    Names = models.CharField("Enter your name", max_length = 100)
    Email = models.EmailField("Enter your email", max_length = 100)
    Phone = models.PositiveIntegerField("Enter your phone number", max_length = 12)
    Message = models.TextField("Leave a message", max_length = 300)
    def __str__(self):
        return self.Names

class UserPaymentConfirmUpload(models.Model):
    CLASS = (('Prep', 'Preparatory'), ('KG', 'Kindergaten'), ('Nur_1', 'Nursery 1'), ('Nur_2', 'Nursery 2'), ('B_1', 'Basic 1'), ('B_2', 'Basic 2'), ('B_3', 'Basic 3'), ('B_4', 'Basic 4'), ('B_5', 'Basic 5'), ('Jss_1', 'JSS 1'), ('Jss_2', 'JSS 2'), ('Jss_3', 'JSS 3'), ('Sss_1', 'SSS 1'))
    PAY_METH = (('Ussd', 'USSD'), ('Deposit', 'Deposit'), ('Pos_Trf', 'POS TRANSFER'))

    USERNAME = models.CharField("Username", max_length = 100)
    CLASS = models.CharField("Class", choices = CLASS, max_length = 50)
    AMOUNTPAID = models.PositiveIntegerField("Amount Paid", max_length = 50)
    BALANCE = models.IntegerField("Balance", max_length = 50)
    METHODOFPAYMENT = models.CharField("Payment Method", choices = PAY_METH, max_length = 50)
    PAYMENTUPLOAD = models.ImageField("Image Confirmation", upload_to = 'uploads')
    def __str__(self):
        return self.USERNAME

class Blog(models.Model):
    HEADER = models.CharField("Post heading", max_length = 100)
    TITLE = models.CharField("Post title", max_length = 100)
    CONTENT = models.TextField("Post content", max_length = 500)
    IMAGE = models.ImageField("Post Image", upload_to = 'uploads')
    def __str__(self):
        return self.HEADER