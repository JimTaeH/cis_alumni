from __future__ import unicode_literals
from django.db import models
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import post_save
from django.urls import reverse
from datetime import date

# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    role = models.CharField(max_length=15, default="#")

    @receiver(post_save, sender=User)
    def create_user_profile(sender, instance, created, **kwargs):
        if created:
            Profile.objects.create(user=instance)
    
    @receiver(post_save, sender=User)
    def save_user_profile(sender, instance, **kwargs):
        instance.profile.save()

    def __str__(self):
        return str(self.user)

class academicadmin(models.Model):
    gender_choices = [
        ("m", "male"),
        ("f", "female"),
        ("o", "lgbtqia2s+")
    ]

    academicadminID = models.CharField(max_length=10, default="#", null=False)
    academicadminName = models.OneToOneField(Profile, on_delete=models.CASCADE)
    phone = models.CharField(max_length=10, default="0123456789")
    dob = models.DateField(max_length=10, default=date.today)
    gender = models.CharField(max_length=10, choices=gender_choices, default="#")
    details = models.CharField(max_length=80, default="#")

    def __str__(self):
        return str(self.academicadminName.user.first_name) + "," + str(self.academicadminName.user.last_name) + "," + str(self.academicadminName.role)

class assistantDean(models.Model):
    gender_choices = [
        ("m", "male"),
        ("f", "female"),
        ("o", "lgbtqia2s+")
    ]

    assistantDeanID = models.CharField(max_length=10, default="#", null=False)
    assistantDeanName = models.OneToOneField(Profile, on_delete=models.CASCADE)
    phone = models.CharField(max_length=10, default="0123456789")

    def __str__(self):
        return str(self.assistantDeanName.user.first_name) + "," + str(self.assistantDeanName.user.last_name) + "," + str(self.assistantDeanName.role)

class fieldstudy(models.Model):
    alumniuser = models.OneToOneField(Profile, on_delete=models.CASCADE)
    studyFieldID = models.CharField(max_length=2, default="#", null=False)
    studyField = models.CharField(max_length=50, default="#")
    studyMajor = models.CharField(max_length=30, default="#")
    studyMinor = models.CharField(max_length=30, default="#")
    yearStart = models.IntegerField(default=2543)
    yearGraduate = models.IntegerField(default=2547)
    gpa = models.FloatField(max_length=4, default=3.50)
    

class job(models.Model):
    alumniuser = models.OneToOneField(Profile, on_delete=models.CASCADE)
    organization = models.CharField(max_length=30, default="#")
    organizeType = models.CharField(max_length=10, default="#")
    department = models.CharField(max_length=20, default="#")
    jobTitle = models.CharField(max_length=30, default="#")
    jobDesc = models.TextField(max_length=255, default="#")

    def __str__(self):
        return str(self.organization) + "," + str(self.department) + "," + str(self.jobTitle)

class education(models.Model):
    alumniuser = models.OneToOneField(Profile, on_delete=models.CASCADE)
    universityID = models.CharField(max_length=10, default="#", null=False)
    degree = models.CharField(max_length=10, default="#")
    university = models.CharField(max_length=50, default="#")
    faculty = models.CharField(max_length=50, default="#")
    major = models.CharField(max_length=50, default="#")
    country = models.CharField(max_length=20, default="#")

    def __str__(self):
        return str(self.degree) + "," + str(self.university) + "," + str(self.faculty)

class success(models.Model):
    alumniuser = models.OneToOneField(Profile, on_delete=models.CASCADE)
    achieveTitle = models.CharField(max_length=50, default="#")
    desc = models.TextField(max_length=2000, default="#")
    achieveDate = models.DateField(max_length=10, default=date.today)

    def __str__(self):
        return str(self.achieveTitle)

class alumnidata(models.Model):
    gender_choices = [
        ("m", "male"),
        ("f", "female"),
        ("o", "lgbtqia2s+")
    ]

    alumniuser = models.OneToOneField(Profile, on_delete=models.CASCADE)
    alumniID = models.CharField(max_length=10, default="#", null=False)
    phone = models.CharField(max_length=10, default="0123456789")
    dob = models.DateField(max_length=10, default=date.today)
    gender = models.CharField(max_length=10, choices=gender_choices, default="#")
    address = models.TextField(max_length=2500, default="#")
    
    @receiver(post_save, sender=Profile)
    def save_alumni_profile(sender, instance, **kwargs):
        if alumnidata.objects.filter(alumniuser=instance).count() != 0:
            print(alumnidata.objects.get(alumniuser=instance))

        elif instance.role != 'alumni':
            print("Not alumni account")
            
        elif alumnidata.objects.filter(alumniuser=instance).count() == 0 and instance.role == 'alumni':
            alumnidata.objects.create(alumniuser=instance)

    def __str__(self):
        return str(self.alumniuser.user.first_name) + "," + str(self.alumniuser.user.last_name) + "," + str(self.alumniuser.role)