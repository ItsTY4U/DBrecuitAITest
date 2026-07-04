from django.shortcuts import render, get_object_or_404
from django.db.models import Q
from .models import Job
from .models import Job, Application


def jobs(request):
    query = request.GET.get("q", "")
    department = request.GET.get("department", "")
    jobs = Job.objects.filter(is_active=True)
    if query:
        jobs = jobs.filter(
            Q(title__icontains=query) |
            Q(department__icontains=query)
        )
    if department:
        jobs = jobs.filter(department=department)
    
    if request.headers.get("HX-Request"):
        return render(request, "jobs/partials/jobs_list.html", {
            "jobs": jobs
        })
    return render(request, "jobs/jobs.html", {
        "jobs": jobs
    })

def job_detail(request, id):
    job = get_object_or_404(Job, id=id)
    return render(request, "jobs/job_detail.html", {
        "job": job
    })
    
def apply_job(request, pk):
    job = get_object_or_404(Job, pk=pk)
    
    if request.method == "POST":
        application = Application.objects.create(
            job=job,
            first_name=request.POST.get("first_name"),
            middle_initial=request.POST.get("middle_initial"),
            last_name=request.POST.get("last_name"),
            email=request.POST.get("email"),
            phone=request.POST.get("phone"),
            resume=request.FILES.get("resume")
        )
        
        return render(request, "jobs/partials/success.html", {"application":application})
    
    return render(request, "jobs/apply.html", {"job": job})