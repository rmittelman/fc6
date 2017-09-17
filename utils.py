#!/Users/ron/projects/fedconnect/venv/bin/python
from datetime import datetime, timedelta
import calendar
import os, sys
import json
import django
from django.forms.models import model_to_dict

sys.path.append('/Users/ron/projects/fedconnect/fc6/')
os.environ['DJANGO_SETTINGS_MODULE'] = 'fc6.settings'
django.setup()

from fc6.models import *

def dateToISO(inputDate, from_or_to='from'):
    try:
        if len(inputDate) < 12:
            inputDate = inputDate.strip()
            if from_or_to == 'from':
                inputDate += ' 00:00:00'
            elif from_or_to == 'to':
                inputDate += ' 23:59:59'

        aDate = datetime.strptime(inputDate, '%m/%d/%Y %H:%M:%S')
    except Exception as e:
        if from_or_to == 'from':
            aDate = datetime.strptime('01/01/1980', '%m/%d/%Y %H:%M:%S')
        elif from_or_to == 'to':
            aDate = datetime.strptime('12/31/2099', '%m/%d/%Y %H:%M:%S')
        else:
            return ''

    return aDate.strftime('%Y-%m-%d %H:%M:%S')

def joinIntList(intList, joinWith):
    try:
        return joinWith.join(map(str, intList))
    except Exception as ex:
        return ''

def trimTime(inputDateTime):
    return datetime.strptime(inputDateTime, '%m/%d/%Y %H:%M:%S').strftime('%m/%d/%Y')

def fiscalYearList(blankItemAtTop=False, yearsToList=5, digits2or4=2, currentYearPosition=2):
    """Returns list of fiscal years in descending order.

    :param blankItemAtTop: Return a blank item at the top of the list so user can choose "none".
    :param yearsToList: How many years to return in the list (not including blank item at top).
    :param digits2or4: Display as 16-17 if 2, or 2016-2017 if 4.
    :param currentYearPosition: 0-based index where current year should appear in the list.
    :return: An array of {yyyy:yy-yy} (or {yyyyyyyy:yyyy-yyyy}) , or '' if incorrect parms supplied.
    """

    # get fy start
    try:
        fyStartMonth = int(Appsettings.objects.get(setting='FiscalYearStartMonth').value)
    except:
        fyStartMonth = 0

    # continue if valid parms sent
    if (fyStartMonth >= 1 and fyStartMonth <= 12) and (digits2or4 == 2 or digits2or4 == 4) and currentYearPosition <= yearsToList:

        # get the beginning and ending year for current date
        _today = datetime.today()
        if _today.month < fyStartMonth:
            startYear = _today.year - 1
            endYear = _today.year
        else:
            startYear = _today.year
            endYear = _today.year + 1

        # get starting fiscal year based on currentYearPosition
        startYear = startYear + currentYearPosition - 1
        endYear = endYear + currentYearPosition - 1

        # prepare list for adding years, add extra blank item at top if wanted
        fyList = []
        if blankItemAtTop:
            fyList.append({'value': '', 'display': ''})
        

        # loop thru yearsToList and add the fiscal years to the list
        for x in range(0, yearsToList):
            fyVal = '{0}{1}'.format('{}'.format(startYear - x)[-digits2or4:], '{}'.format(endYear - x)[-digits2or4:])
            fyDisplay = '{0}-{1}'.format('{}'.format(startYear - x)[-digits2or4:], '{}'.format(endYear - x)[-digits2or4:])
            #fyList.append(fyVal)
            fyList.append({'value': fyVal, 'display': fyDisplay})
        return fyList

    else:
        return ''

