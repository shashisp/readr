from django.db import models



class Article(models.Model):
	hn_id = models.IntegerField()
	url = models.URLField()
	hn_url = models.URLField()
	posted_on = models.CharField(max_length=100)
	up_votes = models.IntegerField()
	comments = models.IntegerField()


	def __unicode__(self):
		return self.url

