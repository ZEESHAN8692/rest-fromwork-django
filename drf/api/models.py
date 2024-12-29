from django.db import models

# Create your models here.

class ContactForm(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    phone = models.IntegerField(max_length=30)
    father = models.CharField(max_length=100)
    school = models.CharField(max_length=200)
    aducation = models.CharField(max_length=100, choices=(
        ('7th ','7th'),
        ('8th ','8th'),
        ('9th ','9th'),
        ('10th ','10th'),
        ('11th ','11th'),
        ('12th ','12th'),
    )
    )
    message =models.TextField()
