from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from fc6.models import *
from datetime import datetime
from django.http import HttpResponse, HttpResponseRedirect
from django.views.decorators.csrf import csrf_exempt
from .utils import *
from decimal import *
from django.core.exceptions import ObjectDoesNotExist, FieldDoesNotExist
from .services import *
import mysql.connector
# import MySQLdb
import pandas as pd
from pandas import DataFrame
from pandas.io.json import json_normalize
import pymysql.cursors

@login_required()
def home(request):
	return render(request, 'home.html', {})

@csrf_exempt
def studentsAndProfiles(request):

	return render(request, 'student_form.html', {})
	#return render(request, 'student_form.html', {'allStudents':Student.objects.all()})
	
	#try:
	#	schoolId = Usersettings.objects.get(user=request.user, setting='ActiveSchool').value
	#	data = getStudentList(schoolId)
	#	return render(request, 'student_form.html', data)
	
		#except Exception as e:

def reports(request):

	return render(request, 'report_form.html', {})

def setSchoolAndYear(request):
	# post request stuff to database
	# use request.body.whatever
	if request.method == 'POST':

		print(request.POST)
		if 'select_school' in request.POST:
			setting, created = Usersettings.objects.get_or_create(user = request.user, setting = 'ActiveSchool')
			setting.value = request.POST['select_school']
			setting.save()

		if 'select_award_year' in request.POST:
			setting, created = Usersettings.objects.get_or_create(user = request.user, setting = 'ActiveYear')
			setting.value = request.POST['select_award_year']
			setting.save()
		
		return HttpResponseRedirect('/')

@csrf_exempt
def getAwardYears(request):
	''' returns list of award years 
		defaults to no blank item at top, 5 items in list, 2-digit years, 
		current year 2nd item in list '''
	if request.method == 'POST':

		try:

			data = json.loads(request.body.decode('utf-8'))
			blankItem = bool(data['blankItemAtTop'])
			awardYears = int(data['years'])
			digits = int(data['digits'])
			fyData = fiscalYearList(blankItem, awardYears, digits, 2)
			
			# build and return json data
			data={'status': 'success', 'awardYears': fyData}
			return HttpResponse(
				json.dumps(data),
				content_type = 'application/json'
			)
			
		except Exception as e:
			return HttpResponse(
				json.dumps({'status': 'error', 'msg': str(e)}),
				content_type = 'application/json'
			)

	else:
		return HttpResponse(
			json.dumps({'status': 'error', 'msg': 'Unable to execute request'}),
			content_type = 'application/json'
		)

@csrf_exempt
def getCampuses(request):
	if request.method == 'GET':
		try:
			
			# get campuses for active school
			schoolId = Usersettings.objects.get(user=request.user, setting='ActiveSchool').value
			data = getCampusesList(schoolId)
			return HttpResponse(
				json.dumps(data),
				content_type = 'application/json'
			)
			
		except Exception as e:
			return HttpResponse(
				json.dumps({'status': 'error', 'msg': str(e)}),
				content_type = 'application/json'
			)

	else:
		return HttpResponse(
			json.dumps({'status': 'error', 'msg': 'Unable to execute request'}),
			content_type = 'application/json'
		)

def getCheckTos(request):
	if request.method == 'GET':
		try:
			
			data = getCheckTosList()
			return HttpResponse(
				json.dumps(data),
				content_type = 'application/json'
			)
			
		except Exception as e:
			return HttpResponse(
				json.dumps({'status': 'error', 'msg': str(e)}),
				content_type = 'application/json'
			)

	else:
		return HttpResponse(
			json.dumps({'status': 'error', 'msg': 'Unable to execute request'}),
			content_type = 'application/json'
		)
	
@csrf_exempt
def getEnrollmentStatuses(request):
	if request.method == 'GET':
		try:
			
			data = getEnrollmentStatusesList()
		
			return HttpResponse(
				json.dumps(data),
				content_type = 'application/json'
			)
			
		except Exception as e:
			return HttpResponse(
				json.dumps({'status': 'error', 'msg': str(e)}),
				content_type = 'application/json'
			)

	else:
		return HttpResponse(
			json.dumps({'status': 'error', 'msg': 'Unable to execute request'}),
			content_type = 'application/json'
		)

