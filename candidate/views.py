from django.shortcuts import redirect, render 
from django.contrib.auth.decorators import login_required

from hr.models import JobPost,CandidateApplication,Hr
from candidate.models import MyApplyJobList
# Create your views here.
@login_required
def candidate_dashboard(request):
    jobs=JobPost.objects.all()
    print(jobs)
    return render(request,'candidate/dashboard.html',{'jobs':jobs})

@login_required
def myJobListviews(request):
    
    myjoblist=MyApplyJobList.objects.filter(user=request.user)
    print(myjoblist)
    return render(request,'candidate\myjoblist.html',{'myjoblist':myjoblist})

@login_required
def applyforjob(request,pk):
    if Hr.objects.filter(user=request.user).exists():
        return redirect('hrdash')
    if JobPost.objects.filter(id=pk).exists():
     if CandidateApplication.objects.filter(user=request.user).exists():
            return redirect('candidate_dashboard')
     print(pk)

     if request.method=='POST':
        name=request.POST.get('name')
        email= request.POST.get('email')
        college=request.POST.get('college')
        passing_year=request.POST.get('passing_year')
        yearOfExperience =request.POST.get('yearOfExperience')
        resume=request.FILES.get('resume')
        job=JobPost.objects.get(id=pk)

        candidate_application=CandidateApplication(user=request.user,job=job,passingYear=passing_year,yearOfExp=yearOfExperience,resume=resume)
        candidate_application.save()
        MyApplyJobList(user=request.user,job=candidate_application).save()
        job.applycount += 1
        job.save()
        return redirect('candidate_dashboard')
    return render(request,'candidate/apply.html')