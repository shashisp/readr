from django.core.management.base import BaseCommand
import requests
import datetime
from news.models import Article

class Command(BaseCommand):
  args = 'Arguments is not needed'
  help = 'Custom Command to populate data'
 
  def handle(self, *args, **options):
    self.stdout.write("Hello World")
    newest = requests.get('https://hacker-news.firebaseio.com/v0/newstories.json').json()
    newest = newest[:10]




    for i in newest:
      x = requests.get('https://hacker-news.firebaseio.com/v0/item/'+str(i)+'.json').json()

      posted_on = datetime.datetime.fromtimestamp(float(x['time']))
      hn_url = 'https://news.ycombinator.com/item?id='+str(x['id'])
   
      if Article.objects.filter(hn_id=x['id']).exists():
        Article.objects.update(hn_id=x['id'], url=x['url'],
            hn_url=hn_url, posted_on=posted_on,
            up_votes=x['score'], comments=x['descendants'])
      else:
        Article.objects.get_or_create(hn_id=x['id'],
            url=x['url'], hn_url=hn_url,
            posted_on=posted_on,
            up_votes=x['score'],
            comments=x['descendants'])
        print x
        print 'created'