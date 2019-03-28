
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

    path('usermanagement/',views.userManagement, name = 'usermanage'),#ncert
    path('uploadevidence/',views.uploadEvidence, name = 'uploadEvi'),#teacher
    path('activityplan/',views.activityPlan, name = 'activityP'),#teacher



    

]