from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from fc6.models import *
from datetime import datetime
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from .utils import *
from decimal import *
from django.core.exceptions import ObjectDoesNotExist, FieldDoesNotExist
from django.forms.models import model_to_dict
from django.core import serializers
import json
from django.core.serializers.json import DjangoJSONEncoder

@login_required()
def home(request):
	return render(request, 'home.html',{})

def field_value(record, fieldName):
	try:
		return getattr(record, fieldName)
	except Exception as e:
		return e

def getStudentList(schoolId):
	''' Returns list of students for active school '''
	
	try:
		
		# get students for active school
		qs = Student.objects.filter(school=schoolId)
		myStudents = list(qs)

		# put each record into serializable dictionary
		studentData = []
		for student in myStudents:
			studentDict = record_to_dict(student)
			studentData.append(studentDict)

		# build and return json data
		data={'status': 'success', 'students': studentData}
		return data

	except Exception as e:
		print('error in getStudentList')
		return {'status': 'error', 'msg': str(e)}

def getCampusesList(schoolId):
	''' returns list of campuses for active school '''

	try:

		# get stucampuses for active school
		qs = Campuses.objects.filter(school=schoolId)
		myCampuses = list(qs)

		# put each record into serializable dictionary
		campusData = []
		for campus in myCampuses:
			campusDict = record_to_dict(campus)
			campusData.append(campusDict)

		# build and return json data
		data={'status': 'success', 'campuses': campusData}
		return data

	except Exception as e:
		print('error in getCampusesList')
		return {'status': 'error', 'msg': str(e)}

def getCheckTosList():
	''' returns list of check-tos '''

	try:

		# get stucampuses for active school
		qs = Checkto.objects.all()
		myCheckTos = list(qs)


		# put each record into serializable dictionary
		checkToData = []
		for ckTo in myCheckTos:
			checkToDict = record_to_dict(ckTo)
			checkToData.append(checkToDict)


		# build and return json data
		data={'status': 'success', 'checkTos': checkToData}
		return data

	except Exception as e:
		print('error in getCheckTosList')
		return {'status': 'error', 'msg': str(e)}

def getEnrollmentStatusesList():
	''' Returns list of all enrollment statuses '''

	try:

		# get enrollment statuses, put in a serializable dictionary
		qs = Enrollmentstatus.objects.all()
		myStatuses = list(qs)
		
		# put each record into serializable dictionary
		statusData = []
		for status in myStatuses:
			statusDict = record_to_dict(status)
			statusData.append(statusDict)

		# build and return json data
		data={'status': 'success', 'enrollmentStatuses': statusData}
		return data
		
	except Exception as e:
		return {'status': 'error', 'msg': str(e)}

def getFederalProgramsList():
	''' Returns list of all federal programs '''

	try:

		# get federal programs, put in a serializable dictionary
		qs = Federalprograms.objects.filter(active=True).order_by('seq')
		myFedPgms = list(qs)
		
		# put each record into serializable dictionary
		fedPgmData = []
		for fedPgm in myFedPgms:
			fedPgmDict = record_to_dict(fedPgm)
			fedPgmData.append(fedPgmDict)

		# build and return json data
		data={'status': 'success', 'federalPrograms': fedPgmData}
		return data
		
	except Exception as e:
		return {'status': 'error', 'msg': str(e)}

def getIsirIrsTypesList():
	''' Returns list of ISIR IRS request types '''

	try:
	
		# get isir verify types, put in a serializable dictionary
		qs = Isirirsreqtypes.objects.all()
		myTypes = list(qs)
		
		# put each record into serializable dictionary
		myData = []
		for verType in myTypes:
			myDict = record_to_dict(verType)
			myData.append(myDict)

		# build and return json data
		data={'status': 'success', 'isirIrsTypes': myData}
		return data

	except Exception as e:
		return {'status': 'error', 'msg': str(e)}
		
def getIsirVerifyTypesList():
	''' Returns list of ISIR Verification types '''

	try:
	
		# get isir verify types, put in a serializable dictionary
		qs = Isirverificationtype.objects.all()
		myTypes = list(qs)
		
		# put each record into serializable dictionary
		myData = []
		for verType in myTypes:
			myDict = record_to_dict(verType)
			myData.append(myDict)

		# build and return json data
		data={'status': 'success', 'isirVerifyTypes': myData}
		return data

	except Exception as e:
		return {'status': 'error', 'msg': str(e)}
		
