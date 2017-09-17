# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User

HOUSING_TYPES = (
(1, 'On Campus'),
(2, 'With Parent'),
(3, 'Off Campus'),
)

REPORT_DATE_TYPES = (
('None', 'None'),
('ThisWeek', 'This Week'),
('LastWeek', 'Last Week'),
('NextWeek', 'Next Week'),
('ThisMonth', 'This Month'),
('LastMonth', 'Last Month'),
('NextMonth', 'Next Month'),
('ThisYear', 'This Year'),
('LastYear', 'Last Year'),
('NextYear', 'Next Year'),
('ThisFiscalYear', 'This Fiscal Year'),
('LastFiscalYear', 'Last Fiscal Year'),
('NextFiscalYear', 'Next Fiscal Year')
)

HOURS_TYPES = (
	(1, 'Credit'),
	(2, 'Clock')
)
AWARD_YEARS = (
('None', 'None'),
('Current', 'Current Award Year'),
('Prior', 'Prior Award Year'),
)

def limit_school_choices():
	return {'school':1}

class Allowances(models.Model):
	fiscalyear = models.CharField(db_column='FiscalYear', primary_key=True, max_length=4)  # Field name made lowercase.
	on_roomboard = models.DecimalField(db_column='ON_RoomBoard', max_digits=8, decimal_places=2, blank=True, null=True, verbose_name='On-Campus Room & Board')  # Field name made lowercase.
	on_transportation = models.DecimalField(db_column='ON_Transportation', max_digits=8, decimal_places=2, blank=True, null=True, verbose_name='On-Campus Transportation')  # Field name made lowercase.
	on_personal = models.DecimalField(db_column='ON_Personal', max_digits=8, decimal_places=2, blank=True, null=True, verbose_name='On-Campus Personal')  # Field name made lowercase.
	wp_roomboard = models.DecimalField(db_column='WP_RoomBoard', max_digits=8, decimal_places=2, blank=True, null=True, verbose_name='With Parent Room & Board')  # Field name made lowercase.
	wp_transportation = models.DecimalField(db_column='WP_Transportation', max_digits=8, decimal_places=2, blank=True, null=True, verbose_name='With Parent Transportation')  # Field name made lowercase.
	wp_personal = models.DecimalField(db_column='WP_Personal', max_digits=8, decimal_places=2, blank=True, null=True, verbose_name='With Parent Personal')  # Field name made lowercase.
	off_roomboard = models.DecimalField(db_column='OFF_RoomBoard', max_digits=8, decimal_places=2, blank=True, null=True, verbose_name='Off-Campus Room & Board')  # Field name made lowercase.
	off_transportation = models.DecimalField(db_column='OFF_Transportation', max_digits=8, decimal_places=2, blank=True, null=True, verbose_name='Off-Campus Transportation')  # Field name made lowercase.
	off_personal = models.DecimalField(db_column='OFF_Personal', max_digits=8, decimal_places=2, blank=True, null=True, verbose_name='Off-Campus Transportation')  # Field name made lowercase.

	def __str__(self):
		return "{}-{}".format( self.fiscalyear[:2], self.fiscalyear[2:])

	class Meta:
		db_table = 'Allowances'
		app_label = 'fc6'
		verbose_name = 'Allowance'
	

class Awardletters(models.Model):
	awardletterid = models.CharField(db_column='AwardLetterID', primary_key=True, max_length=10, verbose_name='ID')  # Field name made lowercase.
	awardlettername = models.CharField(db_column='AwardLetterName', max_length=50, blank=True, null=True, verbose_name='Name')  # Field name made lowercase.
	awardletterdoc = models.CharField(db_column='AwardLetterDoc', max_length=100, blank=True, null=True, verbose_name='Document Name')  # Field name made lowercase.
	paragraph1 = models.TextField(db_column='Paragraph1', blank=True, null=True)  # Field name made lowercase.
	p1signaturerelated = models.BooleanField(db_column='P1SignatureRelated', default=0, verbose_name='Signature Related')  # Field name made lowercase.
	paragraph2 = models.TextField(db_column='Paragraph2', blank=True, null=True)  # Field name made lowercase.
	p2signaturerelated = models.BooleanField(db_column='P2SignatureRelated', default=0, verbose_name='Signature Related')  # Field name made lowercase.
	paragraph3 = models.TextField(db_column='Paragraph3', blank=True, null=True)  # Field name made lowercase.
	p3signaturerelated = models.BooleanField(db_column='P3SignatureRelated', default=0, verbose_name='Signature Related')  # Field name made lowercase.
	paragraph4 = models.TextField(db_column='Paragraph4', blank=True, null=True)  # Field name made lowercase.
	p4signaturerelated = models.BooleanField(db_column='P4SignatureRelated', default=0, verbose_name='Signature Related')  # Field name made lowercase.
	paragraph5 = models.TextField(db_column='Paragraph5', blank=True, null=True)  # Field name made lowercase.
	p5signaturerelated = models.BooleanField(db_column='P5SignatureRelated', default=0, verbose_name='Signature Related')  # Field name made lowercase.
	paragraph6 = models.TextField(db_column='Paragraph6', blank=True, null=True)  # Field name made lowercase.
	p6signaturerelated = models.BooleanField(db_column='P6SignatureRelated', default=0, verbose_name='Signature Related')  # Field name made lowercase.
	paragraph7 = models.TextField(db_column='Paragraph7', blank=True, null=True)  # Field name made lowercase.
	p7signaturerelated = models.BooleanField(db_column='P7SignatureRelated', default=0, verbose_name='Signature Related')  # Field name made lowercase.
	paragraph8 = models.TextField(db_column='Paragraph8', blank=True, null=True)  # Field name made lowercase.
	p8signaturerelated = models.BooleanField(db_column='P8SignatureRelated', default=0, verbose_name='Signature Related')  # Field name made lowercase.

	def __str__(self):
		return self.awardlettername
		
	class Meta:
		db_table = 'AwardLetters'
		app_label = 'fc6'
		verbose_name = 'Award Letter'

		
class Checkto(models.Model):
	cktoid = models.IntegerField(db_column='CkToID', primary_key=True, verbose_name='ID')  # Field name made lowercase.
	checkto = models.CharField(db_column='CheckTo', max_length=15, blank=True, null=True, verbose_name='Send Check To')  # Field name made lowercase.

	def __str__(self):
		return '{} --> {}'.format( self.cktoid, self.checkto)

	class Meta:
		db_table = 'CheckTo'
		app_label = 'fc6'
		verbose_name = 'Check To'
		ordering = ['cktoid']


class Enrollmentstatus(models.Model):
	enrollmentstatusid = models.IntegerField(db_column='EnrollmentStatusID', primary_key=True, verbose_name='ID')  # Field name made lowercase.
	enrollmentstatus = models.CharField(db_column='EnrollmentStatus', max_length=20, blank=True, null=True, verbose_name='Enrollment Status')  # Field name made lowercase.

	def __str__(self):
		return '{} '.format( self.enrollmentstatus)

	class Meta:
		db_table = 'EnrollmentStatus'
		app_label = 'fc6'
		verbose_name = 'Enrollment Status'
		verbose_name_plural = 'Enrollment Statuses'
		ordering = ['enrollmentstatusid']


class Federalprograms(models.Model):
	fedpgmid = models.IntegerField(db_column='FedPgmID', primary_key=True, verbose_name='ID')  # Field name made lowercase.
	fedpgmname = models.CharField(db_column='FedPgmName', max_length=50, verbose_name='Name')  # Field name made lowercase.
	active = models.BooleanField(db_column='Active', default=0, verbose_name='Active Program')  # Field name made lowercase.
	seq = models.IntegerField(db_column='Seq', blank=True, null=True, default=0)  # Field name made lowercase.
	loanfee = models.DecimalField(db_column='LoanFee', max_digits=10, decimal_places=5, default=0.00000, verbose_name='Loan Fee')  # Field name made lowercase.
	titleiv = models.BooleanField(db_column='TitleIV', default=0, verbose_name='Title IV')  # Field name made lowercase.
	ffelp = models.BooleanField(db_column='FFELP', default=0, verbose_name='FFELP')  # Field name made lowercase.
	fawostafford = models.BooleanField(db_column='FAwoStafford', default=0, verbose_name='FA w/o Stafford')  # Field name made lowercase.
	fawstafford = models.BooleanField(db_column='FAwStafford', default=0, verbose_name='FA w/ Stafford')  # Field name made lowercase.

	def __str__(self):
		return '{}'.format( self.fedpgmname)

	class Meta:
		db_table = 'FederalPrograms'
		app_label = 'fc6'
		verbose_name = 'Federal Program'
		ordering = ['seq']
		

