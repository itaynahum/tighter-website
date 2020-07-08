from django.db import models
from django.urls import reverse

# Create your models here.
"""
when you create new class(new table in the database) - it converts it into SQL code file.
you should migrate the app you created to the database, for it to synchronize with everything.
cmd command - (project path) "python manage.py makemigrations music(app)"
and then run the sql file created - "python manage.py migrate"
"""


"""
after you create a table at the database, you can add data 
into it by using the power shell to connect between "manage.py" to the db.

import the models you created(the classes)
the syntax =>"python manage.py shell"
create an object to that classes with the data, hit "<object>.save()"
and then it should be added to the data base.

"""


# when ever you make changes in this file you have to load you migrations inorder for the database to sync!!
# note - only if you delete orr add attributes(data to the table)
# each song in the database is linked to a song. Album - table, Song - table
class Album(models.Model):
    artist = models.CharField(max_length=250)
    album_title = models.CharField(max_length=500)
    genre = models.CharField(max_length=100)
    album_logo = models.FileField()
    is_favorite = models.BooleanField(default=False)

    def get_absolute_url(self):
        return reverse('music:detail', kwargs={'pk': self.pk})

    def __str__(self):
        return self.artist + ' - ' + self.album_title


# on delete - means that if(for some reason) the album table gets deleted,
# the songs linked to that table will be deleted as well
class Song(models.Model):
    album = models.ForeignKey(Album, on_delete=models.CASCADE)
    file_type = models.CharField(max_length=10)
    song_title = models.CharField(max_length=250)
    is_favorite = models.BooleanField(default=False)
    audio_file = models.FileField(default=None)

    # redirect to the last page. using album's pk.
    def get_absolute_url(self):
        return reverse('music:detail', kwargs={'pk': self.album.pk})

    def __str__(self):
        return "Album {}, Song {}".format(self.album, self.song_title)
