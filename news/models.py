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


class Log(models.Model):
	article = models.ForeignKey(Article)
	user = models.ForeignKey(User)
	is_read = models.NullBooleanField(default=False)
	is_deleted  = models.NullBooleanField(default=False)

	def __unicode__(self):
		return u"%s" % self.user