class FisapAwardGroups(models.Model):
	awardgroupid = models.AutoField(db_column='AwardGroupID', primary_key=True)  # Field name made lowercase.
	reporttype = models.IntegerField(db_column='ReportType')  # Field name made lowercase.
	isir_model = models.CharField(db_column='ISIR_Model', max_length=1)  # Field name made lowercase.
	fisap_below = models.IntegerField(db_column='FISAP_Below')  # Field name made lowercase.
	group_no = models.IntegerField(db_column='Group_No')  # Field name made lowercase.
	group_desc = models.CharField(db_column='Group_Desc', max_length=30, blank=True, null=True, verbose_name='Group Description')  # Field name made lowercase.

	def __str__(self):
		return '{} --> {}  {}'.format( self.reporttype, self.isir_model, self.fisap_below)

	class Meta:
		db_table = 'FISAP_Award_Groups'
		app_label = 'fc6'
		unique_together = (('reporttype', 'isir_model', 'fisap_below', 'group_no'),)
		verbose_name = 'FISAP Award Group'
		ordering = ['reporttype', 'isir_model', 'fisap_below']
		

class Isirirsreqtypes(models.Model):
	requesttypeid = models.CharField(db_column='RequestTypeID', primary_key=True, max_length=2, verbose_name='ID')  # Field name made lowercase.
	description = models.CharField(db_column='Description', max_length=75, blank=True, null=True)  # Field name made lowercase.

	def __str__(self):
		return '{} --> {}'.format( self.requesttypeid, self.description)

	class Meta:
		db_table = 'IsirIRSReqTypes'
		app_label = 'fc6'
		verbose_name = 'ISIR IRS Req Type'
		ordering = ['requesttypeid']
		

class Isirverificationtype(models.Model):
	verificationtypeid = models.CharField(db_column='VerificationTypeID', primary_key=True, max_length=2, verbose_name='ID')  # Field name made lowercase.
	description = models.CharField(db_column='Description', max_length=35, blank=True, null=True)  # Field name made lowercase.

	def __str__(self):
		return '{} --> {}'.format( self.verificationtypeid, self.description)

	class Meta:
		db_table = 'IsirVerificationType'
		app_label = 'fc6'
		verbose_name = 'ISIR Verification Type'
		ordering = ['verificationtypeid']
		

class Livingexpenses(models.Model):
	livingexpenseid = models.AutoField(db_column='LivingExpenseID', primary_key=True)  # Field name made lowercase.
	fiscalyear = models.CharField(db_column='FiscalYear', max_length=4, verbose_name='Award Year')  # Field name made lowercase.
	housingtypeid = models.IntegerField(db_column='HousingTypeID', choices = HOUSING_TYPES, verbose_name='Housing Type')  # Field name made lowercase.
	foodandhousing = models.DecimalField(db_column='FoodAndHousing', max_digits=8, decimal_places=2, blank=True, null=True, verbose_name='Food & Housing Expense')  # Field name made lowercase.
	transportation = models.DecimalField(db_column='Transportation', max_digits=8, decimal_places=2, blank=True, null=True, verbose_name='Transportation Expense')  # Field name made lowercase.
	personal = models.DecimalField(db_column='Personal', max_digits=8, decimal_places=2, blank=True, null=True, verbose_name='Personal Expense')  # Field name made lowercase.

	def __str__(self):
		return '{}-{} --> {}'.format( self.fiscalyear[:2], self.fiscalyear[2:], self.get_housingtypeid_display())

	class Meta:
		db_table = 'LivingExpenses'
		app_label = 'fc6'
		unique_together = (('fiscalyear', 'housingtypeid'),)
		verbose_name = 'Living Expense'
		ordering = ['-fiscalyear']
		

