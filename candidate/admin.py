from django.contrib import admin
from candidate import models
# Register your models here.
#saare ko admin panel me dikhane ke liye 

@admin.register(models.MyApplyJobList)
class MyApplyJobListAdmin(admin.ModelAdmin):
    list_display=('id','user','job','dateYouApply')

@admin.register(models.IsSortList)
class IsSortList(admin.ModelAdmin):
    list_display=('id','user','job','dateYouApply')