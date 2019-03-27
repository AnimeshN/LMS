
from django.urls import path
from . import views

urlpatterns = [
    path('',views.home, name = 'home'),
    path('ncertadmin/',views.ncertAdmin, name = 'ncertuser'),
    path('districtmanagement/',views.districtManagement, name = 'districtuser'),
    path('schoolmanagement/',views.schoolManagement, name = 'schooluser'),
    path('teacher/',views.teacherUser, name = 'teacheruser'),
    path('logout/',views.logout_user, name = 'logoutU'),
    path('login/',views.login_user, name = 'login'),

    

]