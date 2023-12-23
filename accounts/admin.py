from django.contrib import admin
from .models import UserProfile,AddEducation,AddExperience


# Register your models here.
admin.site.register(UserProfile)
admin.site.register(AddExperience)
admin.site.register(AddEducation)