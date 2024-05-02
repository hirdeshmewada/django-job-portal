from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Hr(models.Model):
    user=models.OneToOneField(to=User,on_delete=models.CASCADE)

# ek job post banai jb bhi hr job post krega usse hame kya information deni hogi jaise kis 
# kisne banai kya title hain company ka address slary low hain ya high and count and last date
class JobPost(models.Model):
    user=models.ForeignKey(to=User,on_delete=models.CASCADE) 
    title= models.CharField(max_length=200)
    address=models.CharField(max_length=200)
    companyName=models.CharField(max_length=200)
    salaryLow=models.IntegerField(default=0)
    salaryHigh=models.IntegerField(default=0)
    applycount=models.IntegerField(default=0)
    lastDateToApply=models.DateField()
    
    def __str__(self):
        return str(self.title)
    
STATUS_CHOICE =(
    ('pending','pending'),
    ('selected','selected')
)

# agr koi candidate  apply krta hain toh uski details le rhe hain 
class CandidateApplication(models.Model):
    user= models.ForeignKey(to=User,on_delete=models.CASCADE)
    job= models.OneToOneField(to=JobPost,on_delete=models.CASCADE)
    passingYear=models.IntegerField()
    yearOfExp =models.IntegerField(default=0)
    resume= models.FileField(upload_to='resume')
    status=models.CharField(choices=STATUS_CHOICE,max_length=20,default='pending')


#table is app ke liye kaunse candidate slecte hua 
class SelectCandidateJob(models.Model):
    job=models.ForeignKey(to=JobPost,on_delete=models.CASCADE)
    candidate= models.OneToOneField(to=CandidateApplication,on_delete=models.CASCADE)