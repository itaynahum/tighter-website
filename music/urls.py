from django.urls import path
from . import views

app_name = 'music'
# subprocess of the application!
urlpatterns = [
    # /music/
    path(r'', views.IndexView.as_view(), name='index'),

    # /music/register
    path(r'register/', views.UserFormView.as_view(), name='register'),

    # /music/1/
    path('<int:pk>/', views.DetailsView.as_view(), name='detail'),

    # music/album/add/
    path('album/add/', views.AlbumCreate.as_view(), name='album-add'),

    # music/album/2/
    path('album/<int:pk>/', views.AlbumUpdate.as_view(), name='album-update'),

    # music/album/2/delete/
    path('album/<int:pk>/delete/', views.AlbumDelete.as_view(), name='album-delete'),

    # music/logout/
    path('logout/', views.logout_view, name='logout'),

    # music/song/add/
    path('<int:pk>/song/add/', views.SongAdd.as_view(), name='add-song'),

    # music/songs/
    path('songs/', views.Songs.as_view(), name='songs'),

    # song/favorite/pk
    path('song/favorite/<int:pk>/', views.song_favorite, name='song_favorite'),

    # music/
    path('favorite/<int:pk>/', views.favorite, name='favorite'),

    # music/song/delete/pk
    path('song/delete/<int:pk>/', views.song_delete, name='song_delete')
]
