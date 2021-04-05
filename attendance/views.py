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

   #response = HttpResponse(content_type="text/csv")

   #taking the reponse from data base
   #writer_csv = csv.writer(response)
   #writer_csv.writerow(['Student_id','Student_name'])


   with open('records.csv','w', newline='') as csvFile:
      for student in Students.objects.all().values_list('student_id', 'name'):
         student_list = list(student)
         writer = csv.writer(csvFile)
         #writer = (['Student_id','Student_name'])

         writer.writerows(student_list)
         #print(type(student_list),"|",student_list)
   #csvFile.close()
   for student in Students.objects.all().values_list('student_id', 'name'):
      student_list = list(student)
      writer = csv.writer(csvFile)
      # writer = (['Student_id','Student_name'])

      writer.writerows(student_list)


   return HttpResponse('complete')




