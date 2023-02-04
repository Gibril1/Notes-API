from rest_framework import status
from rest_framework.generics import ListAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import BasePermission, IsAuthenticated, SAFE_METHODS
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Notes
from .serializers import NotesSerializer

class UserEditDeletePermission(BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in SAFE_METHODS:
            return True
        return obj.student == request.user


class NotesView(ListAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Notes.objects.all()
    serializer_class = NotesSerializer

class NotesDetailsView(RetrieveUpdateDestroyAPIView):
    permission_classes = [UserEditDeletePermission]
    queryset = Notes.objects.all()
    serializer_class = NotesSerializer


class CreateNoteView(APIView):
    def post(self, request):
        serializer = NotesSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(student = request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class GroupNotesView(APIView):
    permission_classes = [IsAuthenticated]
    def get(self, request, category):
        notes = Notes.objects.filter(category=category).filter(student=request.user).all()
        serializer = NotesSerializer(notes, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)



