from django.contrib import admin
from music.models import Album, Song

# add the models you create inorder for you to manage them..
admin.site.register(Album)
admin.site.register(Song)