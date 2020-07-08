from django.views import generic
from .models import Album, Song
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.views.generic import View
from django.http import HttpResponseRedirect
from .forms import UserForm


class IndexView(generic.ListView):
    template_name = 'music/index.html'
    context_object_name = 'all_albums'

    def get_queryset(self):
        return Album.objects.all()

# were not getting a list of objects so all we need to say is what object we try to get the detail of - Album
# and the next thing is the template name - plug it into the temlate we defining.


class DetailsView(generic.DetailView):
    model = Album
    template_name = 'music/details.html'

# not a good way to do this. making generic views


class AlbumCreate(CreateView):
    model = Album
    fields = ['artist', 'album_title', 'genre', 'album_logo']


class AlbumUpdate(UpdateView):
    model = Album
    fields = ['artist', 'album_title', 'genre', 'album_logo']


class AlbumDelete(DeleteView):
    model = Album
    success_url = reverse_lazy('music:index')


class UserFormView(View):
    form_class = UserForm
    template_name = 'music/registration_form.html'

    # display a blank form
    def get(self, request):
        form = self.form_class(None)
        return render(request, self.template_name, {'form': form})

    # process form data
    def post(self, request):
        form = self.form_class(request.POST)

        if form.is_valid():
            user = form.save(commit=False)

            # cleaned (normalized) data
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user.set_password(password)
            user.save()

            # returns User objects if credentials are correct
            user = authenticate(username=username, password=password)

            if user is not None:
                if user.is_active:
                    login(request, user)

        return render(request, self.template_name, {'form': form})


def logout_view(request):
    logout(request)
    return redirect('music:index')


class SongAdd(CreateView):
    model = Song
    fields = ['album', 'file_type', 'song_title', 'audio_file']

    def get_absolute_url(self, request):
        return redirect('music/details.html')


class Songs(generic.ListView):
    song_model = Song
    template_name = 'music/songs.html'
    context_object_name = 'all_songs'

    def get_queryset(self):
        return self.song_model.objects.all()


def favorite(request, pk):
    template_name = 'music:index'

    for album in Album.objects.all():
        if album.id == pk:
            if not album.is_favorite:
                album.is_favorite = True
                album.save()
                return HttpResponseRedirect(reverse_lazy(template_name))

            else:
                album.is_favorite = False
                album.save()
                return HttpResponseRedirect(reverse_lazy(template_name))


def song_favorite(request, pk):
    template_name = 'music:songs'

    for song in Song.objects.all():
        if song.id == pk:
            if not song.is_favorite:
                song.is_favorite = True
                song.save()
                return HttpResponseRedirect(reverse_lazy(template_name))

            else:
                song.is_favorite = False
                song.save()
                return HttpResponseRedirect(reverse_lazy(template_name))


def song_delete(request, pk):
    template_name = 'music:index'

    song_list = Song.objects.all()
    for song in song_list:
        if song.id == pk:
            song.delete()
            return HttpResponseRedirect(reverse_lazy(template_name))
"""

from music.models import Album, Song
from django.shortcuts import render, get_object_or_404


def index(request):
    all_albums = Album.objects.all()
    context = {'all_albums': all_albums}
    return render(request, 'music/index.html', context)
    # the http response is builtin in that render response. converts it into http response
    # rendering the template function to our web server


def detail(request, album_id):
    # album = Album.objects.get(pk=album_id)
    album = get_object_or_404(Album, pk=album_id)
    return render(request, 'music/details.html', {'all_albums': album})

"""
