from django import forms
from django.utils.timezone import now
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from feedback.models import Answer, Attendee, Company, Form, Role, Question, TrainingType
from django.contrib.admin.widgets import AdminDateWidget

class AttendeeForm(forms.ModelForm):

	first_name = forms.CharField(max_length=25)
	last_name  = forms.CharField(max_length=25)
	
	# Foreign keys
	
	company = forms.ModelChoiceField(
		queryset = Company.objects.all(),
		label = 'Company Name'
	)
	
	role = forms.ModelChoiceField(
		queryset = Role.objects.all(),
		label = 'Job Role'
	)
	
	# -- End foreign keys
	
	email = forms.EmailField(max_length=45)
	phone_number = forms.CharField(max_length=20)
	
	GENDER_CHOICES = (
		('M', 'Male'),
		('F', 'Female'),
	)
	EXPERIENCE_CHOICES = (
		('Yes', 'Yes'),
		('No', 'No'),
	)
	sex = forms.ChoiceField(choices=GENDER_CHOICES)
	experience = forms.ChoiceField(
		label = 'Previous experience?',
		widget = forms.RadioSelect(),
		choices = EXPERIENCE_CHOICES)
	
	# Crispy forms section
	def __init__(self, *args, **kwargs):
		super(AttendeeForm, self).__init__(*args, **kwargs)
		self.helper = FormHelper()
		self.helper.form_id = 'id-attendeeForm'
		self.helper.form_class = ''
		self.helper.form_method = 'post'
		self.helper.form_action = 'submit_survey'
		
		self.helper.add_input(Submit('submit', 'Continue'))
	
	class Meta:
		model = Attendee
		fields = ['first_name', 
				  'last_name', 
				  'email',
				  'phone_number', 
				  'sex', 
				  'experience',
				  'company',
				  'role']
				  
class FeedbackForm(forms.ModelForm):

	attendee = forms.ModelChoiceField(
		queryset=Attendee.objects.all(),
		widget=forms.HiddenInput(),
		label='Attendee',
		initial=1
	)
	training_type = forms.ModelChoiceField(
		queryset=TrainingType.objects.all(),
		label='Training Type'
	)
	
	class Meta:
		model = Form
		fields = ['attendee', 'training_type']
		
	# Crispy forms section
	def __init__(self, *args, **kwargs):
		super(FeedbackForm, self).__init__(*args, **kwargs)
		self.helper = FormHelper()
		self.helper.form_id = 'id-feedbackForm'
		self.helper.form_class = ''
		self.helper.form_method = 'post'
		self.helper.form_action = 'submit_survey'
		
		self.helper.add_input(Submit('submit', 'New Feedback'))
		
''' 
Will build the whole form rigidly for now.
Processing and saving will be performed in views.py.
''' 		
class QuestionForm(forms.Form):

	LIKERT_SCALE = (
		(1, 'Strongly Agree'),
		(2, 'Agree'),
		(3, 'Neutral'),
		(4, 'Disagree'),
		(5, 'Strongly Disagree')	
	)
	q1 = forms.ChoiceField(
		label=Question.objects.get(question_id=1),
		widget=forms.RadioSelect,
		choices=LIKERT_SCALE,
		required=True,
		)
		
	q2 = forms.ChoiceField(
		label=Question.objects.get(question_id=2),
		widget=forms.RadioSelect,
		choices=LIKERT_SCALE,
		required=True,
		)
		
	q3 = forms.ChoiceField(
		label=Question.objects.get(question_id=3),
		widget=forms.RadioSelect,
		choices=LIKERT_SCALE,
		required=True,
		)
		
	q4 = forms.ChoiceField(
		label=Question.objects.get(question_id=4),
		widget=forms.RadioSelect,
		choices=LIKERT_SCALE,
		required=True,
		)
		
	q5 = forms.CharField(
		label=Question.objects.get(question_id=5),
		max_length=45,
		)
		
	q6 = forms.CharField(
		label=Question.objects.get(question_id=6),
		max_length=45,
		)
		
	q7 = forms.CharField(
		label=Question.objects.get(question_id=7),
		max_length=45,
		)
		
	q8 = forms.CharField(
		label=Question.objects.get(question_id=8),
		max_length=45,
		)
		
	q9 = forms.CharField(
		label=Question.objects.get(question_id=9),
		max_length=45,
		)
	
	# Crispy forms section
	def __init__(self, *args, **kwargs):
		super(QuestionForm, self).__init__(*args, **kwargs)
		self.helper = FormHelper()
		self.helper.form_id = 'id-questionForm'
		self.helper.form_class = ''
		self.helper.form_method = 'post'
		self.helper.form_action = 'submit_survey'
		
		self.helper.add_input(Submit('submit', 'New Feedback'))
		
class HorizRadioRenderer(forms.RadioSelect.renderer):
	''' Overrides widget method to put radio buttons horizontally.
	'''
	
	def renderer(self):
		# Outputs radios
		return mark_safe(u'\n'.join([u'%s\n' % w for w in self]))
