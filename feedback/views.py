from django.shortcuts import render, render_to_response
from django.template import RequestContext

# Create your views here.

def index(request):
	context = RequestContext(request)
	context_dict = {}
	
	attendee_list = Attendee.Objects.all()
	context_dict['attendees'] = attendee_list
	return render_to_response('feedback/index.html', {}, context)
