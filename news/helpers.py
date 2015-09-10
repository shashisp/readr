import requests
from news.models import Article


def populate():
	newest = requests.get('https://hacker-news.firebaseio.com/v0/newstories.json').json()

	newest = newest[:10]


	result = []

	for i in newest:
		x = requests.get('https://hacker-news.firebaseio.com/v0/item/'+str(i)+'.json').json()
		result.append(x)

	# import ipdb; ipdb.set_trace()
	# print result[0]['url']
		Article.objects.get_or_create(hn_id=x['id'],
				url=x['url'], hn_url=x['url'],
				posted_on=x['url'],
				up_votes=x['score'],
				comments=x['descendants'])
		print x
		print 'created'