"""fc6 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from . import views
from django.conf.urls import url
from django.contrib import admin

urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^admin/', admin.site.urls),
    url(r'^students/$', views.studentsAndProfiles, name='students_and_profiles'),
    url(r'^reports/$', views.reports, name='reports'),
    url(r'^setschoolandyear/$', views.setSchoolAndYear, name='set_school_and_year'),
    url(r'^getawardyears/$', views.getAwardYears, name='get_award_years'),
    url(r'^getcampuses/$', views.getCampuses, name='get_campuses'),
    url(r'^getchecktos/$', views.getCheckTos, name='get_check_tos'),
    url(r'^getenrollmentstatuses/$', views.getEnrollmentStatuses, name='get_enrollment_statuses'),
    url(r'^getfederalprograms/$', views.getFederalPrograms, name='get_federal_programs'),
    url(r'^getisirirstypes/$', views.getIsirIrsTypes, name='get_isir_irs_types'),
    url(r'getisirverifytypes/$', views.getIsirVerifyTypes, name='get_isir_verify_types'),
    url(r'^getstudents/$', views.getStudents, name='get_students'),
    url(r'^getstudentdata/(?P<id>[0-9]+)/$', views.getStudentData, name='get_student_data'),
    url(r'^getstudyprograms/$', views.getStudyPrograms, name='get_study_programs'),
    url(r'^setstudent/(?P<mode>\w+)/$', views.setStudent, name='set_student'),
    url(r'^setprofile/(?P<mode>\w+)/$', views.setProfile, name='set_profile'),
    url(r'^setfunding/(?P<mode>\w+)/$', views.setFunding, name='set_funding'),
    url(r'^setpayment/(?P<mode>\w+)/$', views.setPayment, name='set_payment'),
    url(r'^getreports', views.getReports, name='get_reports'),
    url(r'^generatereport', views.generateReport, name='generate_report'),
]
