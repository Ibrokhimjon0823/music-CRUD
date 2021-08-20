from django.urls import path
from django.urls.conf import include
from .views import SongListView2,SongView, SongDetail
urlpatterns = [
    path('',SongView.as_view(),name = "song-list"),
    path('<int:pk>/',SongDetail.as_view(),name = "song-details"),
]