from django.contrib import admin
from posts.models import Posts, Hashtag, Comment

admin.site.register(Posts)
admin.site.register(Hashtag)
admin.site.register(Comment)