def codeToDate(whichPeriods):
    """Converts tuple of date codes to actual dates.

    :param whichPeriods: Tuple of date codes (begin, end) each one being: ThisWeek, ThisMonth, ThisYear, ThisFiscalYear (or Last... or Next...).
    :return: Tuple of firstDate, lastDate of desired period.
    """
    _start = 'None'
    _end = 'None'
    
    # get fy start
    try:
        fyStartMonth = int(Appsettings.objects.get(setting='FiscalYearStartMonth').value)
    except:
        fyStartMonth = 0

    # get today's date without time
    _today = datetime.today().replace(hour=0, minute=0, second=0, microsecond=0)

    # loop thru the 2 dates
    for i in range(0, 2):

        period = whichPeriods[i]
        if period != 'None':

            if period.endswith('Week'):

                # get first day of week, then add / subtract a week if needed
                theDate = _today - timedelta(days = _today.weekday() + 1) # subtract extra day so week starts Sunday, not default Monday
                if period.startswith("Last"):
                    theDate -= timedelta(weeks = 1)
                elif period.startswith("Next"):
                    theDate += timedelta(weeks = 1)
                
                # get last day of week if second date
                if i == 1:
                    theDate = (theDate + timedelta(days=6)).replace(hour=23, minute=59, second=59)

                if i == 0:
                    _start = theDate
                else:
                    _end = theDate

            elif period.endswith("Month"):

                # get 15th of month, add / subtract a month if needed, then get first day of month
                _15th = datetime(_today.year, _today.month, 15)
                if period.startswith("Last"):
                    _15th -= timedelta(days = 30)
                elif period.startswith("Next"):
                    _15th += timedelta(days = 30)
                theDate = datetime(_15th.year, _15th.month, 1)

                # get last day of month if second date
                if i == 1:
                    _, num_days = calendar.monthrange(_15th.year, _15th.month)
                    theDate = datetime(_15th.year, _15th.month, num_days).replace(hour=23, minute=59, second=59)

                if i == 0:
                    _start = theDate
                else:
                    _end = theDate

            elif (period.endswith("FiscalYear")) and (fyStartMonth > 1):

                # first figure out the starting fiscal year
                fy = _today.year - 1 if _today.month < fyStartMonth else _today.year

                # get first day of fiscal year, add / subtract a year if needed
                theDate = datetime(fy, fyStartMonth, 1)
                if period.startswith("Last"):
                    theDate = datetime(theDate.year - 1, theDate.month, 1)
                elif period.startswith("Next"):
                    theDate = datetime(theDate.year + 1, theDate.month, 1)

                # get last day of fiscal year if second date
                if i == 1:
                    _, num_days = calendar.monthrange(theDate.year, fyStartMonth - 1)
                    theDate = datetime(theDate.year + 1, fyStartMonth - 1, num_days).replace(hour=23, minute=59, second=59)

                if i == 0:
                    _start = theDate
                else:
                    _end = theDate

            elif (period.endswith("Year")) or (fyStartMonth == 1):

                # get first day of year, then add / subtract a year if needed
                theDate = datetime(_today.year, 1, 1)
                if period.startswith("Last"):
                    theDate = datetime(_today.year - 1, 1, 1)
                elif period.startswith("Next"):
                    theDate = datetime(_today.year + 1, 1, 1)
                
                # get last day of year if second date
                if i == 1:
                    theDate = datetime(theDate.year, 12, 31).replace(hour=23, minute=59, second=59)

                if i == 0:
                    _start = theDate
                else:
                    _end = theDate

    return (_start, _end)

def record_to_dict(record):
    ''' change record object to serializable dictionary (fix datetimes, foreign keys, etc.) '''

    fields = record._meta._get_fields(forward=True, reverse=False)
    recordDict = model_to_dict(record)
    for fld in fields:
        ftype = fld.get_internal_type()
        fname = fld.name
        try:

            if recordDict[fname] == None:
                recordDict[fname] = ''
            elif ftype == 'BooleanField':
                recordDict[fname] = int(recordDict[fname])
            # elif recordDict[fname] == True:
            #     recordDict[fname] = 1
            # elif recordDict[fname] == False:
            #     recordDict[fname] = 0
            elif ftype == 'DateTimeField':
                recordDict[fname] = recordDict[fname].strftime('%m/%d/%Y %H:%M:%S')
            elif ftype == 'DateField':
                recordDict[fname] = recordDict[fname].strftime('%m/%d/%Y')
            elif ftype == 'TimeField':
                recordDict[fname] = recordDict[fname].strftime('%H:%M:%S')
            elif ftype == 'DecimalField':
                recordDict[fname] = float(recordDict[fname]) # str(recordDict[fname])
            elif ftype == 'ManyToManyField':
                pkList = [i.pk for i in recordDict[fname]]
                recordDict[fname] = pkList
        except AttributeError:
            pass

    return recordDict

