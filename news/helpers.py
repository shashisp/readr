import requests
from news.models import Article
import datetime

def populate():
	newest = requests.get('https://hacker-news.firebaseio.com/v0/newstories.json').json()

	newest = newest[:10]




	for i in newest:
		x = requests.get('https://hacker-news.firebaseio.com/v0/item/'+str(i)+'.json').json()

		date = datetime.datetime.fromtimestamp(float(x['time']))
		Article.objects.get_or_create(hn_id=x['id'],
				url=x['url'], hn_url=x['url'],
				posted_on=date,
				up_votes=x['score'],
				comments=x['descendants'])
		print x
		print 'created'