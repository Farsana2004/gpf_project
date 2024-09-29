# gpf/models.py

from django.db import models

class GPFForm(models.Model):
    name = models.CharField(max_length=255)
    permanent_address = models.TextField()
    phone_number = models.CharField(max_length=15)
    marital_status = models.CharField(max_length=20)
    subscriber_name = models.CharField(max_length=100, default='Default Name')
    # other fields...
    


class Nominee(models.Model):
    gpf_form = models.ForeignKey(GPFForm, on_delete=models.CASCADE, related_name='nominees')
    name = models.CharField(max_length=255)
    permanent_address = models.TextField()
    aadhar_no = models.CharField(max_length=12)
    relationship = models.CharField(max_length=50)
    age = models.PositiveIntegerField()
    share_percentage = models.DecimalField(max_digits=5, decimal_places=2)

    def __str__(self):
        return self.name
