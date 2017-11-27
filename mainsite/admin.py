from django.contrib import admin
from .models import Benke, Shuoshi


class BenkeAdmin(admin.ModelAdmin):
    list_display = ('id', 'zhongwen', 'jigou', 'gpa')

admin.site.register(Benke,BenkeAdmin)


class ShuoshiAdmin(admin.ModelAdmin):
    list_display = ('id', 'zhongwen', 'jigou', 'gpa')

admin.site.register(Shuoshi, ShuoshiAdmin)