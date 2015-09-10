from django.core.management.base import BaseCommand
import requests
from news.models import Article

class Command(BaseCommand):
  args = 'Arguments is not needed'
  help = 'Django admin custom command poc.'
 
  def handle(self, *args, **options):
    self.stdout.write("Hello World")
    newest = requests.get('https://hacker-news.firebaseio.com/v0/newstories.json').json()
    newest = newest[:90]

    for news in newest:
    	x = requests.get('https://hacker-news.firebaseio.com/v0/item/'+str(news)+'.json').json()
    	Article.objects.get_or_create(hn_id=x['id'],
				url=x['url'], hn_url=x['url'],
				posted_on=x['url'],
				up_votes=x['score'],
				comments=x['descendants'])
    	print str(x['id'])+'new story added'