class Pellcontrol(models.Model):
	awardyear = models.CharField(db_column='AwardYear', primary_key=True, max_length=4, verbose_name='Award Year')  # Field name made lowercase.
	minclockhours = models.IntegerField(db_column='MinClockHours', blank=True, null=True, verbose_name='Min Clock Hours')  # Field name made lowercase.
	mincredithours = models.IntegerField(db_column='MinCreditHours', blank=True, null=True, verbose_name='Min Credit Hours')  # Field name made lowercase.
	efc0 = models.IntegerField(db_column='EFC0', blank=True, null=True, verbose_name='EFC Level 0')  # Field name made lowercase.
	grant0 = models.IntegerField(db_column='Grant0', blank=True, null=True, verbose_name='Grant Level 0')  # Field name made lowercase.
	efc1 = models.IntegerField(db_column='EFC1', blank=True, null=True, verbose_name='EFC Level 1')  # Field name made lowercase.
	grant1 = models.IntegerField(db_column='Grant1', blank=True, null=True, verbose_name='Grant Level 1')  # Field name made lowercase.
	efc2 = models.IntegerField(db_column='EFC2', blank=True, null=True, verbose_name='EFC Level 2')  # Field name made lowercase.
	grant2 = models.IntegerField(db_column='Grant2', blank=True, null=True, verbose_name='Grant Level 2')  # Field name made lowercase.
	efc3 = models.IntegerField(db_column='EFC3', blank=True, null=True, verbose_name='EFC Level 3')  # Field name made lowercase.
	grant3 = models.IntegerField(db_column='Grant3', blank=True, null=True, verbose_name='Grant Level 3')  # Field name made lowercase.
	efc4 = models.IntegerField(db_column='EFC4', blank=True, null=True, verbose_name='EFC Level 4')  # Field name made lowercase.
	grant4 = models.IntegerField(db_column='Grant4', blank=True, null=True, verbose_name='Grant Level 4')  # Field name made lowercase.
	efc5 = models.IntegerField(db_column='EFC5', blank=True, null=True, verbose_name='EFC Level 5')  # Field name made lowercase.
	grant5 = models.IntegerField(db_column='Grant5', blank=True, null=True, verbose_name='Grant Level 5')  # Field name made lowercase.
	efc6 = models.IntegerField(db_column='EFC6', blank=True, null=True, verbose_name='EFC Level 6')  # Field name made lowercase.
	grant6 = models.IntegerField(db_column='Grant6', blank=True, null=True, verbose_name='Grant Level 6')  # Field name made lowercase.
	efc7 = models.IntegerField(db_column='EFC7', blank=True, null=True, verbose_name='EFC Level 7')  # Field name made lowercase.
	grant7 = models.IntegerField(db_column='Grant7', blank=True, null=True, verbose_name='Grant Level 7')  # Field name made lowercase.
	efc8 = models.IntegerField(db_column='EFC8', blank=True, null=True, verbose_name='EFC Level 8')  # Field name made lowercase.
	grant8 = models.IntegerField(db_column='Grant8', blank=True, null=True, verbose_name='Grant Level 8')  # Field name made lowercase.
	efc9 = models.IntegerField(db_column='EFC9', blank=True, null=True, verbose_name='EFC Level 9')  # Field name made lowercase.
	grant9 = models.IntegerField(db_column='Grant9', blank=True, null=True, verbose_name='Grant Level 9')  # Field name made lowercase.
	efc10 = models.IntegerField(db_column='EFC10', blank=True, null=True, verbose_name='EFC Level 10')  # Field name made lowercase.
	grant10 = models.IntegerField(db_column='Grant10', blank=True, null=True, verbose_name='Grant Level 10')  # Field name made lowercase.
	efc11 = models.IntegerField(db_column='EFC11', blank=True, null=True, verbose_name='EFC Level 11')  # Field name made lowercase.
	grant11 = models.IntegerField(db_column='Grant11', blank=True, null=True, verbose_name='Grant Level 11')  # Field name made lowercase.
	efc12 = models.IntegerField(db_column='EFC12', blank=True, null=True, verbose_name='EFC Level 12')  # Field name made lowercase.
	grant12 = models.IntegerField(db_column='Grant12', blank=True, null=True, verbose_name='Grant Level 12')  # Field name made lowercase.
	efc13 = models.IntegerField(db_column='EFC13', blank=True, null=True, verbose_name='EFC Level 13')  # Field name made lowercase.
	grant13 = models.IntegerField(db_column='Grant13', blank=True, null=True, verbose_name='Grant Level 13')  # Field name made lowercase.
	efc14 = models.IntegerField(db_column='EFC14', blank=True, null=True, verbose_name='EFC Level 14')  # Field name made lowercase.
	grant14 = models.IntegerField(db_column='Grant14', blank=True, null=True, verbose_name='Grant Level 14')  # Field name made lowercase.
	efc15 = models.IntegerField(db_column='EFC15', blank=True, null=True, verbose_name='EFC Level 15')  # Field name made lowercase.
	grant15 = models.IntegerField(db_column='Grant15', blank=True, null=True, verbose_name='Grant Level 15')  # Field name made lowercase.
	efc16 = models.IntegerField(db_column='EFC16', blank=True, null=True, verbose_name='EFC Level 16')  # Field name made lowercase.
	grant16 = models.IntegerField(db_column='Grant16', blank=True, null=True, verbose_name='Grant Level 16')  # Field name made lowercase.
	efc17 = models.IntegerField(db_column='EFC17', blank=True, null=True, verbose_name='EFC Level 17')  # Field name made lowercase.
	grant17 = models.IntegerField(db_column='Grant17', blank=True, null=True, verbose_name='Grant Level 17')  # Field name made lowercase.
	efc18 = models.IntegerField(db_column='EFC18', blank=True, null=True, verbose_name='EFC Level 18')  # Field name made lowercase.
	grant18 = models.IntegerField(db_column='Grant18', blank=True, null=True, verbose_name='Grant Level 18')  # Field name made lowercase.
	efc19 = models.IntegerField(db_column='EFC19', blank=True, null=True, verbose_name='EFC Level 19')  # Field name made lowercase.
	grant19 = models.IntegerField(db_column='Grant19', blank=True, null=True, verbose_name='Grant Level 19')  # Field name made lowercase.
	efc20 = models.IntegerField(db_column='EFC20', blank=True, null=True, verbose_name='EFC Level 20')  # Field name made lowercase.
	grant20 = models.IntegerField(db_column='Grant20', blank=True, null=True, verbose_name='Grant Level 20')  # Field name made lowercase.
	efc21 = models.IntegerField(db_column='EFC21', blank=True, null=True, verbose_name='EFC Level 21')  # Field name made lowercase.
	grant21 = models.IntegerField(db_column='Grant21', blank=True, null=True, verbose_name='Grant Level 21')  # Field name made lowercase.
	efc22 = models.IntegerField(db_column='EFC22', blank=True, null=True, verbose_name='EFC Level 22')  # Field name made lowercase.
	grant22 = models.IntegerField(db_column='Grant22', blank=True, null=True, verbose_name='Grant Level 22')  # Field name made lowercase.
	efc23 = models.IntegerField(db_column='EFC23', blank=True, null=True, verbose_name='EFC Level 23')  # Field name made lowercase.
	grant23 = models.IntegerField(db_column='Grant23', blank=True, null=True, verbose_name='Grant Level 23')  # Field name made lowercase.
	efc24 = models.IntegerField(db_column='EFC24', blank=True, null=True, verbose_name='EFC Level 24')  # Field name made lowercase.
	grant24 = models.IntegerField(db_column='Grant24', blank=True, null=True, verbose_name='Grant Level 24')  # Field name made lowercase.
	efc25 = models.IntegerField(db_column='EFC25', blank=True, null=True, verbose_name='EFC Level 25')  # Field name made lowercase.
	grant25 = models.IntegerField(db_column='Grant25', blank=True, null=True, verbose_name='Grant Level 25')  # Field name made lowercase.
	efc26 = models.IntegerField(db_column='EFC26', blank=True, null=True, verbose_name='EFC Level 26')  # Field name made lowercase.
	grant26 = models.IntegerField(db_column='Grant26', blank=True, null=True, verbose_name='Grant Level 26')  # Field name made lowercase.
	efc27 = models.IntegerField(db_column='EFC27', blank=True, null=True, verbose_name='EFC Level 27')  # Field name made lowercase.
	grant27 = models.IntegerField(db_column='Grant27', blank=True, null=True, verbose_name='Grant Level 27')  # Field name made lowercase.
	efc28 = models.IntegerField(db_column='EFC28', blank=True, null=True, verbose_name='EFC Level 28')  # Field name made lowercase.
	grant28 = models.IntegerField(db_column='Grant28', blank=True, null=True, verbose_name='Grant Level 28')  # Field name made lowercase.
	efc29 = models.IntegerField(db_column='EFC29', blank=True, null=True, verbose_name='EFC Level 29')  # Field name made lowercase.
	grant29 = models.IntegerField(db_column='Grant29', blank=True, null=True, verbose_name='Grant Level 29')  # Field name made lowercase.
	efc30 = models.IntegerField(db_column='EFC30', blank=True, null=True, verbose_name='EFC Level 30')  # Field name made lowercase.
	grant30 = models.IntegerField(db_column='Grant30', blank=True, null=True, verbose_name='Grant Level 30')  # Field name made lowercase.
	efc31 = models.IntegerField(db_column='EFC31', blank=True, null=True, verbose_name='EFC Level 31')  # Field name made lowercase.
	grant31 = models.IntegerField(db_column='Grant31', blank=True, null=True, verbose_name='Grant Level 31')  # Field name made lowercase.
	efc32 = models.IntegerField(db_column='EFC32', blank=True, null=True, verbose_name='EFC Level 32')  # Field name made lowercase.
	grant32 = models.IntegerField(db_column='Grant32', blank=True, null=True, verbose_name='Grant Level 32')  # Field name made lowercase.
	efc33 = models.IntegerField(db_column='EFC33', blank=True, null=True, verbose_name='EFC Level 33')  # Field name made lowercase.
	grant33 = models.IntegerField(db_column='Grant33', blank=True, null=True, verbose_name='Grant Level 33')  # Field name made lowercase.
	efc34 = models.IntegerField(db_column='EFC34', blank=True, null=True, verbose_name='EFC Level 34')  # Field name made lowercase.
	grant34 = models.IntegerField(db_column='Grant34', blank=True, null=True, verbose_name='Grant Level 34')  # Field name made lowercase.
	efc35 = models.IntegerField(db_column='EFC35', blank=True, null=True, verbose_name='EFC Level 35')  # Field name made lowercase.
	grant35 = models.IntegerField(db_column='Grant35', blank=True, null=True, verbose_name='Grant Level 35')  # Field name made lowercase.
	efc36 = models.IntegerField(db_column='EFC36', blank=True, null=True, verbose_name='EFC Level 36')  # Field name made lowercase.
	grant36 = models.IntegerField(db_column='Grant36', blank=True, null=True, verbose_name='Grant Level 36')  # Field name made lowercase.
	efc37 = models.IntegerField(db_column='EFC37', blank=True, null=True, verbose_name='EFC Level 37')  # Field name made lowercase.
	grant37 = models.IntegerField(db_column='Grant37', blank=True, null=True, verbose_name='Grant Level 37')  # Field name made lowercase.
	efc38 = models.IntegerField(db_column='EFC38', blank=True, null=True, verbose_name='EFC Level 38')  # Field name made lowercase.
	grant38 = models.IntegerField(db_column='Grant38', blank=True, null=True, verbose_name='Grant Level 38')  # Field name made lowercase.
	efc39 = models.IntegerField(db_column='EFC39', blank=True, null=True, verbose_name='EFC Level 39')  # Field name made lowercase.
	grant39 = models.IntegerField(db_column='Grant39', blank=True, null=True, verbose_name='Grant Level 39')  # Field name made lowercase.
	efc40 = models.IntegerField(db_column='EFC40', blank=True, null=True, verbose_name='EFC Level 40')  # Field name made lowercase.
	grant40 = models.IntegerField(db_column='Grant40', blank=True, null=True, verbose_name='Grant Level 40')  # Field name made lowercase.
	efc41 = models.IntegerField(db_column='EFC41', blank=True, null=True, verbose_name='EFC Level 41')  # Field name made lowercase.
	grant41 = models.IntegerField(db_column='Grant41', blank=True, null=True, verbose_name='Grant Level 41')  # Field name made lowercase.
	efc42 = models.IntegerField(db_column='EFC42', blank=True, null=True, verbose_name='EFC Level 42')  # Field name made lowercase.
	grant42 = models.IntegerField(db_column='Grant42', blank=True, null=True, verbose_name='Grant Level 42')  # Field name made lowercase.
	efc43 = models.IntegerField(db_column='EFC43', blank=True, null=True, verbose_name='EFC Level 43')  # Field name made lowercase.
	grant43 = models.IntegerField(db_column='Grant43', blank=True, null=True, verbose_name='Grant Level 24')  # Field name made lowercase.
	efc44 = models.IntegerField(db_column='EFC44', blank=True, null=True, verbose_name='EFC Level 44')  # Field name made lowercase.
	grant44 = models.IntegerField(db_column='Grant44', blank=True, null=True, verbose_name='Grant Level 44')  # Field name made lowercase.
	efc45 = models.IntegerField(db_column='EFC45', blank=True, null=True, verbose_name='EFC Level 45')  # Field name made lowercase.
	grant45 = models.IntegerField(db_column='Grant45', blank=True, null=True, verbose_name='Grant Level 45')  # Field name made lowercase.
	efc46 = models.IntegerField(db_column='EFC46', blank=True, null=True, verbose_name='EFC Level 46')  # Field name made lowercase.
	grant46 = models.IntegerField(db_column='Grant46', blank=True, null=True, verbose_name='Grant Level 46')  # Field name made lowercase.
	efc47 = models.IntegerField(db_column='EFC47', blank=True, null=True, verbose_name='EFC Level 47')  # Field name made lowercase.
	grant47 = models.IntegerField(db_column='Grant47', blank=True, null=True, verbose_name='Grant Level 47')  # Field name made lowercase.
	efc48 = models.IntegerField(db_column='EFC48', blank=True, null=True, verbose_name='EFC Level 48')  # Field name made lowercase.
	grant48 = models.IntegerField(db_column='Grant48', blank=True, null=True, verbose_name='Grant Level 48')  # Field name made lowercase.
	efc49 = models.IntegerField(db_column='EFC49', blank=True, null=True, verbose_name='EFC Level 49')  # Field name made lowercase.
	grant49 = models.IntegerField(db_column='Grant49', blank=True, null=True, verbose_name='Grant Level 49')  # Field name made lowercase.
	efc50 = models.IntegerField(db_column='EFC50', blank=True, null=True, verbose_name='EFC Level 50')  # Field name made lowercase.
	grant50 = models.IntegerField(db_column='Grant50', blank=True, null=True, verbose_name='Grant Level 50')  # Field name made lowercase.
	efc51 = models.IntegerField(db_column='EFC51', blank=True, null=True, verbose_name='EFC Level 51')  # Field name made lowercase.
	grant51 = models.IntegerField(db_column='Grant51', blank=True, null=True, verbose_name='Grant Level 51')  # Field name made lowercase.
	efc52 = models.IntegerField(db_column='EFC52', blank=True, null=True, verbose_name='EFC Level 52')  # Field name made lowercase.
	grant52 = models.IntegerField(db_column='Grant52', blank=True, null=True, verbose_name='Grant Level 52')  # Field name made lowercase.
	efc53 = models.IntegerField(db_column='EFC53', blank=True, null=True, verbose_name='EFC Level 53')  # Field name made lowercase.
	grant53 = models.IntegerField(db_column='Grant53', blank=True, null=True, verbose_name='Grant Level 53')  # Field name made lowercase.
	efc54 = models.IntegerField(db_column='EFC54', blank=True, null=True, verbose_name='EFC Level 54')  # Field name made lowercase.
	grant54 = models.IntegerField(db_column='Grant54', blank=True, null=True, verbose_name='Grant Level 54')  # Field name made lowercase.
	efc55 = models.IntegerField(db_column='EFC55', blank=True, null=True, verbose_name='EFC Level 55')  # Field name made lowercase.
	grant55 = models.IntegerField(db_column='Grant55', blank=True, null=True, verbose_name='Grant Level 55')  # Field name made lowercase.
	efc56 = models.IntegerField(db_column='EFC56', blank=True, null=True, verbose_name='EFC Level 56')  # Field name made lowercase.
	grant56 = models.IntegerField(db_column='Grant56', blank=True, null=True, verbose_name='Grant Level 56')  # Field name made lowercase.
	efc57 = models.IntegerField(db_column='EFC57', blank=True, null=True, verbose_name='EFC Level 57')  # Field name made lowercase.
	grant57 = models.IntegerField(db_column='Grant57', blank=True, null=True, verbose_name='Grant Level 57')  # Field name made lowercase.
	efc58 = models.IntegerField(db_column='EFC58', blank=True, null=True, verbose_name='EFC Level 58')  # Field name made lowercase.
	grant58 = models.IntegerField(db_column='Grant58', blank=True, null=True, verbose_name='Grant Level 58')  # Field name made lowercase.
	efc59 = models.IntegerField(db_column='EFC59', blank=True, null=True, verbose_name='EFC Level 59')  # Field name made lowercase.
	grant59 = models.IntegerField(db_column='Grant59', blank=True, null=True, verbose_name='Grant Level 59')  # Field name made lowercase.

	def __str__(self):
		return '{}-{}'.format( self.awardyear[:2], self.awardyear[2:])
		
	class Meta:
		db_table = 'PellControl'
		app_label = 'fc6'
		verbose_name = 'Pell Control'
		verbose_name_plural = 'Pell Control'
		ordering = ['-awardyear']
				