def getStudentProfiles(userId, studentId):
	''' get profiles for student '''

	try:
		# get profiles for active school and student
		schoolId = int(Usersettings.objects.get(user=userId, setting='ActiveSchool').value)
		qs = Studentprofile.objects.filter(school_id=schoolId, studentid=studentId)
		profiles = list(qs)

		# put each record in a serializable dictionary
		profileData = []
		for profile in profiles:
			profileDict = record_to_dict(profile)
			profileData.append(profileDict)
		
		# build and return json data
		data={'status': 'success', 'profiles': profileData}
		return data
		
	except Exception as e:
		return {'status': 'error', 'msg': str(e)}

def getStudyProgram(pgmId):
	''' get program info '''

	try:
		
		# get program, put in a serializable dictionary
		pgm = Program.objects.get(programid=pgmId)
		program = record_to_dict(pgm)

		# build and return json data
		data={'status': 'success', 'program': program}
		return data

	except Exception as e:
		return {'status': 'error', 'msg': str(e)}

def getStudyProgramsList(schoolId):
	''' get study programs list for active school '''

	try:

		# get program, put in a serializable dictionary
		qs = Program.objects.filter(school=schoolId)
		myPrograms = list(qs)

		# put each record into serializable dictionary
		programData = []
		for program in myPrograms:
			programDict = record_to_dict(program)
			programData.append(programDict)

		# build and return json data
		data={'status': 'success', 'studyPrograms': programData}
		return data

	except Exception as e:
		print('error in getStudyProgramsList')
		return {'status': 'error', 'msg': str(e)}

def getEnrollmentStatus(statusId):
	''' get enrollment status info '''

	try:
		
		# get enrollment, put in a serializable dictionary
		enr = Enrollmentstatus.objects.get(enrollmentstatusid=statusId)
		status = record_to_dict(enr)

		# build and return json data
		data={'status': 'success', 'enrollmentstatus': status}
		return data

	except Exception as e:
		return {'status': 'error', 'msg': str(e)}

def getStudentFundings(userId, studentId):
	''' get fundings for student '''

	try:

		# get profiles for active school and student
		schoolId = int(Usersettings.objects.get(user=userId, setting='ActiveSchool').value)
		qs = Studentprofile.objects.filter(school_id=schoolId, studentid=studentId)
		profiles = list(qs)

		# get fundings for profiles found
		qs = Studentfunding.objects.filter(studentprofileid__in=[p.studentprofileid for p in profiles])
		fundings = list(qs)

		# put each record in a serializable dictionary
		fundingData = []
		for funding in fundings:
			
			fundingDict = record_to_dict(funding)
			fundingData.append(fundingDict)
		
		# build and return json data
		data={'status': 'success', 'fundings': fundingData}
		return data
		
	except Exception as e:
		return {'status': 'error', 'msg': str(e)}

def getStudentPayments(userId, studentId):
	''' get payments for student '''

	try:

		# get payments for active school and student
		schoolId = int(Usersettings.objects.get(user=userId, setting='ActiveSchool').value)
		qs = Payments.objects.filter(school_id=schoolId, studentid=studentId)
		payments = list(qs)

		# put each record in a serializable dictionary
		paymentData = []
		for payment in payments:
			
			paymentDict = record_to_dict(payment)
			paymentData.append(paymentDict)

		# build and return json data
		data={'status': 'success', 'payments': paymentData}
		return data

	except Exception as e:
		return {'status': 'error', 'msg': str(e)}

def addStudent(newData):
	''' add student record '''

	try:
		currentRecord = Student()
		currentRecord = dict_to_record('add', newData, currentRecord)
		currentRecord.save()
		data = record_to_dict(currentRecord)
		data['status'] = 'success'
		return data

	except Exception as e:
		return {'status': 'error', 'msg': str(e)}

def updateStudent(newData):
	''' update student record '''

	try:
		currentRecord = Student.objects.get(studentid=newData['studentid'])
		currentRecord = dict_to_record('update', newData, currentRecord)
		currentRecord.save()
		data = record_to_dict(currentRecord)
		data['status'] = 'success'
		return data

	except ObjectDoesNotExist:
		msg = 'No student found with ID: %s' % (newData['studentid'])
		return {'status': 'error', 'msg': msg}

	except Exception as e:
		return {'status': 'error', 'msg': str(e)}

