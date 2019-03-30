
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
    path('learning_outcome/',views.learningOutcomeReport, name = 'lout'),#ncert
    path('resource_management/',views.resourceManagement, name = 'rmanage'),#ncert
    path('information_and_update/',views.informationAndUpdate, name = 'infoup'),#ncert
    path('support_and_supervision/',views.supportAndSupervision, name = 'sas'),#ncert

    path('teacher_performance/',views.teacherPerformance, name = 'tp'),#ncert/support
    path('student_performance/',views.studentPerformance, name = 'sp'),#ncert/support
    path('teacher_support/',views.teacherSupport, name = 'ts'),#ncert/support
    path('student_support/',views.studentSupport, name = 'ss'),#ncert/support


    path('uploadevidence/',views.uploadEvidence, name = 'uploadEvi'),#teacher
    path('activityplan/',views.activityPlan, name = 'activityP'),#teacher
    path('llo/',views.lowestLearningOutcome, name = 'lowestlo'),#teacher
    path('student_learning_outcome/',views.studentLearningOutcome, name = 'slo'),#teacher
    path('progress_report/',views.progressReport, name = 'pr'),#teacher
    path('view_content_and_resource/',views.viewContentAndResource, name = 'vcar'),#teacher




    

]