@csrf_exempt
def getFederalPrograms(request):
	if request.method == 'GET':
		try:
			
			data = getFederalProgramsList()
		
			return HttpResponse(
				json.dumps(data),
				content_type = 'application/json'
			)
			
		except Exception as e:
			return HttpResponse(
				json.dumps({'status': 'error', 'msg': str(e)}),
				content_type = 'application/json'
			)

	else:
		return HttpResponse(
			json.dumps({'status': 'error', 'msg': 'Unable to execute request'}),
			content_type = 'application/json'
		)

@csrf_exempt
def getIsirIrsTypes(request):
	if request.method == 'GET':
		try:
			
			data = getIsirIrsTypesList()
		
			return HttpResponse(
				json.dumps(data),
				content_type = 'application/json'
			)
			
		except Exception as e:
			return HttpResponse(
				json.dumps({'status': 'error', 'msg': str(e)}),
				content_type = 'application/json'
			)

	else:
		return HttpResponse(
			json.dumps({'status': 'error', 'msg': 'Unable to execute request'}),
			content_type = 'application/json'
		)

@csrf_exempt
def getIsirVerifyTypes(request):
	if request.method == 'GET':
		try:
			
			data = getIsirVerifyTypesList()
		
			return HttpResponse(
				json.dumps(data),
				content_type = 'application/json'
			)
			
		except Exception as e:
			return HttpResponse(
				json.dumps({'status': 'error', 'msg': str(e)}),
				content_type = 'application/json'
			)

	else:
		return HttpResponse(
			json.dumps({'status': 'error', 'msg': 'Unable to execute request'}),
			content_type = 'application/json'
		)

@csrf_exempt
def getReports(request):
	''' returns list of reports with date codes resolved
		ex: ThisYear code is converted to 1/1 and 12/31 of current year '''

	if request.method == 'GET':
	
		try:
			
			reportData = getReportList()

			# build and return json data
			data={'status': 'success', 'reports': reportData['reports']}
			return HttpResponse(
				json.dumps(data),
				content_type = 'application/json'
			)

		except Exception as e:
			return HttpResponse(
				json.dumps({'status': 'error', 'msg': '%s: %s' %('Error in getReports', str(e))}),
				content_type = 'application/json'
			)

	else:
		return HttpResponse(
			json.dumps({'status': 'error', 'msg': 'Unable to execute request'}),
			content_type = 'application/json'
		)
	
@csrf_exempt
def getStudentData(request, id):
	''' Returns list of profiles, fundings and payments for active student and school '''

	if request.method == 'GET':
	
		try:
			# get profiles for active school and student
			data = getStudentProfiles(request.user, id)
			if data['status'] == 'success':
				profileData = data['profiles']
				
				# get associated values
				for profile in profileData:

					# study program
					id = int(profile['programid'])
					sp = getStudyProgram(id)
					pgmName = sp['program']['programname']
					other1 = sp['program']['otherfee1desc']
					other2 = sp['program']['otherfee2desc']
					profile['programname'] = pgmName
					profile['otherfee1desc'] = other1
					profile['otherfee2desc'] = other2
					
					# enrollment status
					id = int(profile['enrollmentstatusid'])
					es = getEnrollmentStatus(id)
					enrollStatus = es['enrollmentstatus']['enrollmentstatus']
					profile['enrollmentstatus'] = enrollStatus



				data = getStudentFundings(request.user, id)
				if data['status'] == 'success':
					fundingData = data['fundings']

					data = getStudentPayments(request.user, id)
					if data['status'] == 'success':
						paymentData = data['payments']

						# build and return json data
						data={'status': 'success', 'profiles': profileData, 'fundings': fundingData, 'payments': paymentData}
						return HttpResponse(
							json.dumps(data),
							content_type = 'application/json'
						)

					else: # error in payments
						return data
				else: # error in fundings
					return data
			else: # error in profiles
				return data

		except Exception as e:
			return HttpResponse(
				json.dumps({'status': 'error', 'msg': str(e)}),
				content_type = 'application/json'
			)

	else:
		return HttpResponse(
			json.dumps({'status': 'error', 'msg': 'Unable to execute request'}),
			content_type = 'application/json'
		)

