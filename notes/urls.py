from django.urls import path
from .views import NotesView, GroupNotesView, NotesDetailsView

urlpatterns = [
    path('', NotesView.as_view()),
    path('<str:category>/', GroupNotesView.as_view()),
    path('<int:id>/', NotesDetailsView.as_view()),
]

