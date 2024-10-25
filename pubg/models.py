from django.db import models
class pubg(models.Model):
    school_name=models.CharField(max_length=50,null=True)
    school_place=models.CharField(max_length=50,null=True)
    about_school=models.CharField(max_length=50,null=True)

# Create your models here.
