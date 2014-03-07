from django.shortcuts import render, render_to_response
from django.template import RequestContext
from django.http import HttpResponse, HttpResponseRedirect
from django.views.generic.edit import CreateView
from feedback.models import Attendee
from feedback.forms import AttendeeForm

# Create your views here.

def index(request):
	context = RequestContext(request)
	context_dict = {}
		
	return render_to_response('feedback/index.html', {}, context)
	
class AttendeeCreate(CreateView):
	model = Attendee
	form_class = AttendeeForm
	template_name = 'feedback/add_feedback.html'
