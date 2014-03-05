from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from feedback.models import Attendee

class AttendeeForm(forms.ModelForm):

	GENDER_CHOICES = (
		('M', 'Male'),
		('F', 'Female'),
	)

	first_name = forms.CharField(max_length=25)
	last_name  = forms.CharField(max_length=25)
	email	   = forms.EmailField(max_length=45)
	phone_number = forms.CharField(max_length=20)
	sex = forms.ChoiceField(choices=GENDER_CHOICES)
	experience = forms.CharField(max_length=1)
	
	# hidden fields
	attendee_id = forms.IntegerField(widget=forms.HiddenInput())
	company_id  = forms.IntegerField(widget=forms.HiddenInput())
	role_id     = forms.IntegerField(widget=forms.HiddenInput())
	
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
		fields = ['first_name', 'last_name', 'email',
				  'phone_number', 'sex', 'experience']