@csrf_exempt
def getStudents(request):
	''' Returns list of students for active school '''
	
	if request.method == 'GET':
		
		try:
			
			# get students for active school
			schoolId = Usersettings.objects.get(user=request.user, setting='ActiveSchool').value
			data = getStudentList(schoolId)
			return HttpResponse(
				json.dumps(data),
				content_type = 'application/json'
			)

		except Exception as e:
			return HttpResponse(
				json.dumps({'status': 'error', 'msg': str(e)}),
				content_type = 'application/json'
			)

	else:
		return HttpResponse(
			json.dumps({'status': 'error', 'msg': 'Unable to execute request'}),
			content_type = 'application/json'
		)

@csrf_exempt
def getStudyPrograms(request):
	''' Returns list of study programs for active school '''
	
	if request.method == 'GET':
		
		try:
			
			# get study programs for active school
			schoolId = Usersettings.objects.get(user=request.user, setting='ActiveSchool').value
			data = getStudyProgramsList(schoolId)
			return HttpResponse(
				json.dumps(data),
				content_type = 'application/json'
			)

		except Exception as e:
			return HttpResponse(
				json.dumps({'status': 'error', 'msg': str(e)}),
				content_type = 'application/json'
			)

	else:
		return HttpResponse(
			json.dumps({'status': 'error', 'msg': 'Unable to execute request'}),
			content_type = 'application/json'
		)
	

# setters
@csrf_exempt
def setStudent(request, mode):
	''' add or update a student record '''

	if request.method == 'POST':
		
		str_response = request.body.decode('utf-8')
		newData = json.loads(str_response) #[0]
		print(newData)

		try:
			
			# depending on mode, get record or new record to update
			if mode == 'add':
				
				# check required fields for adding record
				reqFields = ['school','ssn']
				if len([field for field in reqFields if field not in newData]) > 0:
					return HttpResponse(
						json.dumps({'status': 'error', 'msg': 'required fields missing: %s' % (','.join(missing))}),
						content_type = 'application/json'
					)

				# get required items if not supplied
				if 'schoolid' not in newData:
					s = Schoolinfo.objects.get(school_id=newData['school'])
					newData['schoolid'] = s.schoolid
				
				data = addStudent(newData)

			else:

				# check required fields for changing record
				reqFields = ['studentid']
				missing = [field for field in reqFields if field not in newData]
				if len(missing) > 0:
					return HttpResponse(
						json.dumps({'status': 'error', 'msg': 'required fields missing: %s' % (','.join(missing))}),
						content_type = 'application/json'
					)

				# remove unwanted fields, we really don't want to change these
				unwantedFields = ['school', 'schoolid', 'ssn']
				[newData.pop(field) for field in unwantedFields if field in newData]

				data = updateStudent(newData)

			# return success or failure message
			return HttpResponse(
				json.dumps(data),
				content_type = 'application/json'
			)

		except Exception as e:
			return HttpResponse(
				json.dumps({'status': 'error', 'msg': str(e)}),
				content_type = 'application/json'
			)
			
	else:
		return HttpResponse(
			json.dumps({'status': 'error', 'msg': 'Unable to execute request'}),
			content_type = 'application/json'
		)

@csrf_exempt
def setProfile(request, mode):
	''' add or update a profile record '''

	if request.method == 'POST':
		
		record_type = 'profile'
		str_response = request.body.decode('utf-8')
		newData = json.loads(str_response)[0]
		try:
			
			# depending on mode, get record or new record to update
			if mode == 'add':
				
				reqFields=['studentid']
				if len([field for field in reqFields if field not in newData]) > 0:
					return HttpResponse(
						json.dumps({'status': 'error', 'msg': 'required fields missing: %s' % (','.join(missing))}),
						content_type = 'application/json'
					)

				# get required items if not supplied
				if 'schoolid' not in newData or 'school_id' not in newData or 'ssn' not in newData:
					s = Student.objects.get(studentid=newData['studentid'])
					
					# get short name
					if 'schoolid' not in newData:
						newData['schoolid'] = s.schoolid
					
					# get school ID
					if 'school_id' not in newData:
						newData['school_id'] = s.school.pk

					# get ssn
					if 'ssn' not in newData:
						newData['ssn'] = s.ssn

				data = addProfile(newData)

			else:

				# check required fields for changing record
				reqFields = ['studentprofileid']
				missing = [field for field in reqFields if field not in newData]
				if len(missing) > 0:
					return HttpResponse(
						json.dumps({'status': 'error', 'msg': 'required fields missing: %s' % (','.join(missing))}),
						content_type = 'application/json'
					)

				# remove unwanted fields, we really don't want to change these
				unwantedFields = ['schoolid', 'school_id', 'ssn', 'studentid', 'programname', 'otherfee1desc', 'otherfee2desc', 'enrollmentstatus']
				[newData.pop(field) for field in unwantedFields if field in newData]

				data = updateProfile(newData)

			# return success or failure message
			return HttpResponse(
				json.dumps(data),
				content_type = 'application/json'
			)
		
		except ObjectDoesNotExist:
			
			msg = 'No %s found with ID: %s' % (record_type, newData['studentprofileid'])
			return HttpResponse(
				json.dumps({'status': 'error', 'msg': msg}),
				content_type = 'application/json'
			)
		
		except Exception as e:
			return HttpResponse(
				json.dumps({'status': 'error', 'msg': str(e)}),
				content_type = 'application/json'
			)
			
	else:
		return HttpResponse(
			json.dumps({'status': 'error', 'msg': 'Unable to execute request'}),
			content_type = 'application/json'
		)

