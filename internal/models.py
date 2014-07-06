from django.db import models

# Create your models here.

class Staff(models.Model):
	staff_id = models.IntegerField(primary_key=True)
	first_name = models.CharField(max_length=45)
	last_name = models.CharField(max_length=45)
	start_date = models.DateTimeField()
	
	def __unicode__(self):
		full_name = self.first_name + ' ' + self.last_name
		return full_name
    	
class Subject(models.Model):
	subject_id = models.IntegerField(primary_key=True)
	subject_title = models.CharField(max_length=45)
	marks = models.IntegerField()
	pass_mark = models.IntegerField()
	
	def __unicode__(self):
		return subject_title
		
class Test(models.Model):
	test_id = models.IntegerField(primary_key=True)
	staff = models.ForeignKey('Staff')
	subject = models.ForeignKey('Subject')
	test_date = models.DateTimeField()
	mark = models.IntegerField()
	
	def __unicode__(self):
		test_string = self.staff.__unicode__ + ': ' + self.subject.__unicode__ + '(' + self.test_date + ')'
		return test_string
