from django.shortcuts import redirect, render
from hr.models import Hr, JobPost, CandidateApplication, SelectCandidateJob
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404
# Create your views here.
@login_required
def hrHome_views(request):
    if Hr.objects.filter(user=request.user).exists():
          jobpost =JobPost.objects.filter(user=request.user)
          print(jobpost)
          return render(request,'hr/hrdash.html',{'jobpost':jobpost})
    return redirect('candidate_dashboard')
@login_required
def post_job_views(request):
    msg=None
    if request.method=='POST':
        job_title=request.POST.get('job-title')
        address=request.POST.get('address')
        company_name=request.POST.get('company-name')
        salary_low=request.POST.get('salary-low')
        salary_high=request.POST.get('salary-high')
        last_date=request.POST.get('last-date')
        print(job_title+""+address+""+company_name+"")
        msg="Job Added succesfully"
        job_post=JobPost(user=request.user,title=job_title,address=address,companyName=company_name,salaryHigh=salary_high,salaryLow=salary_low,lastDateToApply=last_date)
        job_post.save()
    return render(request,'hr/postjob.html',{'msg':msg})

@login_required
def candidate_view(request,pk):

    if JobPost.objects.filter(id=pk).exists(): 
        jobpost=JobPost.objects.get(id=pk)
        applications = CandidateApplication.objects.filter(job=jobpost)
        selectedapplications=SelectCandidateJob.objects.filter(job=jobpost)
        print(applications)
        print(selectedapplications)
        return render(request,'hr/candidate.html',{'applications':applications,'selectedapplications':selectedapplications,'jobpost':jobpost})
    else:
        return redirect('hr_dash')

@login_required
def selectCandidate(request):
    if request.method=='POST':
        candidateid=request.POST.get('candidateid')
        jobpostid=request.POST.get('jobpostid')
        job=JobPost.objects.get(id=jobpostid)
        candidate=CandidateApplication.objects.get(id=candidateid)
        SelectCandidateJob(job=job,candidate=candidate).save()
        
    return redirect('hrdash')

@login_required
def deleteCandidate(request):
    if request.method=='POST':
        candidateid=request.POST.get('candidateid')
        jobpostid=request.POST.get('jobpostid')
        job=JobPost.objects.get(id=jobpostid)
        candidate=CandidateApplication.objects.get(id=candidateid).delete()
        job.applycount=job.applycount-1
        job.save()
    return redirect('hrdash')