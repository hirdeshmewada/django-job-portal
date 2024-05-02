
from django.urls import path
from hr import views 

urlpatterns = [
    path('hrdash/',views.hrHome_views,name='hrdash'),
    path('post-job/',views.post_job_views,name='post_job'),
    path('candidate-details/<int:pk>',views.candidate_view,name='candidate_details'),
    path('select-candidate/',views.selectCandidate,name='selectCandidate'),
    path('delete-candidate/',views.deleteCandidate,name='deleteCandidate')
]