from django.db import models

# Create your models here.
class Reviews(models.Model):
    PostedName = models.CharField(max_length=30)
    PostedMobile = models.CharField(max_length=15)
    PostedReview = models.CharField(max_length=400)