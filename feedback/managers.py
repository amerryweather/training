from django.db import models

class FormManager(models.Manager):
	def create_feedback_form(self, attendee, training_type):
		feedback_form = self.create
