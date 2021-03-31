from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from django.urls import reverse_lazy

from django.views.generic import ListView
from django.views.generic import CreateView
from django.views.generic import DetailView
from django.views.generic import UpdateView
from django.views.generic import DeleteView
from django.views.generic import TemplateView

from student_profile.models import Students

from .forms import CreateStudentForm,UpdateStudentInformation


# Create your views here.


class HomeView(TemplateView):
   template_name = 'home.html'

   def get_context_data(self, **kwargs):
      context = super().get_context_data(**kwargs)
      context['data']=Students.objects.all()

      return context




class StudentListView(ListView):
   model = Students
   template_name = 'student_list.html'



def search_student(request):
   if 'term' in request.GET:
      qs = Students.objects.filter(name__icontains=request.GET.get('term'))
      student_names = list()
      for student in qs:
         student_names.append(student.name)
      # titles = [product.title for product in qs]
      return JsonResponse(student_names, safe=False)
   return render(request,'student_search.html')



def search_by_id(request):
   if 'term' in request.GET:
      qs = Students.objects.filter(student_id__icontains=request.GET.get('term'))
      student_id_list = list()
      for student_id in qs:
         student_id_list.append(student_id.student_id)
      # titles = [product.title for product in qs]
      return JsonResponse(student_id_list, safe=False)
   return render(request,'student_search_by_id.html')







class ProfileView(DetailView):
   model = Students
   template_name = 'profile_view_with_class.html'


class AddStudentView(CreateView):
   form_class = CreateStudentForm
   model = Students
   template_name = 'add_student.html'

   #we have define fields on form.py
   #fields = '__all__'

class UpdateInformationView(UpdateView):
   form_class = UpdateStudentInformation
   model = Students
   template_name = 'Update_student_information.html'


class DeleteStudent(DeleteView):
   model = Students
   template_name = 'delete_post_view.html'
   success_url = reverse_lazy('student_list_link')