def dict_to_record(mode, fldVals, currentRecord):
	''' fill record from contents of dictionary, field-for-field (ignore AutoField) '''

	# iterate fldVals dictionary
	for fldName, fldVal in fldVals.items():
		
		try:

			fld = currentRecord._meta.get_field(fldName)
			ftype = fld.get_internal_type()

			if ftype == 'AutoField':
				pass # don't want to update this

			elif ftype == 'ForeignKey':
				parent_model = fld.rel.to
				parent_object = parent_model.objects.get(pk=fldVal)
				setattr(currentRecord, fldName, parent_object)

			elif ftype == 'IntegerField':
				setattr(currentRecord, fldName, int(fldVal))

			elif ftype == 'Decimalfield':
				setattr(currentRecord, fldName, Decimal(fldVal))

			elif ftype == 'DateTimeField':
				setattr(currentRecord, fldName, datetime.strptime(fldVal, '%m/%d/%Y %H:%M:%S'))

			elif ftype == 'DateField':
				setattr(currentRecord, fldName, datetime.strptime(fldVal, '%m/%d/%Y'))

			elif ftype == 'TimeField':
				setattr(currentRecord, fldName, datetime.strptime(fldVal, '%H:%M:%S'))

			elif ftype == 'FloatField':
				setattr(currentRecord, fldName, float(fldVal))

			else:
				setattr(currentRecord, fldName, fldVal)

		except FieldDoesNotExist:
			raise FieldDoesNotExist('Field \'%s\' does not exist' %(fldName))

		except TypeError:
			print('type err')
			raise

		except ValueError:
			raise ValueError('Invalid value for %s: %s' % (fname, newValue))

		except ObjectDoesNotExist:
			if ftype == 'ForeignKey':
				msg = 'Could not find %s with ID %s' % (fldName, fldVal)
			else:
				msg = 'error field %s, val %s' % (fldName, fldVal)
			raise ObjectDoesNotExist(msg)

		except AttributeError:
			print('error')
		
		except Exception as e:
			print(e.args)
			print(type(e))
	return currentRecord

if __name__ == '__main__':
    #from fc6.models import *
    #x=Appsettings.objects.all()
    #print(x[0])

    qs = Usersettings.objects.all()
    us = list(qs)
    print(json.dumps(us))
    quit()
    

    # convert date codes to dates
    qs = Reports.objects.all()
    reports = list(qs)
    print(json.dumps(reports))
    quit()

    try:
        for report in reports:
            realDates = codeToDate((report.startdatedefault, report.enddatedefault))
            report.startdatedefault = realDates[0]
            report.enddatedefault = realDates[1]
    except Exception as e:
        print(str(e))
        print(report.reportname)
        print(realDates)
        quit()

    for report in reports:
        print('%s: %s, %s' % (report.reportname, report.startdatedefault, report.enddatedefault))

    quit()



    print("\nfiscalYearList:\n")
    print(fiscalYearList(True,7,2,3))
    print("\ncodeToDate:\n")
    print("ThisWeek:", codeToDate(('ThisWeek', 'ThisWeek')))
    print("LastWeek:", codeToDate(('LastWeek', 'LastWeek')))
    print("NextWeek:", codeToDate(('NextWeek', 'NextWeek')))
    print("ThisMonth:", codeToDate(('ThisMonth', 'ThisMonth')))
    print("LastMonth:", codeToDate(('LastMonth', 'LastMonth')))
    print("NextMonth:", codeToDate(('NextMonth', 'NextMonth')))
    print("ThisFiscalYear:", codeToDate(('ThisFiscalYear', 'ThisFiscalYear')))
    print("LastFiscalYear:", codeToDate(('LastFiscalYear', 'LastFiscalYear')))
    print("NextFiscalYear:", codeToDate(('NextFiscalYear', 'NextFiscalYear')))
    print("ThisYear:", codeToDate(('ThisYear', 'ThisYear')))
    print("LastYear:", codeToDate(('LastYear', 'LastYear')))
    print("NextYear:", codeToDate(('NextYear', 'NextYear')))
    print("")
    quit()



    us = list(Student.objects.all()[:5])
    for s in us:
        fields = s.__dict__
        for k,v in fields.items():
            if k != '_state':
                print('key: %s, val: %s' %(k,v))
        
        print('\n')
