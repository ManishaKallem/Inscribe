from django.views.generic import CreateView, ListView, TemplateView

from . import models


# DO NOT DISTRUB
class NoteCreateView(TemplateView):
    """ This view will handle the creation of notes, and saving them to the database """

    template_name = "notes/create.html"


class NotesListView(ListView):
    """ This view will handle displaying all the notes in the database """

    model = models.Note
    template_name = "notes/list.html"
