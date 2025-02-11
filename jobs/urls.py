from django.urls import path
from . import views
from .views import job_list, job_detail, apply_for_job,success_view # ✅ Match function names



urlpatterns = [
    path('', views.job_list, name='job_list'),
    path('job/<int:job_id>/', views.job_detail, name='job_detail'),
    
    path('job/<int:job_id>/apply/', views.apply_for_job, name='apply_job'),
    path('job/<int:job_id>/apply/success/', views.success_view, name='success'),
    
    
    
]
