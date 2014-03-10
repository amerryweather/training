from django.shortcuts import render, render_to_response, get_object_or_404
from django.template import RequestContext
from django.http import HttpResponse, HttpResponseRedirect
from django.views import generic
from feedback.models import AnswerOffered, Attendee, Question
from feedback.forms import AttendeeForm

# Create your views here.

def index(request):
	context = RequestContext(request)
	context_dict = {}
		
	return render_to_response('feedback/index.html', context_dict, context)
	
def add_attendee(request):
	context = RequestContext(request)
	context_dict = {}
	
	if request.method == 'POST':
		attendee_form = AttendeeForm(request.POST)
		
		if attendee_form.is_valid():
			attendee_obj = attendee_form.save(commit=False)
			attendee_obj.save()
			context_dict['attendee'] = attendee_obj.attendee_id
			return HttpResponseRedirect('/feedback/questions/%s/' % attendee_obj.attendee_id)
		else:
			return HttpResponse(attendee_form.errors)
	else:
		form = AttendeeForm()
	
	context_dict['form'] = form
	return render_to_response('feedback/add_attendee.html', context_dict, context)
	

def feedback_form(request):
	context = RequestContext(request)
	context_dict = {}
		
	return render_to_response('feedback/feedback_form.html', context_dict, context)
	
def questions(request, attendee_id):

	a = get_object_or_404(Attendee, pk=attendee_id)

	context = RequestContext(request)
	context_dict = {'attendee' : a}
	question_list = Question.objects.all()
	offered_answer_list = AnswerOffered.objects.all()
	context_dict['questions'] = question_list
	context_dict['offered_answers'] = offered_answer_list
	
	return render_to_response('feedback/questions.html', context_dict, context)
