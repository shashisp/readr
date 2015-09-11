from django.contrib import admin
import news.models as models


class ArticleAdmin(admin.ModelAdmin):
	model = models.Article
	list_display = ('posted_on', 'comments', 'up_votes')

class ReadlogAdmin(admin.ModelAdmin):
	model = models.ReadLog
	list_display = ('article', 'is_read')


class DeletelogAdmin(admin.ModelAdmin):
	model = models.DeleteLog
	list_display = ('article', 'is_deleted')

admin.site.register(models.Article, ArticleAdmin)
admin.site.register(models.ReadLog)
admin.site.register(models.DeleteLog)