@csrf_exempt
def setFunding(request, mode):
	''' add or update a funding record '''

	if request.method == 'POST':
		
		record_type = 'funding'
		str_response = request.body.decode('utf-8')
		newData = json.loads(str_response)[0]
		try:

			# depending on mode, get record or new record to update
			if mode == 'add':

				reqFields=['studentprofileid']
				if len([field for field in reqFields if field not in newData]) > 0:
					return HttpResponse(
						json.dumps({'status': 'error', 'msg': 'required fields missing: %s' % (','.join(missing))}),
						content_type = 'application/json'
					)

				# get required items if not supplied
				if 'schoolid' not in newData or 'school_id' not in newData or 'studentid' not in newData or 'ssn' not in newData:
					p = Studentprofile.objects.get(studentprofileid=newData['studentprofileid'])
					
					# get short name
					if 'schoolid' not in newData:
						newData['schoolid'] = p.schoolid
					
					# get school ID
					if 'school_id' not in newData:
						newData['school_id'] = p.school_id

					# get student ID
					if 'studentid' not in newData:
						newData['studentid'] = p.studentid.pk

					# get ssn
					if 'ssn' not in newData:
						newData['ssn'] = p.ssn
					
				data = addFunding(newData)

			else:

				# check required fields for changing record
				reqFields = ['studentfundingid']
				missing = [field for field in reqFields if field not in newData]
				if len(missing) > 0:
					return HttpResponse(
						json.dumps({'status': 'error', 'msg': 'required fields missing: %s' % (','.join(missing))}),
						content_type = 'application/json'
					)

				# remove unwanted fields, we really don't want to change these
				unwantedFields = ['schoolid', 'school_id', 'ssn', 'studentid', 'studentprofileid']
				[newData.pop(field) for field in unwantedFields if field in newData]

				data = updateFunding(newData)

			# return success or failure message
			return HttpResponse(
				json.dumps(data),
				content_type = 'application/json'
			)

		except ObjectDoesNotExist:
			msg = 'No %s found with ID: %s' % (record_type, newData['studentfundingid'])
			return HttpResponse(
				json.dumps({'status': 'error', 'msg': msg}),
				content_type = 'application/json'
			)

		except Exception as e:
			return HttpResponse(
				json.dumps({'status': 'error', 'msg': str(e)}),
				content_type = 'application/json'
			)
			
	else:
		return HttpResponse(
			json.dumps({'status': 'error', 'msg': 'Unable to execute request'}),
			content_type = 'application/json'
		)