class Reportdates(models.Model):
	datefield = models.CharField(db_column='DateField', primary_key=True, max_length=25)  # Field name made lowercase.
	description = models.CharField(db_column='Description', max_length=50)  # Field name made lowercase.

	def __str__(self):
		return '{} --> {}'.format( self.datefield, self.description)

	class Meta:
		db_table = 'ReportDates'
		app_label = 'fc6'
		verbose_name = 'Report Date'
		

class Program(models.Model):
	programid = models.AutoField(db_column='ProgramID', primary_key=True)  # Field name made lowercase.
	school = models.ForeignKey('Schoolinfo', models.DO_NOTHING, db_column='School_ID', blank=True, null=True)  # Field name made lowercase.
	schoolid = models.CharField(db_column='SchoolID', max_length=10, blank=True, null=True, verbose_name='School')  # Field name made lowercase.
	programname = models.CharField(db_column='ProgramName', max_length=50, blank=True, null=True, verbose_name='Program Name')  # Field name made lowercase.
	federalweeks = models.DecimalField(db_column='FederalWeeks', max_digits=5, decimal_places=2, blank=True, null=True, verbose_name='Federal Weeks')  # Field name made lowercase.
	programweeks = models.DecimalField(db_column='ProgramWeeks', max_digits=5, decimal_places=2, blank=True, null=True, verbose_name='Program Weeks')  # Field name made lowercase.
	federalcredithours = models.DecimalField(db_column='FederalCreditHours', max_digits=8, decimal_places=4, blank=True, null=True, verbose_name='Federal Credit Hours')  # Field name made lowercase.
	programcredithours = models.DecimalField(db_column='ProgramCreditHours', max_digits=8, decimal_places=4, blank=True, null=True, verbose_name='Program Credit Hours')  # Field name made lowercase.
	federalclockhours = models.DecimalField(db_column='FederalClockHours', max_digits=8, decimal_places=4, blank=True, null=True, verbose_name='Federal Clock Hours')  # Field name made lowercase.
	programclockhours = models.DecimalField(db_column='ProgramClockHours', max_digits=8, decimal_places=4, blank=True, null=True, verbose_name='Program Clock Hours')  # Field name made lowercase.
	programhourstype = models.IntegerField(db_column='ProgramHoursType', choices = HOURS_TYPES, blank=True, null=True, verbose_name='Hours Type')  # Field name made lowercase.
	otherfee1desc = models.CharField(db_column='OtherFee1Desc', max_length=15, blank=True, null=True, verbose_name='Other Fee 1 Description')  # Field name made lowercase.
	otherfee2desc = models.CharField(db_column='OtherFee2Desc', max_length=15, blank=True, null=True, verbose_name='Other Fee 2 Description')  # Field name made lowercase.
	cipcode = models.CharField(db_column='CIPCode', max_length=7, blank=True, null=True, verbose_name='CIP Code')  # Field name made lowercase.
	programidold = models.IntegerField(db_column='ProgramIDOLD', blank=True, null=True, default=0)  # Field name made lowercase.

	def __str__(self):
		return '{}'.format( self.programname)

	class Meta:
		db_table = 'Program'
		app_label = 'fc6'
		ordering = ['school', 'programname']

