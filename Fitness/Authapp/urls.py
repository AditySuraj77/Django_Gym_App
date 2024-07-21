from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
    path('', views.Home,name="Home"),
    path('SignUp',views.SignUp,name='SignUp'),
    path('LogIn',views.LogIn,name='LogIn'),
    path('LogOut',views.LogOut,name='LogOut'),
    path('Contact',views.contact,name='contact'),
    path('Enrollment',views.Enrollments,name='Enrollment'),
    path('Profile',views.Profile,name='Profile'),
    path('Attendence',views.Attendence,name='Attendence'),
    path('<int:delete_id>/deleteAttendence/',views.Delete_attendence,name='Delete_attendence'),

]
