from django.urls import path
from django.views.generic import TemplateView
from .views import (
    ListNotes, 
    DisplayNotes, 
    DisplayNotesPages,
    CreateNotesPage
)

urlpatterns = [
    path("", TemplateView.as_view(template_name="main/index.html"), name="home"),
    path("notes/<int:pk>/", DisplayNotes.as_view(), name="display_notes"),
    path("notes/page/<int:pk>/", DisplayNotesPages, name="display_notes_page"),
    path("notes/page/create/", CreateNotesPage, name="create_notes_page"),
    path("dashboard/", ListNotes.as_view(), name="dashboard"),
]