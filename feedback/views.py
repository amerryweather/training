from django.shortcuts import render, render_to_response
from django.template import RequestContext
from django.http import HttpResponseRedirect
from feedback.models import Attendee
from feedback.forms import AttendeeForm

# Create your views here.

def index(request):
	context = RequestContext(request)
	context_dict = {}
		
	return render_to_response('feedback/index.html', {}, context)
	
def add_feedback(request):
	context = RequestContext(request)
	context_dict = {}
	
	if request.method == 'POST':
		form = AttendeeForm(request.POST)
		
		if form.is_valid():
			attendee = form.save(commit=False)
			#attendee.attendee_id = 2
			#attendee.company_id = 1
			#attendee.role_id = 1
			#attendee.save()
			return HttpResponseRedirect('/feedback/')
		else:
			return HttpResponseRedirect('/feedback/')
	else:
		form = AttendeeForm()
	
	return render_to_response('feedback/add_feedback.html', {'form': form}, context)
