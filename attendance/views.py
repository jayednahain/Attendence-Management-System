from django.http import HttpResponse
from django.shortcuts import render, redirect
from student_profile.models import Students

import cv2
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

def face_test(request):
   return render(request,'face_testing.html')


def take_image(request):
   import cv2

   #path = 'cascadefile/haarcascade_frontalface_default.xml'

   # Load the cascade
   face_cascade = cv2.CascadeClassifier('cascadefile/haarcascade_frontalface_default.xml')

   # To capture video from webcam.
   cap = cv2.VideoCapture(0)
   # To use a video file as input
   # cap = cv2.VideoCapture('filename.mp4')

   while True:
      # Read the frame
      _, img = cap.read()
      # Convert to grayscale
      gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
      # Detect the faces
      faces = face_cascade.detectMultiScale(gray, 1.1, 4)
      # Draw the rectangle around each face
      for (x, y, w, h) in faces:
         cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)
      # Display
      cv2.imshow('img', img)
      # Stop if escape key is pressed
      k = cv2.waitKey(30) & 0xff
      if k == 27:
         break
   # Release the VideoCapture object
   cap.release()

   return redirect('face_test_page_link')






