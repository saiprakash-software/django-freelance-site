from django.db import models
from django.contrib.auth.models import User


class JobPosting(models.Model):
    title = models.CharField(max_length=255)
    company = models.CharField(max_length=255)
    description = models.TextField()
    location = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


  

class Job(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    location = models.CharField(max_length=100)
    salary = models.CharField(max_length=100)
    posted_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


# jobs/models.py

from django.db import models
from django.contrib.auth.models import User
from .models import Job

class JobApplication(models.Model):
    job = models.ForeignKey(Job, on_delete=models.CASCADE)
    applicant = models.ForeignKey(User, on_delete=models.CASCADE)
    cover_letter = models.TextField()  # Ensure this field exists
    applied_at = models.DateTimeField(auto_now_add=True)
    
    
    def __str__(self):
        return f"{self.applicant} applied for {self.job.title}"
