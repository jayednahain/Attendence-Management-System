from django.db import models
from django.contrib.auth.models import User
from django.urls import  reverse
from datetime import datetime,date

# Create your models here.

class Department(models.Model):
   dept_title = models.CharField(max_length=50)

   def __str__(self):
      return self.dept_title

    #after creating ! new data will pops up in specific page !
   def get_absolute_url(self):
      return reverse('home_link')



class Students(models.Model):

   author = models.ForeignKey(User,on_delete=models.CASCADE)
   #------------------------------------------------------
   name = models.CharField(max_length=30, blank=False)
   student_id = models.CharField(max_length=30, blank=False)
   department = models.CharField(max_length=30,default='Uncataegorize')

   phone_number = models.CharField(max_length=30,blank=False)
   stundet_email = models.CharField(max_length=30,blank=False)


   student_add_data = models.DateField(auto_now_add=True)
   student_address = models.CharField(max_length=40,blank=False)
   local_guardian_name = models.CharField(max_length=40,blank=False)
   local_guardian_address= models.CharField(max_length=40,blank=False)
   local_guardian_phone= models.CharField(max_length=40,blank=False)





   class Meta:
      ordering = ['-id']




   def __str__(self):
      return self.name + ' | ' + str(self.author)+' | '+ str(self.pk)

    #after creating ! new data will pops up in specific page !
   def get_absolute_url(self):
      return reverse('profile_view_with_class_link',args=[str(self.id)])



