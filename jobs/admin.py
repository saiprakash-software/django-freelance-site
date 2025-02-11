

# Register your models here.
from django.contrib import admin
from .models import Job,JobPosting, JobApplication

admin.site.register(JobPosting)
admin.site.register(JobApplication)
admin.site.register(Job)






