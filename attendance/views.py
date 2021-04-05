from django.http import HttpResponse
from django.shortcuts import render
from student_profile.models import Students
import csv

# Create your views here.

def welcome_page(request):
   return render(request,'welcome_attendence.html')

def student_sql_list(request):
   all_data = Students.objects.all()
   return render(request,'student_list_table.html',{'Students':all_data})

def export(request):
   #return HttpResponse('hellow')

   response = HttpResponse(content_type="text/csv")

   #taking the reponse from data base
   writer_csv = csv.writer(response)
   writer_csv.writerows(['Student_id','Student_name'])

   for student in Students.objects.all().values_list('student_id','name'):
      writer_csv.writerow(student)

   response['Content-Disposition'] ='attachment; filename="records.csv'



   return response




