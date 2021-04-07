from django import forms
from .models import Students
from .models import Department


dept_choise = Department.objects.all().values_list('dept_title','dept_title')

dept_choise_list=[]
for item in dept_choise:
   dept_choise_list.append(item)




class CreateStudentForm(forms.ModelForm):
   class Meta:
      model = Students
      fields = ('name','student_id','phone_number','stundet_email','department','author','student_address','local_guardian_name','local_guardian_phone','local_guardian_address')


      widgets={
         'name':forms.TextInput(attrs={'class': 'form-control'}),
         'student_id':forms.TextInput(attrs={'class': 'form-control'}),
         'phone_number': forms.TextInput(attrs={'class': 'form-control'}),
         'stundet_email':forms.TextInput(attrs={'class': 'form-control'}),



         'author':forms.Select(attrs={'class': 'form-control'}),
         'department':forms.Select(choices=dept_choise_list,attrs={'class': 'form-control'}),
         'student_address':forms.TextInput(attrs={'class': 'form-control'}),

         'local_guardian_name':forms.TextInput(attrs={'class': 'form-control'}),
         'local_guardian_phone':forms.TextInput(attrs={'class': 'form-control'}),
         'local_guardian_address':forms.TextInput(attrs={'class': 'form-control'})
      }




class UpdateStudentInformation(forms.ModelForm):
   class Meta:
      model = Students
      fields = ('name','student_id','phone_number','department','stundet_email','author','student_address','local_guardian_name','local_guardian_phone','local_guardian_address')


      widgets={
         'name':forms.TextInput(attrs={'class': 'form-control'}),
         'student_id':forms.TextInput(attrs={'class': 'form-control'}),
         'phone_number': forms.TextInput(attrs={'class': 'form-control'}),
         'stundet_email':forms.TextInput(attrs={'class': 'form-control'}),


         'department':forms.Select(choices=dept_choise_list,attrs={'class': 'form-control'}),
         'author':forms.Select(attrs={'class': 'form-control'}),

         'student_address': forms.TextInput(attrs={'class': 'form-control'}),
         'local_guardian_name': forms.TextInput(attrs={'class': 'form-control'}),
         'local_guardian_phone': forms.TextInput(attrs={'class': 'form-control'}),
         'local_guardian_address': forms.TextInput(attrs={'class': 'form-control'})
      }