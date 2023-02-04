from django.urls import path
from .views import (
    NotesView, 
    GroupNotesView, 
    NotesDetailsView, 
    CreateNoteView
)

urlpatterns = [
    path('', NotesView.as_view()),
    path('create/', CreateNoteView.as_view()),
    path('<str:category>/', GroupNotesView.as_view()),
    path('<int:pk>/', NotesDetailsView.as_view()),
    
]

