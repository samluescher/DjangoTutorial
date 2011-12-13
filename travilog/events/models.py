from django.db import models


class Event(models.Model):
	title = models.CharField("title", max_length=255)
	description = models.TextField("description", null=True, blank=True)
	date = models.DateTimeField("date and time")
	location = models.CharField("location", max_length=255)
	#photo = models.ImageField("preview photo", null=True, blank=True)

	def __unicode__(self):
		return self.title


class Person(models.Model):
	first_name = models.CharField("first name", max_length=255)
	last_name = models.CharField("last name", max_length=255)
	event = models.ForeignKey(Event, related_name="participants")	
	
	def __unicode__(self):
		return "%s %s" % (self.first_name, self.last_name)