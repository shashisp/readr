from tastypie.resources import ModelResource
from news.models import Article


class ArticleResource(ModelResource):
    class Meta:
        queryset = Article.objects.all()
        resource_name = 'news'