class Reports(models.Model):
	reportname = models.CharField(db_column='ReportName', primary_key=True, max_length=50, verbose_name='Report Name')  # Field name made lowercase.
	reporttitle = models.CharField(db_column='ReportTitle', max_length=50, blank=True, null=True, verbose_name='Report Title')  # Field name made lowercase.
	datefield1 = models.CharField(db_column='DateField1', max_length=25, blank=True, null=True, verbose_name='Date Field 1')  # Field name made lowercase.
	datefield2 = models.CharField(db_column='DateField2', max_length=25, blank=True, null=True, verbose_name='Date Field 2')  # Field name made lowercase.
	datefield3 = models.CharField(db_column='DateField3', max_length=25, blank=True, null=True, verbose_name='Date Field 3')  # Field name made lowercase.
	datefield4 = models.CharField(db_column='DateField4', max_length=25, blank=True, null=True, verbose_name='Date Field 4')  # Field name made lowercase.
	datefielddefault = models.IntegerField(db_column='DateFieldDefault', blank=True, null=True, verbose_name='Date Field Default')  # Field name made lowercase.
	askstartdate = models.BooleanField(db_column='AskStartDate', verbose_name='Ask Start Date at Run-time', default=0)  # Field name made lowercase.
	startdatedefault = models.CharField(db_column='StartDateDefault', max_length=15, default='None', verbose_name='Default Start Date', choices=REPORT_DATE_TYPES)  # Field name made lowercase.
	askenddate = models.BooleanField(db_column='AskEndDate', verbose_name='Ask End Date at Run-time', default=0)  # Field name made lowercase.
	enddatedefault = models.CharField(db_column='EndDateDefault', max_length=15, default='None', verbose_name='Default End Date', choices=REPORT_DATE_TYPES)  # Field name made lowercase.
	askawardyear = models.BooleanField(db_column='AskAwardYear', blank=True, null=False, default=0, verbose_name='Ask Award Year at Run-time')  # Field name made lowercase.
	awardyeardefault = models.CharField(db_column='AwardYearDefault', max_length=10, default='None', verbose_name='Default Award Year', choices=AWARD_YEARS)  # Field name made lowercase.
	askcampus = models.BooleanField(db_column='AskCampus', default=0, verbose_name='Ask for Campus at Run-time')  # Field name made lowercase.
	campusdefault = models.IntegerField(db_column='CampusDefault', default=0, verbose_name='Default Campus')  # Field name made lowercase.
	askdetails = models.BooleanField(db_column='AskDetails', default=0, verbose_name='Ask to Print Details at Run-time')  # Field name made lowercase.
	detailsdefault = models.BooleanField(db_column='DetailsDefault', max_length=1, default=0, verbose_name='Print Details at Run-time Default')  # Field name made lowercase.
	asktotals = models.BooleanField(db_column='AskTotals', default=0, verbose_name='Ask to Print Totals at Run-time')  # Field name made lowercase.
	totalsdefault = models.BooleanField(db_column='TotalsDefault', default=0, verbose_name='Print Totals at Run-time Default')  # Field name made lowercase.
	askfullssn = models.BooleanField(db_column='AskFullSSN', default=0, verbose_name='Ask to Print Full SSN at Run-time')  # Field name made lowercase.
	fullssndefault = models.BooleanField(db_column='FullSSNDefault', default=0, verbose_name='Print Full SSN at Run-time Default')  # Field name made lowercase.
	askstatus = models.BooleanField(db_column='AskStatus', default=0, verbose_name='Ask for Enrollment Statuses at Run-time')  # Field name made lowercase.
	statuses = models.ManyToManyField(Enrollmentstatus, verbose_name='Enrollment Statuses')
	askfedpgm = models.BooleanField(db_column='AskFedPgm', default=0, verbose_name='Ask for Federal Programs at Run-time')  # Field name made lowercase.
	fedpgms = models.ManyToManyField(Federalprograms, verbose_name='Federal Programs', limit_choices_to={'active':True})
	askstudypgm = models.BooleanField(db_column='AskStudyPgm', default=0, verbose_name='Ask for Study Programs at Run-time')  # Field name made lowercase.
	studypgms = models.ManyToManyField(Program, verbose_name='Study Programs', limit_choices_to=limit_school_choices)
	studypgmdefaults = models.CharField(db_column='StudyPgmDefaults', max_length=50, blank=True, null=True)  # Field name made lowercase.
	askorderby = models.BooleanField(db_column='AskOrderBy', blank=True, null=False, default=0, verbose_name='Ask Order-by at Run-time')  # Field name made lowercase.
	orderbydefault = models.IntegerField(db_column='OrderByDefault', blank=True, null=True, verbose_name='Order-by Default')  # Field name made lowercase.
	orderbyfield1 = models.CharField(db_column='OrderByField1', max_length=100, verbose_name='Order-by Field 1')  # Field name made lowercase.
	orderbyfield2 = models.CharField(db_column='OrderByField2', max_length=100, verbose_name='Order-by Field 2')  # Field name made lowercase.
	orderbyfield3 = models.CharField(db_column='OrderByField3', max_length=100, verbose_name='Order-by Field 3')  # Field name made lowercase.
	orderbyfield4 = models.CharField(db_column='OrderByField4', max_length=100, verbose_name='Order-by Field 4')  # Field name made lowercase.
	reportqueries = models.CharField(db_column='ReportQueries', max_length =50, blank=True, null=True)  # Field name made lowercase.
	deferqueries = models.BooleanField(db_column='DeferQueries', blank=True, null=False)  # Field name made lowercase.
	outputtype = models.CharField(db_column='OutputType', max_length=255, blank=True, null=True)  # Field name made lowercase.
	reporttable = models.CharField(db_column='ReportTable', max_length=255, blank=True, null=True)  # Field name made lowercase.

	def __str__(self):
		return '{}'.format( self.reporttitle)

	class Meta:
		db_table = 'Reports'
		app_label = 'fc6'
		verbose_name = 'Report'
		ordering = ['reportname',]
		

class Sequences(models.Model):
	sequenceid = models.AutoField(db_column='SequenceID', primary_key=True)  # Field name made lowercase.
	tablename = models.CharField(db_column='TableName', max_length=50)  # Field name made lowercase.
	keyfield = models.CharField(db_column='KeyField', max_length=50)  # Field name made lowercase.
	seq = models.IntegerField(db_column='Seq', blank=True, null=True)  # Field name made lowercase.

	def __str__(self):
		return '{} --> {} --> {}'.format( self.tablename, self.keyfield, self.seq)

	class Meta:
		db_table = 'Sequences'
		app_label = 'fc6'
		unique_together = (('tablename', 'keyfield'),)
		verbose_name = 'Sequence'
		ordering = ['tablename', 'seq', 'keyfield']
		
class Schoolinfo(models.Model):
	school_id = models.AutoField(db_column='School_ID', primary_key=True)  # Field name made lowercase.
	schoolid = models.CharField(db_column='SchoolID', max_length=10, verbose_name='Short Name')  # Field name made lowercase.
	schoolname = models.CharField(db_column='SchoolName', max_length=50, blank=True, null=True, verbose_name='Name')  # Field name made lowercase.
	contactname = models.CharField(db_column='ContactName', max_length=50, blank=True, null=True, verbose_name='Contact Name')  # Field name made lowercase.
	contacttitle = models.CharField(db_column='ContactTitle', max_length=50, blank=True, null=True, verbose_name='Contact Title')  # Field name made lowercase.
	contactemail = models.CharField(db_column='ContactEmail', max_length=50, blank=True, null=True, verbose_name='Contact Email')  # Field name made lowercase.
	contactphone = models.CharField(db_column='ContactPhone', max_length=10, blank=True, null=True, verbose_name='Contact Phone')  # Field name made lowercase.
	clockhoursschool = models.BooleanField(db_column='ClockHoursSchool', default=0, verbose_name='Clock Hours School')  # Field name made lowercase.
	schoolsendsawardletters = models.BooleanField(db_column='SchoolSendsAwardLetters', default=0, verbose_name='School Sends Award Letters')  # Field name made lowercase.
	tin_no = models.CharField(db_column='TIN_No', max_length=10, blank=True, null=True, verbose_name='TIN No.')  # Field name made lowercase.
	duns_no = models.CharField(db_column='DUNS_No', max_length=12, blank=True, null=True, verbose_name='DUNS No.')  # Field name made lowercase.
	pell_id = models.CharField(db_column='PELL_ID', max_length=6, blank=True, null=True, verbose_name='PELL ID')  # Field name made lowercase.
	ope_id = models.CharField(db_column='OPE_ID', max_length=8, blank=True, null=True, verbose_name='OPE ID')  # Field name made lowercase.
	
	def __str__(self):
		return '{} --> {} --> {}'.format( self.school_id, self.schoolid, self.schoolname)

	class Meta:
		db_table = 'SchoolInfo'
		app_label = 'fc6'
		verbose_name = 'School'
		ordering = ['school_id']
		

