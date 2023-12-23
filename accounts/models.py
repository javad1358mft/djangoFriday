from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class UserProfile(models.Model):
    bio= models.CharField(max_length=150)
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    picture= models.ImageField(upload_to= 'profile_picture')
    
    
class AddEducation(models.Model):
    school= models.CharField(max_length=50)
    degree= models.CharField(max_length=50)
    field_of_study= models.CharField(max_length=50)
    start_date=models.DateField()
    end_date= models.DateField()
    current_school= models.BooleanField(default=False)
    description= models.TextField()
    
class AddExperience(models.Model):
    job_title= models.CharField(max_length=50)
    company= models.CharField(max_length=50)
    location= models.CharField(max_length=50)
    start_date=models.DateField()
    end_date= models.DateField()
    current_job= models.BooleanField(default=False)
    description= models.TextField()  