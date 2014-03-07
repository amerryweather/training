from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from feedback.models import Attendee, Company, Role
from tekextensions.widgets import SelectWithPopUp

# Class to override ModelChoiceForm fields.
# This allows access to the ID

class CompanyModelChoiceField(forms.ModelChoiceField):
	def label_from_instance(self, obj):
		return obj
		
class RoleModelChoiceField(forms.ModelChoiceField):
	def label_from_instance(self, obj):
		return obj

class AttendeeForm(forms.ModelForm):

	#attendee_id = forms.IntegerField(widget=forms.HiddenInput(),label="Attendee ID")

	first_name = forms.CharField(max_length=25)
	last_name  = forms.CharField(max_length=25)
	
	# Foreign keys
	
	company = forms.ModelChoiceField(
		queryset = Company.objects.all(),
		label = 'Company Name',
		widget = SelectWithPopUp
	)
	
	role = forms.ModelChoiceField(
		queryset = Role.objects.all(),
		label = 'Job Role'
	)
	
	email	   = forms.EmailField(max_length=45)
	phone_number = forms.CharField(max_length=20)
	
	GENDER_CHOICES = (
		('M', 'Male'),
		('F', 'Female'),
	)
	EXPERIENCE_CHOICES = (
		('Y', 'Yes'),
		('N', 'No'),
	)
	sex = forms.ChoiceField(choices=GENDER_CHOICES)
	experience = forms.BooleanField(label = 'Previous experience?')
	
	
	# hidden fields
	#attendee_id = forms.IntegerField(widget=forms.HiddenInput(), initial=3)
	
	def __init__(self, *args, **kwargs):
		super(AttendeeForm, self).__init__(*args, **kwargs)
		self.helper = FormHelper()
		self.helper.form_id = 'id-attendeeForm'
		self.helper.form_class = ''
		self.helper.form_method = 'post'
		self.helper.form_action = 'submit_survey'
		
		self.helper.add_input(Submit('submit', 'Submit'))
	
	class Meta:
		model = Attendee
		fields = [#'attendee_id',
				  'first_name', 
				  'last_name', 
				  'email',
				  'phone_number', 
				  'sex', 
				  'experience',
				  'company',
				  'role']
				  
				  
