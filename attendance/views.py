from django.http import HttpResponse
from django.shortcuts import render
from student_profile.models import Students

# Create your views here.

def welcome_page(request):
   return render(request,'welcome_attendence.html')

def student_sql_list(request):
   all_data = Students.objects.all()
   return render(request,'student_list_table.html',{'Students':all_data})

def export(request):
   return HttpResponse('hellow')

