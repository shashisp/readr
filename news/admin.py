from django.contrib import admin
import news.models as models


admin.site.register(models.Article)
admin.site.register(models.ReadLog)
admin.site.register(models.DeleteLog)