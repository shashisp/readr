from tastypie.resources import ModelResource
from tastypie.authorization import Authorization
from tastypie import fields
from tastypie.utils import trailing_slash
from news.models import Article, Log
from django.conf.urls import url


class ArticleResource(ModelResource):
    class Meta:
        queryset = Article.objects.all()
        resource_name = 'news'
        list_allowed_methods = ['get']
        detail_allowed_methods = ['post', 'get']
        authorization = Authorization()


    def prepend_urls(self):
        return [
            url(r"^(?P<resource_name>%s)/(?P<pk>\d+)/updated%s$$" %
                (self._meta.resource_name, trailing_slash()),
                    self.wrap_view('update_log'),
                    name='api-update-read'),
        ]
    def get_object_list(self, request):

    	obj_list = super(ArticleResource, self).get_object_list(request)

    	return obj_list

    def update_log(self, request, **kwargs):
        self.method_check(request, allowed=['post'])
        body = json.loads(request.body)
        article = models.Article.objects.get(id=kwargs['pk'])

        log = Log.objects.get_or_create(
            user=request.user,
            article=article,
        )
        log.is_read = body['is_read']
        log.is_deleted = body['is_deleted']
        log.save()

        return self.create_response(request, {
            'success': True,
            'message': 'Successfully updated the log.',
        })


    def dehydrate(self, bundle):
    	# import ipdb; ipdb.set_trace()
    	read = Log.objects.filter(user=bundle.request.user ,article=bundle.obj, is_read=True).exists()
    	if read:
    		bundle.data['is_read'] = True

    	delete = Log.objects.filter(user=bundle.request.user,article=bundle.obj, is_deleted=True)
    	if delete:
    		bundle.data['is_deleted'] = True
    	# import datetime
    	bundle.data['posted_on'] = bundle.data['posted_on'].strftime("%Y-%m-%d %H:%M:%S")

    	return bundle


