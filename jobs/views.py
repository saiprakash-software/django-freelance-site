from django.shortcuts import render, get_object_or_404, redirect
from .models import Job, JobApplication
from django.contrib import messages
from .forms import JobForm
from django.contrib.auth.decorators import login_required  # Ensure user is logged in
from .forms import JobApplicationForm


def job_list(request):
    """ Display all available jobs """
    jobs = Job.objects.all()
    return render(request, 'jobs/job_list.html', {'jobs': jobs})

def job_detail(request, job_id):
    """ Show details of a specific job """
    job = get_object_or_404(Job, id=job_id)
    return render(request, 'jobs/job_detail.html', {'job': job})

def apply_for_job(request, job_id):  # ✅ Ensure this matches `urls.py`
    """ Handle job application """
    job = get_object_or_404(Job, id=job_id)

    if request.method == 'POST':
        applicant_name = request.POST.get('name')
        applicant_email = request.POST.get('email')

        if not applicant_name or not applicant_email:
            messages.error(request, "All fields are required.")
            return redirect('job_detail', job_id=job_id)

        JobApplication.objects.create(job=job, name=applicant_name, email=applicant_email)
        messages.success(request, "Application submitted successfully!")
        return redirect('job_list')

    return render(request, 'jobs/apply.html', {'job': job})


def post_job(request):
    if request.method == 'POST':
        form = JobForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('job_list')
    else:
        form = JobForm()
    return render(request, 'jobs/post_job.html', {'form': form})


@login_required  # Ensure user is logged in before applying

def apply_for_job(request, job_id):
    job = get_object_or_404(Job, id=job_id)
    
    if request.method == "POST":
        form = JobApplicationForm(request.POST)
        if form.is_valid():
            application = form.save(commit=False)
            application.job = job
            application.applicant = request.user  # ✅ Set the applicant
            application.save()
            return redirect('success', job_id=job.id)
            
    else:
        form = JobApplicationForm()

    return render(request, 'jobs/apply_job.html', {'form': form, 'job': job})


def success_view(request, job_id):
    return render(request, 'success.html', {'job_id': job_id})





