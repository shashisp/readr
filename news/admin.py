from django.contrib import admin
import news.models as models


class ArticleAdmin(admin.ModelAdmin):
	model = models.Article
	list_display = ('posted_on', 'comments', 'up_votes')


class LogAdmin(admin.ModelAdmin):
	model = models.Log
	list_display = ('user', 'article', 'is_read', 'is_deleted')

admin.site.register(models.Article, ArticleAdmin)
admin.site.register(models.Log, LogAdmin)