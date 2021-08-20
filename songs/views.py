from songs.models import Artist
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Artist,Song
from .serializers import SongSerializer
from rest_framework import generics, serializers
from rest_framework import status
from django.http import Http404

class SongView(APIView):

    def get(self,request):
        songs = Song.objects.all()

        serializer = SongSerializer(songs,many=True)
        return Response(serializer.data)
    
    def post(self,request):
        serializer = SongSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data,status=status.HTTP_201_CREATED)




class SongDetail(APIView):
    """
    Retrieve, update or delete a snippet instance.
    """
    def get_object(self, pk):
        try:
            return Song.objects.get(pk=pk)
        except Song.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        song = Song.objects.get(pk=pk)
        serializer = SongSerializer(song)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        song = Song.objects.get(pk=pk)
        serializer = SongSerializer(song, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        song = Song.objects.get(pk=pk)
        song.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)



class SongListView2(generics.ListAPIView):
    queryset = Song.objects.all()
    serializer_class = SongSerializer

    def list(self, request, *args, **kwargs):
        queryset = Song.objects.filter(title__icontains="a")

        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)