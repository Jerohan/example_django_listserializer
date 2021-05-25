from myapp.views import EmployesApiView
from django.urls import path
from myapp import  *


urlpatterns = [    
    path('myapp/',  EmployesApiView.as_view()),
]