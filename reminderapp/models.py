from django.db import models

# Create your models here.
class reminder(models.Model):
    rem_choice = [
        ('sms', 'SMS'),
        ('email', 'Email'),
        ('call', 'Call'),
    ]
    rem_type = models.CharField(max_length=10, choices=rem_choice, default='sms')
    message = models.TextField()
    rem_date = models.DateTimeField()


    def __str__(self):
        return f"{self.rem_type} - {self.message} - {self.rem_date}"