@csrf_exempt
def setPayment(request, mode):
	''' add or update a payment record '''

	if request.method == 'POST':
		
		record_type = 'payment'
		str_response = request.body.decode('utf-8')
		newData = json.loads(str_response)[0]
		try:

			# check for required fields, get record or new record to update
			# if adding need profile ID, if changing need payment ID
			if mode == 'add':

				reqFields=['studentid', 'studentprofileid', 'fedpgmid', 'awardyear']
				if len([field for field in reqFields if field not in newData]) > 0:
					return HttpResponse(
						json.dumps({'status': 'error', 'msg': 'required fields missing: %s' % (','.join(missing))}),
						content_type = 'application/json'
					)

				# get required items if not supplied
				if 'schoolid' not in newData or 'school_id' not in newData or 'ssn' not in newData:
					s = Student.objects.get(studentid=newData['studentid'])
					
					# get short name
					if 'schoolid' not in newData:
						newData['schoolid'] = s.schoolid
					
					# get school ID
					if 'school_id' not in newData:
						newData['school_id'] = s.school.pk

					# get ssn
					if 'ssn' not in newData:
						newData['ssn'] = s.ssn

				data = addPayment(newData)

			else:

				# check required fields for changing record
				reqFields = ['paymentid']
				missing = [field for field in reqFields if field not in newData]
				if len(missing) > 0:
					return HttpResponse(
						json.dumps({'status': 'error', 'msg': 'required fields missing: %s' % (','.join(missing))}),
						content_type = 'application/json'
					)

				# remove unwanted fields, we really don't want to change these
				unwantedFields = ['schoolid', 'school_id', 'ssn', 'studentid']
				[newData.pop(field) for field in unwantedFields if field in newData]

				data = updatePayment(newData)

			# return success or failure message
			return HttpResponse(
				json.dumps(data),
				content_type = 'application/json'
			)
		
		except ObjectDoesNotExist:
			return HttpResponse(
				json.dumps({'status': 'error', 'msg': 'No %s found with ID: %s' % (record_type, newData['paymentid'])}),
				content_type = 'application/json'
			)

		except Exception as e:
			return HttpResponse(
				json.dumps({'status': 'error', 'msg': str(e)}),
				content_type = 'application/json'
			)

	else:
		return HttpResponse(
			json.dumps({'status': 'error', 'msg': 'Unable to execute request'}),
			content_type = 'application/json'
		)

