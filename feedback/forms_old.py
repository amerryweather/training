from django import forms
from feedback.models import Attendee

class AttendeeForm(forms.ModelForm):

	first_name = forms.CharField(max_length=25)
	last_name  = forms.CharField(max_length=25)
	email	   = forms.EmailField(max_length=45)
	phone_number = forms.CharField(max_length=20)
	
	class Meta:
		model = Attendee
		fields = ['first_name', 'last_name', 'email',
				  'phone_number']