class Campuses(models.Model):
	campus_id = models.AutoField(db_column='Campus_ID', primary_key=True)  # Field name made lowercase.
	campusid = models.IntegerField(db_column='CampusID', default=1, verbose_name='ID')  # Field name made lowercase.
	schoolid = models.CharField(db_column='SchoolID', max_length=10, verbose_name='School')  # Field name made lowercase.
	school = models.ForeignKey('Schoolinfo', models.DO_NOTHING, db_column='School_ID')  # Field name made lowercase.#	school = models.IntegerField(db_column='School_ID')  # Field name made lowercase.
	campusname = models.CharField(db_column='CampusName', max_length=15, blank=True, null=True, verbose_name='Campus Name')  # Field name made lowercase.
	address1 = models.CharField(db_column='Address1', max_length=50, blank=True, null=True)  # Field name made lowercase.
	address2 = models.CharField(db_column='Address2', max_length=50, blank=True, null=True)  # Field name made lowercase.
	citystzip = models.CharField(db_column='CityStZip', max_length=50, blank=True, null=True, verbose_name='City, State, Zip')  # Field name made lowercase.
	phone = models.CharField(db_column='Phone', max_length=10, blank=True, null=True, verbose_name='Campus Phone')  # Field name made lowercase.
	contactname = models.CharField(db_column='ContactName', max_length=50, blank=True, null=True, verbose_name='Contact Name')  # Field name made lowercase.
	contacttitle = models.CharField(db_column='ContactTitle', max_length=50, blank=True, null=True, verbose_name='Contact Title')  # Field name made lowercase.
	contactemail = models.CharField(db_column='ContactEmail', max_length=50, blank=True, null=True, verbose_name='Contact Email')  # Field name made lowercase.
	contactphone = models.CharField(db_column='ContactPhone', max_length=10, blank=True, null=True, verbose_name='Contact Phone')  # Field name made lowercase.
	signawardletter = models.BooleanField(db_column='SignAwardLetter', default=0, verbose_name='Sign Awd Ltr')  # Field name made lowercase.

	def __str__(self):
		return '{} --> {}'.format( self.schoolid, self.campusname)

	class Meta:
		db_table = 'Campuses'
		app_label = 'fc6'
		unique_together = (('campusid', 'school'),)
		verbose_name = 'Campus'
		verbose_name_plural = 'Campuses'


class Schoolauthorizations(models.Model):
	authorizationid = models.AutoField(db_column='AuthorizationID', primary_key=True)  # Field name made lowercase.
	schoolid = models.CharField(db_column='SchoolID', max_length=10, blank=True, null=True)  # Field name made lowercase.
	school = models.ForeignKey('Schoolinfo', models.DO_NOTHING, db_column='School_ID')  # Field name made lowercase.
	awardyear = models.CharField(db_column='AwardYear', max_length=4)  # Field name made lowercase.
	fseog = models.DecimalField(db_column='FSEOG', max_digits=8, decimal_places=2, blank=True, null=True, default=0.00)  # Field name made lowercase.
	fws = models.DecimalField(db_column='FWS', max_digits=8, decimal_places=2, blank=True, null=True, default=0.00)  # Field name made lowercase.

	def __str__(self):
		return "{}-{}".format( self.awardyear[:2], self.awardyear[2:])

	class Meta:
		db_table = 'SchoolAuthorizations'
		app_label = 'fc6'
		unique_together = (('school', 'awardyear'),)
		verbose_name = 'School Authorization'
		ordering = ['schoolid', '-awardyear']
		

