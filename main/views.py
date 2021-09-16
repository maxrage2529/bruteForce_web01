from django.shortcuts import render,HttpResponse,get_object_or_404
from django.views.generic import ListView,DetailView,CreateView,DeleteView
from .models import Note,NotePages
from django.http import JsonResponse

from django.views.decorators.http import require_http_methods
from django.views.decorators.clickjacking import xframe_options_exempt
from django.utils.decorators import method_decorator

# Create your views here.

class ListNotes(ListView) :
    model = Note
    template_name = "main/dashboard.html"
    
    def get_queryset(self):
        return Note.objects.filter(user=self.request.user)
    
class DisplayNotes(DetailView) :
    model = Note
    template_name = "main/notes_page.html"

'''@method_decorator(xframe_options_exempt, name='dispatch')
class DisplayNotesPages(DetailView) :
    model = NotePages
    template_name = "main/notes_page_detail.html"'''

def DisplayNotesPages(request,pk) :
    Page = get_object_or_404(NotePages,pk=pk)
    title = Page.title
    content = Page.content
    context = {
        "title" : title,
        "content" : content
    }
    return JsonResponse(context)
    
   
@require_http_methods(["POST"])    
def CreateNotesPage(request) :
    if request.method=="POST" :
        title = request.POST.get("title",None)
        note = Note.objects.get(id=request.POST.get("note_id")) 
        Page = NotePages.objects.create(title = title,note=note)
        Page.save()
        return HttpResponse(content=Page.id)

@require_http_methods(["POST"])
def UpdateNotesPage(request,id) :
    if request.method == "POST" :
        #title = request.POST.get("title")
        content = request.POST.get("content","")
        Page = get_object_or_404(NotePages,pk=id)
        Page.content = content
        Page.save()
        return HttpResponse(content="success")

def DeleteNotesPage(request,id) :
    Page = get_object_or_404(NotePages,pk=id)
    id = Page.pk
    Page.delete()
    return HttpResponse(content=id)