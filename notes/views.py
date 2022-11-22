from django.shortcuts import render
from django.http import Http404
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Notes
from .serializers import NotesSerializer

# Create your views here.
class NotesView(APIView):
    def get(self, request):
        notes = Notes.objects.all()
        serializer = NotesSerializer(notes, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = NotesSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

class GroupNotesView(APIView):
    def get(self, request, category):
        notes = Notes.objects.filter(category=category)
        serializer = NotesSerializer(notes, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

class NotesDetailsView(APIView):
    def get_note_by_id(self, id):
        try:
            return Notes.objects.get(id=id)
        except Notes.DoesNotExist:
            raise Http404

    def get(self, request, id, format=None):
        note = self.get_note_by_id(id)
        print(note)
        serializer = NotesSerializer(note)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def put(self, request, id, format=None):
        note = self.get_note_by_id(id)
        serializer = NotesSerializer(note, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.error, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id, format=None):
        note = self.get_note_by_id(id)
        note.delete()
        return Response(note.id, status=status.HTTP_204_NO_CONTENT)