@csrf_exempt
def generateReport(request):
	''' generate the selected report '''

	if request.method == 'POST':
		
		str_response = request.body.decode('utf-8')
		data = json.loads(str_response)
		# print(data)

		# verify valid dates
		try:
			dt = datetime.strptime(data['startdatedefault'], '%m/%d/%Y %H:%M:%S')
		except Exception as ex:
			return HttpResponse(
				json.dumps({'status': 'error', 'msg': 'Invalid Starting Date'}),
				content_type = 'application/json'
			)

		try:
			dt = datetime.strptime(data['enddatedefault'], '%m/%d/%Y %H:%M:%S')
		except Exception as ex:
			return HttpResponse(
				json.dumps({'status': 'error', 'msg': 'Invalid Ending Date'}),
				content_type = 'application/json'
			)

		# verify valid many-to-manys
		if data['statuses'] == [] or data['fedpgms'] == [] or data['studypgms'] == []:
			msg = 'Missing:'
			if data['statuses'] == []:
				msg += ' Enrollment Status(es),'
			if data['fedpgms'] == []:
				msg += ' Federal Program(s),'
			if data['studypgms'] == []:
				msg += ' Study Program(s)'
			msg = msg.rstrip(',')
			return HttpResponse(
				json.dumps({'status': 'error', 'msg': msg}),
				content_type = 'application/json'
			)

		# setup objects needed for report
		proc = ''
		s = Schoolinfo.objects.get(school_id=data['school_id'])
		headings = [s.schoolname, data['reporttitle'], '']
		parms = []

		# get stored procedure and parameters
		joinWith = ', '
		report = (data['reportname'])
		if report == 'AuditReport':
			proc = 'audit_report'
			headings[2] = 'Dates: {} - {}'.format(trimTime(data['startdatedefault']), trimTime(data['enddatedefault']))
			cols = ['Student','SSN','SSN','Awd Yr','Campus','Status','Loan Per From', 'Loan Per To','Program Name','DL Sub','DL Unsub','PELL','FSEOG','DL PLUS']
			parms = [data['schoolid'], dateToISO(data['startdatedefault'],'from'), dateToISO(data['enddatedefault'],'to'), joinIntList(data['studypgms'], joinWith), joinIntList(data['fedpgms'], joinWith), joinIntList(data['statuses'], joinWith), data['fullssndefault']]
		elif report == 'CheckRegister' or report == 'CheckRegisterByCategory' or report =='CheckRegisterByFederalProgram' or report == 'CheckRegisterByStudyProgram' or report == 'SatisfactoryAcademicProgress':
			proc = 'check_register_report'
			headings[2] = 'Dates: {} - {}'.format(trimTime(data['startdatedefault']), trimTime(data['enddatedefault']))
			cols = [{'field': 'CkDate', 'heading': 'Ck Date', 'visible': 1}, {'field': 'SchedDate', 'heading': 'Sched Date', 'visible': 1}, {'field': 'CkNo', 'heading': 'Ck No', 'visible': 1}, {'field': 'SSN', 'heading': 'SSN', 'visible': 0}, {'field': 'formattedSSN', 'heading': 'SSN', 'visible': 1}, {'field': 'StudentName', 'heading': 'Student', 'visible': 1}, {'field': 'AwardYear', 'heading': 'Awd Yr', 'visible': 1}, {'field': 'ProgramName', 'heading': 'Study Program', 'visible': 0}, {'field': 'EnrollmentStatus', 'heading': 'Status', 'visible': 0}, {'field': 'FedPgmID', 'heading': 'Fed Pgm ID', 'visible': -1}, {'field': 'FedPgmName', 'heading': 'Fed Program', 'visible': 1}, {'field': 'PayPeriod', 'heading': 'Pay Per', 'visible': 1}, {'field': 'CampusName', 'heading': 'Campus', 'visible': 0}, {'field': 'CheckTo', 'heading': 'Ck To', 'visible': 0}, {'field': 'Amount', 'heading': 'Amount', 'visible': 1}]
			parms = [data['schoolid'], data['awardyeardefault'], dateToISO(data['startdatedefault'],'from'), dateToISO(data['enddatedefault'],'to'), data['datefield']['field'], joinIntList(data['studypgms'], joinWith), joinIntList(data['fedpgms'], joinWith), joinIntList(data['statuses'], joinWith), int(data['fullssndefault']), 'paid']
		elif report == 'COA Report':
			proc = 'cost_of_attendance_report'
			parms = [data['schoolid'], data['awardyeardefault'], dateToISO(data['startdatedefault'],'from'), dateToISO(data['enddatedefault'],'to'), joinWith.join(data['studypgms']), joinWith.join(data['fedpgms']), joinWith.join(data['statuses']), data['fullssndefault']]
		elif report == 'EFC Report':
			proc = 'efc_report'
			parms = [data['schoolid'], data['awardyeardefault'], dateToISO(data['startdatedefault'],'from'), dateToISO(data['enddatedefault'],'to'), joinWith.join(data['statuses']), data['fullssndefault']]
		elif report == 'FinancialAidAwarded' or report == 'FinancialAidAwardedByStudyProgram':
			proc = 'financial_aid_awarded_report'
			parms = [data['schoolid'], data['awardyeardefault'], dateToISO(data['startdatedefault'],'from'), dateToISO(data['enddatedefault'],'to'), joinWith.join(data['studypgms']), joinWith.join(data['fedpgms']), joinWith.join(data['statuses']), data['fullssndefault']]
		elif report == 'FISAP Part VI':
			proc = 'fisap_part_vi_report'
			parms = [data['schoolid'], data['awardyeardefault'], data['fullssndefault']]
		elif report == 'Gainful Employment':
			proc = 'gainful_employment_report'
			parms = [data['schoolid'], dateToISO(data['startdatedefault'],'from'), dateToISO(data['enddatedefault'],'to'), joinWith.join(data['statuses']), data['fullssndefault']]
		elif report == 'ProspectiveStudents':
			proc = 'prospective_students_report'
			if data['campusdefault'] == 0:
				frCampus = 1
				toCampus = 99
			else:
				frCampus = data['campusdefault']
				toCampus = data['campusdefault']
			parms = [data['schoolid'], frCampus, toCampus, joinWith.join(data['studypgms']), data['fullssndefault']]
		elif report == 'StatusReport':
			proc = 'status_report'
			parms = [data['schoolid'], dateToISO(data['startdatedefault'],'from'), dateToISO(data['enddatedefault'],'to'), data['datefielddefault'], joinWith.join(data['statuses']), joinWith.join(data['studypgms']), data['fullssndefault']]

		# call stored procedure
		conn = pymysql.connect(user='root', password='GlutenFree0', db='fc5', cursorclass=pymysql.cursors.DictCursor)
		try:
			with conn.cursor() as cursor:
				cursor.callproc(proc, parms)

				# put data rows in list, fix non-serializable fields
				dataList = []
				row = cursor.fetchone()
				while row is not None:
					for fld, val in row.items():
						if isinstance(val, datetime):
							row[fld] = val.strftime('%m/%d/%Y')
						elif isinstance(val, Decimal):
							row[fld] = float(val)
					dataList.append(row)
					row = cursor.fetchone()

				# collect desired fields and customize headings
				colDefs = []
				for col in cols:
					if col['visible'] >= 0:
						colDefs.append({'field': col['heading'], 'visible': col['visible']})

				# collect actual data with desired field heading names
				dataOut = []
				for record in dataList:
					flds = {}
					for col in cols:
						if col['visible'] >= 0:
							flds[col['heading']] = record[col['field']]
					dataOut.append(flds)

					# print(record)
					# print(flds)

