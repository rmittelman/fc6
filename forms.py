from django import forms

class CampusForm(forms.ModelForm):
	'''CampusForm:  Used to size input fields'''
	
	class Meta:
		fields = ['campusid', 'campusname', 'address1', 'address2', 'citystzip', 'phone', 'contactname', 'contacttitle', 'contactemail', 'contactphone', 'signawardletter']
		widgets = {
					'campusid': forms.TextInput(attrs={'size': 2,}),
                    'campusname': forms.TextInput(attrs={'size': 10,}),
                    'address1': forms.TextInput(attrs={'size': 20}),
                    'address2': forms.TextInput(attrs={'size': 20}),
                    'citystzip': forms.TextInput(attrs={'size': 20}),
                    'phone': forms.TextInput(attrs={'size': 10}),
                    'contactname': forms.TextInput(attrs={'size': 15}),
                    'contacttitle': forms.TextInput(attrs={'size': 15}),
                    'contactemail': forms.TextInput(attrs={'size': 20}),
                    'contactphone': forms.TextInput(attrs={'size': 10}),
                    'signawardletter': forms.CheckboxInput(attrs={'size': 10})
                	}

class AuthorizationsForm(forms.ModelForm):
	'''AuthorizationsForm:  Used to size input fields'''
	
	class Meta:
		fields = ['awardyear', 'fseog', 'fws']
		widgets = {
					'awardyear': forms.TextInput(attrs={'size':4,}),
					'fseog': forms.TextInput(attrs={'size':6,}),
					'fws': forms.TextInput(attrs={'size':6,})
					}

class ProgramfeesForm(forms.ModelForm):
	'''ProgramfeesForm:  Used to size input fields'''

	class Meta:
		fields = ['effectivedate', 'tuitionfee', 'registrationfee', 'strffee', 'booksfee', 'otherfee1', 'otherfee2']
		widgets = {
			'effectivedate': forms.DateTimeInput(attrs={'size': 20}),
			'tuitionfee': forms.TextInput(attrs={'size': 10}),
			'registrationfee': forms.TextInput(attrs={'size': 10}),
			'strffee': forms.TextInput(attrs={'size': 10}),
			'booksfee': forms.TextInput(attrs={'size': 10}),
			'otherfee1': forms.TextInput(attrs={'size': 10}),
			'otherfee2': forms.TextInput(attrs={'size': 10}),

		}					