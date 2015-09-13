from django.core.management.base import BaseCommand
import requests
import datetime
from news.models import Article

class Command(BaseCommand):
  args = 'Arguments is not needed'
  help = 'Custom Command to populate data'
 
  def handle(self, *args, **options):
    latest = requests.get('https://hacker-news.firebaseio.com/v0/topstories.json').json()
    latest = latest[:2]

    for i in latest:
      x = requests.get('https://hacker-news.firebaseio.com/v0/item/'+str(i)+'.json').json()

      #convert unix timestamp to datetime
      posted_on = datetime.datetime.fromtimestamp(float(x['time']))

      #create hn_url (HN format)
      hn_url = 'https://news.ycombinator.com/item?id='+str(x['id'])

      #HN jobs doesn't have comments(descendants), so assigning comments count to 0
      try:
        comments = x['descendants']
      except Exception:
        comments = 0

      try:
        #if article already exists update attributes 
        old = Article.objects.get(hn_id=x['id'])
        if old:
          Article.objects.update(hn_id=x['id'],
              up_votes=x['score'], comments=comments)
          print hn_url
          print 'updated'
          
      except Exception:
          Article.objects.get_or_create(hn_id=x['id'],
              url=x['url'], hn_url=hn_url,
              posted_on=posted_on,
              up_votes=x['score'],
              comments=comments)
          print hn_url
          print 'created'