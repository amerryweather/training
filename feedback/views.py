from django.shortcuts import render, render_to_response
from django.template import RequestContext
from feedback.models import Attendee

# Create your views here.

def index(request):
	context = RequestContext(request)
	context_dict = {}
		
	return render_to_response('feedback/index.html', {}, context)
