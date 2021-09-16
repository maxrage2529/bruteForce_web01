from django.db import models
from django.contrib.auth.models import User
from tinymce.models import HTMLField


NOTES_TYPE = (
    ("PR","PRIVATE"),
    ("PU","PUBLIC")
    )
# Create your models here.
class Note(models.Model) :
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    created_on = models.DateTimeField(auto_now_add=True)
    notes_type = models.CharField(max_length=255,choices=NOTES_TYPE,default="PR")
    contributors = models.ManyToManyField(User,blank=True,related_name="note_contributors")
    
    def __str__(self):
        return f"{self.user.username}-{self.title[:20]}.."
    
class NotePages(models.Model) :
    note = models.ForeignKey(Note,on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    content = HTMLField(blank=True,null=True)
    created_on = models.DateTimeField(auto_now_add=True)
    