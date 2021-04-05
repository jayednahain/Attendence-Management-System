from django import forms
from .models import Students







class CreateStudentForm(forms.ModelForm):
   class Meta:
      model = Students
      fields = ('name','student_id','phone_number','email','author','student_address','local_guardian_name','local_guardian_phone','local_guardian_address')



      name_style={
         'class': 'form-control',
         'placeholder': "Type title",

      }
      student_id_style={
         'class': 'form-control',
         'placeholder': "Type Title Page"
      }
      phone_number_style ={
         'class': 'form-control',
         'value':'',
         'id':'author_filed'
      }

      email_style={
         'class': 'form-control',
         'placeholder': "type here full post.."
      }
      author_style = {
         'class': 'form-control',
         'value': '',
         'id': 'author_filed',
         'type': 'hidden'

      }
      student_address_style={
         'class': 'form-control',
         'placeholder': " Type Address",
      }

      local_guardian_name_style = {
         'class': 'form-control',
         'placeholder': "Type local",

      }
      local_guardian_phone_style = {
         'class': 'form-control',
         'placeholder': "Type title",

      }
      local_guardian_address_style = {
         'class': 'form-control',
         'placeholder': "Type title",

      }

      widgets={
         'name':forms.TextInput(attrs=name_style),
         'student_id':forms.TextInput(attrs=student_id_style),
         'phone_number': forms.TextInput(attrs=phone_number_style),
         'email': forms.TextInput(attrs=email_style),
         #'author': forms.TextInput(attrs=author_style),
         'author':forms.Select(attrs=author_style),
         'student_address':forms.TextInput(attrs=student_address_style),
         'local_guardian_name':forms.TextInput(attrs=local_guardian_name_style),
         'local_guardian_phone':forms.TextInput(attrs=local_guardian_phone_style),
         'local_guardian_address':forms.TextInput(attrs=local_guardian_address_style)
      }




class UpdateStudentInformation(forms.ModelForm):
   class Meta:
      model = Students
      fields = ('name','student_id','phone_number','email','author','student_address')



      name_style={
         'class': 'form-control',
         'placeholder': "Type title",

      }
      student_id_style={
         'class': 'form-control',
         'placeholder': "Type Title Page"
      }
      phone_number_style ={
         'class': 'form-control',
         'value':'',
         'id':'author_filed'
      }

      email_style={
         'class': 'form-control',
         'placeholder': "type here full post.."
      }
      author_style = {
         'class': 'form-control',
         'value': '',
         'id': 'author_filed',
         'type': 'hidden'

      }
      student_address_style = {
         'class': 'form-control',
         'placeholder': " Type Address",
      }

      widgets={
         'name':forms.TextInput(attrs=name_style),
         'student_id':forms.TextInput(attrs=student_id_style),
         'phone_number': forms.TextInput(attrs=phone_number_style),
         'email': forms.TextInput(attrs=email_style),
         #'author': forms.TextInput(attrs=author_style),
         'author':forms.Select(attrs=author_style),
         'student_address': forms.TextInput(attrs=student_address_style)
      }