from django.db import models
from django.contrib.auth.models import User


class Article(models.Model):
	hn_id = models.IntegerField()
	url = models.URLField()
	hn_url = models.URLField()
	posted_on = models.DateTimeField(null=True)
	up_votes = models.IntegerField()
	comments = models.IntegerField()

	ordering = ('posted_on')

	def __unicode__(self):
		return self.url


class ReadLog(models.Model):
	article = models.OneToOneField(Article)
	user = models.OneToOneField(User)
	is_read = models.BooleanField(default=False)

	def __unicode__(self):
		return self.is_read

class DeleteLog(models.Model):
	article = models.OneToOneField(Article)
	user = models.OneToOneField(User)
	is_deleted = models.BooleanField(default=False)

	def __unicode(self):
		self.article