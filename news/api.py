from tastypie.resources import ModelResource
from tastypie.authorization import Authorization
from news.models import Article


class ArticleResource(ModelResource):
    class Meta:
        queryset = Article.objects.all()
        resource_name = 'news'
        authorization = Authorization()