class Payments(models.Model):
	paymentid = models.AutoField(db_column='PaymentID', primary_key=True)  # Field name made lowercase.
	studentid = models.ForeignKey('Student', models.DO_NOTHING, db_column='StudentID', blank=True, null=True)  # Field name made lowercase.
	schoolid = models.CharField(db_column='SchoolID', max_length=10, blank=True, null=True)  # Field name made lowercase.
	school_id = models.IntegerField(db_column='School_ID', blank=True, null=True)
	ssn = models.CharField(db_column='SSN', max_length=9, blank=True, null=True)  # Field name made lowercase.
	studentprofileid = models.IntegerField(db_column='StudentProfileID', blank=True, null=True)  # Field name made lowercase.
	fedpgmid = models.IntegerField(db_column='FedPgmID', blank=True, null=True)  # Field name made lowercase.
	awardyear = models.CharField(db_column='AwardYear', max_length=4, blank=True, null=True)  # Field name made lowercase.
	scheddate = models.DateTimeField(db_column='SchedDate', blank=True, null=True)  # Field name made lowercase.
	amount = models.DecimalField(db_column='Amount', max_digits=8, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
	fedpgmpymtno = models.IntegerField(db_column='FedPgmPymtNo', blank=True, null=True)  # Field name made lowercase.
	hours = models.CharField(db_column='Hours', max_length=10, blank=True, null=True)  # Field name made lowercase.
	isirin = models.IntegerField(db_column='IsirIn', blank=True, null=True, default=0)  # Field name made lowercase.
	isirtranno = models.CharField(db_column='ISIRTranNo', max_length=2, blank=True, null=True)  # Field name made lowercase.
	repackage = models.IntegerField(db_column='Repackage', blank=True, null=True, default=0)  # Field name made lowercase.
	ckno = models.IntegerField(db_column='CkNo', blank=True, null=True)  # Field name made lowercase.
	ckdate = models.DateTimeField(db_column='CkDate', blank=True, null=True)  # Field name made lowercase.
	cktoid = models.IntegerField(db_column='CkToID', blank=True, null=True, default=1)  # Field name made lowercase.
	reqdate = models.DateTimeField(db_column='ReqDate', blank=True, null=True)  # Field name made lowercase.
	exported = models.IntegerField(db_column='exported', blank=True, null=True, default=0)
	exported_at = models.DateTimeField(db_column='exported_at', blank=True, null=True)
	paymentidold = models.IntegerField(db_column='PaymentIDOLD', blank=True, null=True, default=0)  # Field name made lowercase.
	disbid = models.CharField(db_column='DisbID', max_length=255, blank=True, null=True)
	enrollid = models.CharField(db_column='EnrollID', max_length=255, blank=True, null=True)
	postdate = models.DateTimeField(db_column='PostDate', blank=True, null=True)

	class Meta:
		db_table = 'Payments'
		app_label = 'fc6'
		verbose_name = 'Payment'
		

class Programfee(models.Model):
	programfeeid = models.AutoField(db_column='ProgramFeeID', primary_key=True)  # Field name made lowercase.
	schoolid = models.CharField(db_column='SchoolID', max_length=10, blank=True, null=True)  # Field name made lowercase.
	programid = models.ForeignKey(Program, models.DO_NOTHING, db_column='ProgramID', blank=True, null=True)  # Field name made lowercase.
	effectivedate = models.DateTimeField(db_column='EffectiveDate', blank=True, null=True, verbose_name='Effective Date')  # Field name made lowercase.
	tuitionfee = models.DecimalField(db_column='TuitionFee', max_digits=8, decimal_places=2, blank=True, null=True, verbose_name='Tuition Fee')  # Field name made lowercase.
	registrationfee = models.DecimalField(db_column='RegistrationFee', max_digits=8, decimal_places=2, blank=True, null=True, verbose_name='Registration Fee')  # Field name made lowercase.
	strffee = models.DecimalField(db_column='STRFFee', max_digits=8, decimal_places=2, blank=True, null=True, verbose_name='STRF Fee')  # Field name made lowercase.
	booksfee = models.DecimalField(db_column='BooksFee', max_digits=8, decimal_places=2, blank=True, null=True, verbose_name='Books Fee')  # Field name made lowercase.
	otherfee1 = models.DecimalField(db_column='OtherFee1', max_digits=8, decimal_places=2, blank=True, null=True, verbose_name='Other Fee 1')  # Field name made lowercase.
	otherfee2 = models.DecimalField(db_column='OtherFee2', max_digits=8, decimal_places=2, blank=True, null=True, verbose_name='Other Fee 2')  # Field name made lowercase.

	def __str__(self):
		return '{} --> {}'.format( self.programid, self.effectivedate)

	class Meta:
		db_table = 'ProgramFee'
		app_label = 'fc6'
		verbose_name = 'Program Fee'
		ordering = ['schoolid', 'programid', '-effectivedate']
		

class Student(models.Model):
	studentid = models.AutoField(db_column='StudentID', primary_key=True)  # Field name made lowercase.
	school = models.ForeignKey(Schoolinfo, models.DO_NOTHING, db_column='School_ID', blank=True, null=True, default=0)  # Field name made lowercase.
	schoolid = models.CharField(db_column='SchoolID', max_length=10)  # Field name made lowercase.
	ssn = models.CharField(db_column='SSN', unique=True, max_length=9)  # Field name made lowercase.
	lastname = models.CharField(db_column='LastName', max_length=30, blank=True, null=True)  # Field name made lowercase.
	firstname = models.CharField(db_column='FirstName', max_length=30, blank=True, null=True)  # Field name made lowercase.
	middleinit = models.CharField(db_column='MiddleInit', max_length=1, blank=True, null=True)  # Field name made lowercase.
	address1 = models.CharField(db_column='Address1', max_length=50, blank=True, null=True)  # Field name made lowercase.
	address2 = models.CharField(db_column='Address2', max_length=50, blank=True, null=True)  # Field name made lowercase.
	city = models.CharField(db_column='City', max_length=50, blank=True, null=True)  # Field name made lowercase.
	state = models.CharField(db_column='State', max_length=2, blank=True, null=True)  # Field name made lowercase.
	zip = models.CharField(db_column='Zip', max_length=9, blank=True, null=True)  # Field name made lowercase.
	phone = models.CharField(db_column='Phone', max_length=15, blank=True, null=True)  # Field name made lowercase.
	gender = models.CharField(db_column='Gender', max_length=1, blank=True, null=True)  # Field name made lowercase.
	ethnicityid = models.IntegerField(db_column='EthnicityID', blank=True, null=True)  # Field name made lowercase.
	email = models.CharField(db_column='Email', max_length=50, blank=True, null=True)  # Field name made lowercase.
	notes = models.TextField(db_column='Notes', blank=True, null=True)  # Field name made lowercase.
	dob = models.DateTimeField(db_column='DOB', blank=True, null=True)  # Field name made lowercase.

	def __str__(self):
		return str(self.studentid)

	class Meta:
		db_table = 'Student'
		app_label = 'fc6'

class Studentfunding(models.Model):
	studentfundingid = models.AutoField(db_column='StudentFundingID', primary_key=True)  # Field name made lowercase.
	school_id = models.IntegerField(db_column='School_ID', blank=True, null=True, default=0)  # Field name made lowercase.
	studentid = models.IntegerField(db_column='StudentID', blank=True, null=True, default=0)  # Field name made lowercase.
	schoolid = models.CharField(db_column='SchoolID', max_length=10, blank=True, null=True)  # Field name made lowercase.
	ssn = models.CharField(db_column='SSN', max_length=9, blank=True, null=True)  # Field name made lowercase.
	studentprofileid = models.ForeignKey('Studentprofile', models.DO_NOTHING, db_column='StudentProfileID', blank=True, null=True)  # Field name made lowercase.
	fedpgmid = models.IntegerField(db_column='FedPgmID', blank=True, null=True)  # Field name made lowercase.
	enrollid = models.CharField(db_column='EnrollID', max_length=255, blank=True, null=True)
	awardid = models.CharField(db_column='AwardID', max_length=255, blank=True, null=True)
	disbid = models.CharField(db_column='DisbID', max_length=255, blank=True, null=True)
	disbnum = models.CharField(db_column='DisbNum', max_length=255, blank=True, null=True)
	scheddate = models.DateTimeField(db_column='SchedDate', blank=True, null=True)  # Field name made lowercase.
	fundingamount = models.DecimalField(db_column='FundingAmount', max_digits=8, decimal_places=2, blank=True, null=True, default=0.00)  # Field name made lowercase.
	loanfee = models.DecimalField(db_column='LoanFee', max_digits=6, decimal_places=5, blank=True, null=True, default=0.00000)  # Field name made lowercase.

	class Meta:
		db_table = 'StudentFunding'
		app_label = 'fc6'
		unique_together = (('studentprofileid', 'studentfundingid', 'fedpgmid'),)


class Studentprofile(models.Model):
	studentprofileid = models.AutoField(db_column='StudentProfileID', primary_key=True)  # Field name made lowercase.
	schoolid = models.CharField(db_column='SchoolID', max_length=10, blank=True, null=True)  # Field name made lowercase.
	ssn = models.CharField(db_column='SSN', max_length=9, blank=True, null=True)  # Field name made lowercase.
	school_id = models.IntegerField(db_column='School_ID', blank=True, null=True, default=0)  # Field name made lowercase.
	studentid = models.ForeignKey(Student, models.DO_NOTHING, db_column='StudentID', blank=True, null=True)  # Field name made lowercase.
	studentprofileidold = models.IntegerField(db_column='StudentProfileIDOLD', blank=True, null=True, default=0)  # Field name made lowercase.
	programid = models.IntegerField(db_column='ProgramID', blank=True, null=True)  # Field name made lowercase.
	awardyear = models.CharField(db_column='AwardYear', max_length=4, blank=True, null=True)  # Field name made lowercase.
	budgetyear = models.CharField(db_column='BudgetYear', max_length=4, blank=True, null=True)  # Field name made lowercase.
	campusid = models.IntegerField(db_column='CampusID', blank=True, null=True, default=1)  # Field name made lowercase.
	startdate = models.DateTimeField(db_column='StartDate', blank=True, null=True)  # Field name made lowercase.
	enddate = models.DateTimeField(db_column='EndDate', blank=True, null=True)  # Field name made lowercase.
	expectedgraddate = models.DateTimeField(db_column='ExpectedGradDate', blank=True, null=True)  # Field name made lowercase.
	programhours = models.DecimalField(db_column='ProgramHours', max_digits=8, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
	federalhours = models.DecimalField(db_column='FederalHours', max_digits=8, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
	programweeks = models.DecimalField(db_column='ProgramWeeks', max_digits=5, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
	federalweeks = models.DecimalField(db_column='FederalWeeks', max_digits=5, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
	transferhours = models.DecimalField(db_column='TransferHours', max_digits=8, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
	programhourstype = models.IntegerField(db_column='ProgramHoursType', blank=True, null=True)  # Field name made lowercase.
	enrollmentstatusid = models.IntegerField(db_column='EnrollmentStatusID', blank=True, null=True)  # Field name made lowercase.
	tuitionfee = models.DecimalField(db_column='TuitionFee', max_digits=8, decimal_places=2, blank=True, null=True, default=0.00)  # Field name made lowercase.
	registrationfee = models.DecimalField(db_column='RegistrationFee', max_digits=8, decimal_places=2, blank=True, null=True, default=0.00)  # Field name made lowercase.
	booksfee = models.DecimalField(db_column='BooksFee', max_digits=8, decimal_places=2, blank=True, null=True, default=0.00)  # Field name made lowercase.
	strffee = models.DecimalField(db_column='STRFFee', max_digits=8, decimal_places=2, blank=True, null=True, default=0.00)  # Field name made lowercase.
	otherfee1 = models.DecimalField(db_column='OtherFee1', max_digits=8, decimal_places=2, blank=True, null=True, default=0.00)  # Field name made lowercase.
	otherfee2 = models.DecimalField(db_column='OtherFee2', max_digits=8, decimal_places=2, blank=True, null=True, default=0.00)  # Field name made lowercase.
	otherfee1desc = models.CharField(db_column='OtherFee1Desc', max_length=15, blank=True, null=True)  # Field name made lowercase.
	otherfee2desc = models.CharField(db_column='OtherFee2Desc', max_length=15, blank=True, null=True)  # Field name made lowercase.
	housingtypeid = models.IntegerField(db_column='HousingTypeID', blank=True, null=True)  # Field name made lowercase.
	foodhousingexp = models.DecimalField(db_column='FoodHousingExp', max_digits=8, decimal_places=2, blank=True, null=True, default=0.00)  # Field name made lowercase.
	transportationexp = models.DecimalField(db_column='TransportationExp', max_digits=8, decimal_places=2, blank=True, null=True, default=0.00)  # Field name made lowercase.
	personalexp = models.DecimalField(db_column='PersonalExp', max_digits=8, decimal_places=2, blank=True, null=True, default=0.00)  # Field name made lowercase.
	childcareexp = models.DecimalField(db_column='ChildCareExp', max_digits=8, decimal_places=2, blank=True, null=True, default=0.00)  # Field name made lowercase.
	otherexp = models.DecimalField(db_column='OtherExp', max_digits=8, decimal_places=2, blank=True, null=True, default=0.00)  # Field name made lowercase.
	manualisir = models.IntegerField(db_column='ManualISIR', blank=True, null=True, default=0)  # Field name made lowercase.
	isir_model = models.CharField(db_column='ISIR_Model', max_length=1, blank=True, null=True)  # Field name made lowercase.
	efc_9_mo = models.DecimalField(db_column='EFC_9_Mo', max_digits=9, decimal_places=2, blank=True, null=True, default=0.00)  # Field name made lowercase.
	efc_used = models.DecimalField(db_column='EFC_Used', max_digits=9, decimal_places=2, blank=True, null=True, default=0.00)  # Field name made lowercase.
	fisap = models.DecimalField(db_column='FISAP', max_digits=9, decimal_places=2, blank=True, null=True, default=0.00)  # Field name made lowercase.
	isirtranno = models.CharField(db_column='ISIRTranNo', max_length=2, blank=True, null=True)  # Field name made lowercase.
	isirupdatedate = models.DateTimeField(db_column='ISIRUpdateDate', blank=True, null=True)  # Field name made lowercase.
	autozeroefc = models.IntegerField(db_column='AutoZeroEFC', blank=True, null=True, default=0)  # Field name made lowercase.
	firsttimefinaid = models.IntegerField(db_column='FirstTimeFinAid', blank=True, null=True, default=0)  # Field name made lowercase.
	verifytype = models.CharField(db_column='VerifyType', max_length=2, blank=True, null=True)  # Field name made lowercase.
	c_flag = models.IntegerField(db_column='C_Flag', blank=True, null=True, default=0)  # Field name made lowercase.
	studentirsreqflag = models.CharField(db_column='StudentIRSReqFlag', max_length=2, blank=True, null=True)  # Field name made lowercase.
	parentirsreqflag = models.CharField(db_column='ParentIRSReqFlag', max_length=2, blank=True, null=True)  # Field name made lowercase.
	incomeyearforneed = models.CharField(db_column='IncomeYearForNeed', max_length=4, blank=True, null=True)  # Field name made lowercase.
	professionaljudgment = models.IntegerField(db_column='ProfessionalJudgment', blank=True, null=True, default=0)  # Field name made lowercase.
	loanperiodfrom = models.DateTimeField(db_column='LoanPeriodFrom', blank=True, null=True)  # Field name made lowercase.
	loanperiodto = models.DateTimeField(db_column='LoanPeriodTo', blank=True, null=True)  # Field name made lowercase.
	awardletterid = models.IntegerField(db_column='AwardLetterID', blank=True, null=True)  # Field name made lowercase.
	awardletterdate = models.DateTimeField(db_column='AwardLetterDate', blank=True, null=True)  # Field name made lowercase.
	moddate = models.DateTimeField(db_column='ModDate', blank=True, null=True)  # Field name made lowercase.
	modby = models.CharField(db_column='ModBy', max_length=10, blank=True, null=True)  # Field name made lowercase.
	dod = models.DateTimeField(db_column='DOD', blank=True, null=True)  # Field name made lowercase.
	acd = models.DateTimeField(db_column='ACD', blank=True, null=True)  # Field name made lowercase.
	loa1start = models.DateTimeField(db_column='LOA1Start', blank=True, null=True)  # Field name made lowercase.
	loa1end = models.DateTimeField(db_column='LOA1End', blank=True, null=True)  # Field name made lowercase.
	loa2start = models.DateTimeField(db_column='LOA2Start', blank=True, null=True)  # Field name made lowercase.
	loa2end = models.DateTimeField(db_column='LOA2End', blank=True, null=True)  # Field name made lowercase.
	loa3start = models.DateTimeField(db_column='LOA3Start', blank=True, null=True)  # Field name made lowercase.
	loa3end = models.DateTimeField(db_column='LOA3End', blank=True, null=True)  # Field name made lowercase.

	def __str__(self):
		return str(self.studentprofileid)

	class Meta:
		db_table = 'StudentProfile'
		app_label = 'fc6'
		unique_together = (('studentid', 'studentprofileid'),)

class Appsettings(models.Model):
	setting = models.CharField(max_length=255)
	value = models.CharField(max_length=255)

	def __str__(self):
		val = '*' * len(self.value) if self.setting == 'EdExpressPassword' else self.value
		return '{} --> {}'.format( self.setting, val)

	class Meta:
		db_table = 'AppSettings'
		app_label = 'fc6'
		verbose_name = 'Application Setting'

class Usersettings(models.Model):
	user = models.ForeignKey(User, models.CASCADE)
	setting = models.CharField(max_length=255)
	value = models.CharField(max_length=255)

	def __str__(self):
		val = '{}-{}'.format(self.value[:2], self.value[2:]) if self.setting == 'ActiveYear' else self.value
		return '{} --> {} --> {}'.format( self.user.username, self.setting, val)

	class Meta:
		db_table = 'UserSettings'
		app_label = 'fc6'
		verbose_name = 'User Setting'

class Migrations(models.Model):
	migration = models.CharField(max_length=255)
	batch = models.IntegerField()

	class Meta:
		managed = False
		db_table = 'migrations'

class PasswordResets(models.Model):
	email = models.CharField(max_length=255)
	token = models.CharField(max_length=255)
	created_at = models.DateTimeField(blank=True, null=True)

	class Meta:
		managed = False
		db_table = 'password_resets'


class PermissionRole(models.Model):
	permission = models.ForeignKey('Permissions', models.DO_NOTHING, primary_key=True)
	role = models.ForeignKey('Roles', models.DO_NOTHING)

	class Meta:
		managed = False
		db_table = 'permission_role'


class Permissions(models.Model):
	name = models.CharField(max_length=255)
	label = models.CharField(max_length=255, blank=True, null=True)
	created_at = models.DateTimeField(blank=True, null=True)
	updated_at = models.DateTimeField(blank=True, null=True)

	class Meta:
		managed = False
		db_table = 'permissions'


class RoleUser(models.Model):
	role = models.ForeignKey('Roles', models.DO_NOTHING, primary_key=True)
	user = models.ForeignKey('Users', models.DO_NOTHING)

	class Meta:
		managed = False
		db_table = 'role_user'


class Roles(models.Model):
	name = models.CharField(max_length=255)
	label = models.CharField(max_length=255, blank=True, null=True)
	created_at = models.DateTimeField(blank=True, null=True)
	updated_at = models.DateTimeField(blank=True, null=True)

	class Meta:
		managed = False
		db_table = 'roles'


class UserActivations(models.Model):
	user_id = models.IntegerField()
	token = models.CharField(max_length=255)
	created_at = models.DateTimeField(blank=True, null=True)
	updated_at = models.DateTimeField(blank=True, null=True)

	class Meta:
		managed = False
		db_table = 'user_activations'


class Users(models.Model):
	name = models.CharField(max_length=255)
	email = models.CharField(unique=True, max_length=255)
	password = models.CharField(max_length=255)
	institution = models.TextField(blank=True, null=True)
	activated = models.IntegerField()
	remember_token = models.CharField(max_length=100, blank=True, null=True)
	created_at = models.DateTimeField(blank=True, null=True)
	updated_at = models.DateTimeField(blank=True, null=True)

	class Meta:
		managed = False
		db_table = 'users'
