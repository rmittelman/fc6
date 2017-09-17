from django.contrib import admin
from django.contrib.admin import SimpleListFilter

class SchoolFilter(SimpleListFilter):
	title='school'
	parameter_name='school'
	
	def lookups(self, request, model_admin):
		programs = set([p for p in model_admin.model.objects.all()])
		return [(p.school, p.programname) for p in programs]

	def queryset(self, request, queryset):
		return queryset.filter(school__exact=2)

from fc6.models import *
from fc6.forms import *

#from django import forms

admin.site.site_header = 'FC-6 Administration'
admin.site.index_title = 'FC-6 Administration'


class AllowancesAdmin(admin.ModelAdmin):
	fields = ('fiscalyear', ('on_roomboard', 'on_transportation', 'on_personal'), ('wp_roomboard', 'wp_transportation', 'wp_personal'), ('off_roomboard', 'off_transportation', 'off_personal'))
	
admin.site.register(Allowances, AllowancesAdmin)

admin.site.register(Appsettings)
admin.site.register(Usersettings)

class AwardlettersAdmin(admin.ModelAdmin):
	fields = (
		'awardletterid', ('awardlettername', 'awardletterdoc'), ('paragraph1', 'p1signaturerelated'), ('paragraph2', 'p2signaturerelated'), 
		('paragraph3', 'p3signaturerelated'), ('paragraph4', 'p4signaturerelated'), ('paragraph5', 'p5signaturerelated'), 
		('paragraph6', 'p6signaturerelated'), ('paragraph7', 'p7signaturerelated'), ('paragraph8', 'p8signaturerelated'))
	
	save_on_top = True
	
admin.site.register(Awardletters, AwardlettersAdmin)

admin.site.register(Checkto)
admin.site.register(Enrollmentstatus)

class FederalprogramsAdmin(admin.ModelAdmin):
	fields = (
		('fedpgmid', 'fedpgmname', 'seq', 'active'), ('loanfee', 'titleiv', 'ffelp', 'fawostafford', 'fawstafford'))
	#ordering = ['fedpgmid']
	
admin.site.register(Federalprograms, FederalprogramsAdmin
)
admin.site.register(FisapAwardGroups)

#class IsirirsreqtypesAdmin(admin.ModelAdmin):
#	list_display = ('__str__',)
#	list_display_links = ('__str__',)

admin.site.register(Isirirsreqtypes) #, IsirirsreqtypesAdmin)

admin.site.register(Isirverificationtype)
admin.site.register(Livingexpenses)

class PellcontrolAdmin(admin.ModelAdmin):
	fields = (
		('awardyear', 'minclockhours', 'mincredithours'),
		('efc0', 'grant0'), ('efc1', 'grant1'), ('efc2', 'grant2'), ('efc3', 'grant3'), ('efc4', 'grant4'), 
		('efc5', 'grant5'), ('efc6', 'grant6'), ('efc7', 'grant7'), ('efc8', 'grant8'), ('efc9', 'grant9'), 
		('efc10', 'grant10'), ('efc11', 'grant11'), ('efc12', 'grant12'), ('efc13', 'grant13'), ('efc14', 'grant14'), 
		('efc15', 'grant15'), ('efc16', 'grant16'), ('efc17', 'grant17'), ('efc18', 'grant18'), ('efc19', 'grant19'), 
		('efc20', 'grant20'), ('efc21', 'grant21'), ('efc22', 'grant22'), ('efc23', 'grant23'), ('efc24', 'grant24'), 
		('efc25', 'grant25'), ('efc26', 'grant26'), ('efc27', 'grant27'), ('efc28', 'grant28'), ('efc29', 'grant29'), 
		('efc30', 'grant30'), ('efc31', 'grant31'), ('efc32', 'grant32'), ('efc33', 'grant33'), ('efc34', 'grant34'), 
		('efc35', 'grant35'), ('efc36', 'grant36'), ('efc37', 'grant37'), ('efc38', 'grant38'), ('efc39', 'grant39'), 
		('efc40', 'grant40'), ('efc41', 'grant41'), ('efc42', 'grant42'), ('efc43', 'grant43'), ('efc44', 'grant44'), 
		('efc45', 'grant45'), ('efc46', 'grant46'), ('efc47', 'grant47'), ('efc48', 'grant48'), ('efc49', 'grant49'), 
		('efc50', 'grant50'), ('efc51', 'grant51'), ('efc52', 'grant52'), ('efc53', 'grant53'), ('efc54', 'grant54'), 
		('efc55', 'grant55'), ('efc56', 'grant56'), ('efc57', 'grant57'), ('efc58', 'grant58'), ('efc59', 'grant59'))

	save_on_top = True

admin.site.register(Pellcontrol, PellcontrolAdmin)
admin.site.register(Reportdates)

class ReportsAdmin(admin.ModelAdmin):
	fields = (
		('reportname', 'reporttitle'), ('datefield1', 'datefield2'), ('datefield3', 'datefield4', 'datefielddefault'),
		('startdatedefault', 'askstartdate', 'enddatedefault', 'askenddate'), 
		('awardyeardefault', 'askawardyear', 'campusdefault', 'askcampus'), 
		('detailsdefault', 'askdetails'), ('totalsdefault', 'asktotals'), ('fullssndefault', 'askfullssn'), 
		('statuses', 'askstatus'), ('fedpgms', 'askfedpgm'), ('studypgms', 'askstudypgm'),
		('orderbyfield1', 'orderbyfield2'), ('orderbyfield3', 'orderbyfield4'), 
		('orderbydefault', 'askorderby'),
		('reportqueries', 'outputtype'))
	
	save_on_top = True
	filter_horizontal = ('statuses', 'fedpgms', 'studypgms',)
	
admin.site.register(Reports, ReportsAdmin)
admin.site.register(Sequences)

class CampusesInline(admin.TabularInline):
	model = Campuses
	form = CampusForm
	extra = 0


#admin.site.register(Campuses)

class SchoolauthorizationsInline(admin.TabularInline):
	model = Schoolauthorizations
	form = AuthorizationsForm
	extra = 0

#admin.site.register(Schoolauthorizations)

class SchoolInfoAdmin(admin.ModelAdmin):
	fields = (
		('schoolid', 'schoolname'), ('contactname', 'contacttitle'), ('contactphone', 'contactemail'), 
		('clockhoursschool', 'schoolsendsawardletters'), ('tin_no', 'duns_no'), ('pell_id', 'ope_id'))
	
	save_on_top = True
	inlines = [CampusesInline, SchoolauthorizationsInline,]

admin.site.register(Schoolinfo, SchoolInfoAdmin)

class ProgramfeesInline(admin.TabularInline):
	model = Programfee
	form = ProgramfeesForm
	extra = 0

class ProgramAdmin(admin.ModelAdmin):
	fields = (
		('schoolid', 'programname'), ('federalweeks', 'programweeks'),
		('federalcredithours', 'programcredithours'), ('federalclockhours', 'programclockhours'),
		('programhourstype', 'cipcode'), ('otherfee1desc', 'otherfee2desc')
	)
	save_on_top = True
	list_filter = ('school',)
	inlines = [ProgramfeesInline,]

admin.site.register(Program, ProgramAdmin)
#admin.site.register(Programfee)
