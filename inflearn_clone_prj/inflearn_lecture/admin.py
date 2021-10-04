from django.contrib import admin
from .models import myText, Comment


class myTextadmin(admin.ModelAdmin):
    list_display = ('pk', 'title')

admin.site.register(myText, myTextadmin)


class Commnetadmin(admin.ModelAdmin):
    list_display = ('pk', 'comment')

admin.site.register(Comment, Commnetadmin)
