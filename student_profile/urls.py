
from django.contrib import admin
from django.urls import path,include
from student_profile import views
from student_profile.views import StudentListView,AddStudentView,ProfileView,UpdateInformationView,DeleteStudent,HomeView,CreateDepartment


urlpatterns = [

    path('',HomeView.as_view(),name='home_link'),
    path('studentlist/',StudentListView.as_view(),name='student_list_link'),
    path('addstudent/',AddStudentView.as_view(),name='add_student_link'),

    #path('studentprofile/<int:id>',views.StudentPorfileView,name='student_profile_link'),
    #path('studentprofile/',views.StudentPorfileView,name='student_profile_link'),
    path('profile_view_with_class/<int:pk>',ProfileView.as_view(),name='profile_view_with_class_link'),
    path('profile_view_with_class/edit/<int:pk>', UpdateInformationView.as_view(), name='update_innformation'),
    path('profile_view_with_class/<int:pk>/delete',DeleteStudent.as_view(), name='delete_student_link'),

    path('search_by_name/',views.search_student,name="search_by_name_link"),
    path('search_by_id/',views.search_by_id,name="search_by_id_link"),

    path('create_data_set/<int:pk>',views.create_image_data,name='create_image_data_link'),
    path('create_depart_ment/',CreateDepartment.as_view(),name='create_department_link'),
    path('View_student_by_department/<str:cats>',views.ViewByDeparment,name='view_category_by_department_link')



    #path('studentlist2/',views.Student_profile_view,name='student_profile_view')
]
