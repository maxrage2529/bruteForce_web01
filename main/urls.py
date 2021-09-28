from django.urls import path
from django.views.generic import TemplateView
from .views import (
    MainPage,
    ListNotes, 
    DisplayNotes,
    CreateNotes,
    DeleteNotes,
    UpdateNotes,
    DisplayNotesPages,
    CreateNotesPage,
    UpdateNotesPage,
    DeleteNotesPage
)

urlpatterns = [
    path("", MainPage, name="home"),
    path("dashboard/", ListNotes.as_view(), name="dashboard"),
    path("notes/<int:pk>/", DisplayNotes.as_view(), name="display_notes"),
    path("notes/create/", CreateNotes, name="create_notes"),
    path("notes/update/<int:id>", UpdateNotes, name="update_notes"),
    path("notes/delete/<int:id>", DeleteNotes, name="delete_notes"),
    path("notes/page/<int:pk>/", DisplayNotesPages, name="display_notes_page"),
    path("notes/page/create/", CreateNotesPage, name="create_notes_page"),
    path("notes/page/update/<int:id>", UpdateNotesPage, name="update_notes_page"),
    path("notes/page/delete/", DeleteNotesPage, name="delete_notes_page"),
]