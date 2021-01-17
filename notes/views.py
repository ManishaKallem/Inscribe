from django.views.generic import CreateView, TemplateView

from . import models


# The below view should be a `CreateView` but since the model isn't created, we
# will be using a `TemplateView` instead
class NoteCreateView(TemplateView):
    """ This view will handle the creation of notes, and saving them to the database """

    # model = models.Note
    template_name = "notes/create.html"
