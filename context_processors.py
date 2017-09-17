from fc6.models import Schoolinfo
from .utils import *
from django.forms.models import model_to_dict

def getAwardYears(request):
    if request.user.is_authenticated():
        activeYear = Usersettings.objects.get(user=request.user, setting='ActiveYear').value
    else:
        activeYear = ''
    awardYears = fiscalYearList(False,9,2)
    awardYearsBlank = fiscalYearList(True,9,2)
    return {'awardYears': awardYears, 'awardYearsBlank':awardYearsBlank, 'activeYear': activeYear}

def getSchools(request):
     
    if request.user.is_authenticated():
        sch = int(Usersettings.objects.get(user=request.user, setting='ActiveSchool').value)
        # activeSchool = record_to_dict(Schoolinfo.objects.get(school_id=sch))
    else:
        sch = 0
        # activeSchool = {}
    
    qs = Schoolinfo.objects.all()
    mySchools = list(qs)

    # put each record into serializable dictionary
    schoolData = []
    for school in mySchools:
        schoolDict=record_to_dict(school)
        schoolData.append(schoolDict)
    
    return {'schools': schoolData, 'currentSchool': sch}
    