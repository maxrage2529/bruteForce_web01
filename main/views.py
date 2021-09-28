from django.shortcuts import render, HttpResponse, get_object_or_404, redirect
from django.views.generic import ListView, DetailView, CreateView, DeleteView
from .models import Note, NotePages
from django.http import JsonResponse
from django.urls import reverse

from django.views.decorators.http import require_http_methods
from django.contrib.auth.decorators import  login_required
from django.contrib.auth.mixins import  LoginRequiredMixin
from django.views.decorators.clickjacking import xframe_options_exempt
from django.utils.decorators import method_decorator

# Create your views here.

def MainPage(request) :
    if request.user.is_authenticated:
        return redirect(reverse("dashboard"))
    return render(request,"main/index.html")

class ListNotes(LoginRequiredMixin,ListView):
    model = Note
    template_name = "main/dashboard.html"

    def get_queryset(self):
        return Note.objects.filter(user=self.request.user)


class DisplayNotes(DetailView):
    model = Note
    template_name = "main/notes_page.html"


@require_http_methods(["POST"])
@login_required
def CreateNotes(request):
    if request.method == "POST":
        title = request.POST.get("title", None)
        user = request.user
        Notes = Note.objects.create(title=title, user=user)
        Notes.save()
        return redirect(reverse("display_notes",kwargs={"pk":Notes.id}))

@login_required
def DeleteNotes(request, id):
    Notes = get_object_or_404(Note, pk=id)
    id = Notes.pk
    Notes.delete()
    return redirect(reverse("dashboard"))

@require_http_methods(["POST"])
@login_required
def UpdateNotes(request,id) :
    if request.method == "POST" :
        title = request.POST.get("title",None)
        notes_type = request.POST.get("notes_type",None)
        Notes = Note.objects.get(id=id)
        Notes.title = title if title else Notes.title
        Notes.notes_type = notes_type if notes_type else Notes.notes_type
        Notes.save()
        return HttpResponse("success")

'''@method_decorator(xframe_options_exempt, name='dispatch')
class DisplayNotesPages(DetailView) :
    model = NotePages
    template_name = "main/notes_page_detail.html"'''


def DisplayNotesPages(request, pk):
    Page = get_object_or_404(NotePages, pk=pk)
    title = Page.title
    content = Page.content
    context = {"title": title, "content": content}
    return JsonResponse(context)


@require_http_methods(["POST"])
@login_required
def CreateNotesPage(request):
    if request.method == "POST":
        title = request.POST.get("title", None)
        note = Note.objects.get(id=request.POST.get("note_id"))
        Page = NotePages.objects.create(title=title, note=note)
        Page.save()
        return HttpResponse(content=Page.id)


@require_http_methods(["POST"])
@login_required
def UpdateNotesPage(request, id):
    if request.method == "POST":
        title = request.POST.get("title",None)
        content = request.POST.get("content", None)
        Page = get_object_or_404(NotePages, pk=id)
        Page.title = title if title else Page.title
        Page.content = content if content else Page.content
        Page.save()
        return HttpResponse(content="success")
    
    
@require_http_methods(["POST"])
@login_required
def DeleteNotesPage(request):
    if (request.method == "POST") :
        id = request.POST.get("id")
        Page = get_object_or_404(NotePages, pk=id)
        id = Page.pk
        Page.delete()
        return HttpResponse(content=id)