# here is a dataList item
#[{'EnrollmentStatus': 'LOA', 'CheckTo': 'School', 'SchedDate': '07/15/2015', 'SSN': '559550526', 'StudentName': 'Saitta, Erin M', 'Amount': 1732.0, 'CkNo': 71515, 'AwardYear': '1516', 'formattedSSN': 'xxxx-xx-0526', 'FedPgmName': 'DL Subsidized', 'PayPeriod': '1', 'CampusName': 'Main', 'ProgramName': 'Diagnostic Medical Sonography I', 'FedPgmID': 8, 'CkDate': '07/15/2015'}, 

# here are cols I want. note: -1= don't include, 0=include but don't show, 1=include and show.
# cols = [{'field': 'CkDate', 'heading': 'Ck Date', 'visible': 1}, {'field': 'SchedDate', 'heading': 'Sched Date', 'visible': 1}, {'field': 'CkNo', 'heading': 'Ck No', 'visible': 1}, {'field': 'SSN', 'heading': 'SSN', 'visible': 0}, {'field': 'formattedSSN', 'heading': 'SSN', 'visible': 1}, {'field': 'StudentName', 'heading': 'Student', 'visible': 1}, {'field': 'AwardYear', 'heading': 'Awd Yr', 'visible': 1}, {'field': 'ProgramName', 'heading': 'Study Program', 'visible': 0}, {'field': 'EnrollmentStatus', 'heading': 'Status', 'visible': 0}, {'field': 'FedPgmID', 'heading': 'Fed Pgm ID', 'visible': 0}, {'field': 'FedPgmName', 'heading': 'Fed Program', 'visible': 1}, {'field': 'PayPeriod', 'heading': 'Pay Per', 'visible': 1}, {'field': 'CampusName', 'heading': 'Campus', 'visible': 0}, {'field': 'CheckTo', 'heading': 'Ck To', 'visible': 0}, {'field': 'Amount', 'heading': 'Amount', 'visible': 1}]

# here is how data has to look
# [
#     {
#         "name": "Ethel Price",
#         "gender": "female",
#         "company": "Enersol"
#     },

# here is how we show or hide fields
        # columnDefs: [
        #     { field: 'name' },
        #     { field: 'gender', visible: false},
        #     { field: 'company' }
        # ],




		finally:
			cursor = None
			conn.close
		
		
		
		
		# conn = mysql.connector.connect(user='root', database='fc5', password='GlutenFree0')
		# cursor = conn.cursor()
		# cursor.callproc(proc, parms)
		# print(cursor.description)
		# print(cursor.column_names)
		# for result in cursor.stored_results():
		# 	print(result.fetchall())
		# # put results in json list
		# dataOut = []
		# for result in cursor.stored_results():
		# 	row = result.fetchone()
		# 	while row is not None:
		# 		recOut = {}
		# 		for fld in range(0, len(row)):
		# 			val = row[fld]
		# 			if isinstance(val, datetime):
		# 				val = row[fld].strftime('%m/%d/%Y')
		# 			elif isinstance(val, Decimal):
		# 				val = float(row[fld])
		# 			recOut[cols[fld]] = val
		# 		#rowOut = record_to_dict(recOut)
		# 		dataOut.append(recOut)
		# 		row = result.fetchone()

		# build json response
		data = {'status': 'success', 'headings': headings, 'columns': colDefs, 'data': dataOut}

		# #df = pd.read_json(myData, orient='records')
		# df = json_normalize(myData)#.T
		# # gb = df.groupby(level = 0, axis = 1).sum().fillna(0)
		# print(df)

		# gb = df.groupby('Fed Program').agg({'Fed Program':'size','Amount':'sum'})
		# gb.columns = ['Count', 'Total']
		# print(gb)



		# return success or failure message
		return HttpResponse(
			json.dumps(data),
			content_type = 'application/json'
		)

	else:
		return HttpResponse(
			json.dumps({'status': 'error', 'msg': 'Unable to execute request'}),
			content_type = 'application/json'
		)