def addProfile(newData):
	''' add profile record '''

	try:
		currentRecord = Studentprofile()
		currentRecord = dict_to_record('add', newData, currentRecord)
		currentRecord.save()
		data = record_to_dict(currentRecord)
		data['status'] = 'success'
		return data

	except Exception as e:
		return {'status': 'error', 'msg': str(e)}

def updateProfile(newData):
	''' update profile record '''

	try:
		currentRecord = Studentprofile.objects.get(studentprofileid=newData['studentprofileid'])
		currentRecord = dict_to_record('update', newData, currentRecord)
		currentRecord.save()
		data = record_to_dict(currentRecord)
		data['status'] = 'success'
		return data

	except ObjectDoesNotExist:
		msg = 'No profiles found with ID: %s' % (newData['studentprofileid'])
		return {'status': 'error', 'msg': msg}

	except Exception as e:
		return {'status': 'error', 'msg': str(e)}

def addFunding(newData):
	''' add student funding record '''

	try:
		currentRecord = Studentfunding()
		currentRecord = dict_to_record('add', newData, currentRecord)
		currentRecord.save()
		data = record_to_dict(currentRecord)
		data['status'] = 'success'
		return data

	except Exception as e:
		return {'status': 'error', 'msg': str(e)}

def updateFunding(newData):
	''' update student funding record '''

	try:
		currentRecord = Studentfunding.objects.get(studentfundingid=newData['studentfundingid'])
		currentRecord = dict_to_record('update', newData, currentRecord)
		currentRecord.save()
		data = record_to_dict(currentRecord)
		data['status'] = 'success'
		return data

	except ObjectDoesNotExist:
		msg = 'No student fundings found with ID: %s' % (newData['studentfundingid'])
		return {'status': 'error', 'msg': msg}

	except Exception as e:
		return {'status': 'error', 'msg': str(e)}

def addPayment(newData):
	''' add payment record '''

	try:
		currentRecord = Payments()
		currentRecord = dict_to_record('add', newData, currentRecord)
		currentRecord.save()
		data = record_to_dict(currentRecord)
		data['status'] = 'success'
		return data

	except Exception as e:
		return {'status': 'error', 'msg': str(e)}

def updatePayment(newData):
	''' update payment record '''

	try:
		currentRecord = Payments.objects.get(paymentid=newData['paymentid'])
		currentRecord = dict_to_record('update', newData, currentRecord)
		currentRecord.save()
		data = record_to_dict(currentRecord)
		data['status'] = 'success'
		return data

	except ObjectDoesNotExist:
		msg = 'No payments found with ID: %s' % (newData['paymentid'])
		return {'status': 'error', 'msg': msg}

	except Exception as e:
		return {'status': 'error', 'msg': str(e)}

def getReportList():
	''' returns list of reports with date codes resolved
		ex: ThisYear code is converted to 1/1 and 12/31 of current year '''

	try:

		# get list of reports
		qs = Reports.objects.all()
		reportList = list(qs)

		# put each record in dictionary, handle foreign-key, fix dates
		reportData = []
		for report in reportList:
			reportDict = record_to_dict(report)

			# convert date codes
			realDates = codeToDate((reportDict['startdatedefault'],reportDict['enddatedefault']))
			if realDates[0] == 'None':
				reportDict['startdatedefault'] = ''
			else:
				reportDict['startdatedefault'] = realDates[0].strftime('%m/%d/%Y %H:%M:%S')
			if realDates[1] == 'None':
				reportDict['enddatedefault'] = ''
			else:
				reportDict['enddatedefault'] = realDates[1].strftime('%m/%d/%Y %H:%M:%S')

			# convert award year
			awdYrs = fiscalYearList(True,3)
			if reportDict['awardyeardefault'] == 'None':
				reportDict['awardyeardefault'] = awdYrs[0]['value']
			if reportDict['awardyeardefault'] == 'Next':
				reportDict['awardyeardefault'] = awdYrs[1]['value']
			if reportDict['awardyeardefault'] == 'Current':
				reportDict['awardyeardefault'] = awdYrs[2]['value']
			if reportDict['awardyeardefault'] == 'Prior':
				reportDict['awardyeardefault'] = awdYrs[3]['value']
			
			reportData.append(reportDict)
			
		# build and return json data
		data={'status': 'success', 'reports': reportData}

		return data

	except Exception as e:
		return {'status': 'error', 'msg': '%s: %s' %('Error in getReportList', str(e))}
		
