from django.db import models
from django.utils.translation import gettext as _


class Note(models.Model):
    title = models.CharField(max_length=100, unique= True, help_text=_("The title of the Note."))
    writer = models.ForeignKey("accounts.CustomUser", on_delete= models.CASCADE, help_text=_("Author of the note"))
    published_at = models.DateTimeField(auto_now_add= True, help_text=_("publishing date"))
    body = models.TextField(help_text=_("Main blog"))
    draft = models.BooleanField(default= False, help_text=_("Draft or published note"))
    updated_at = models.DateTimeField(auto_now= True, help_text=_("Edited and published at"))
    hidden = models.BooleanField(default= False, help_text=_("the file is hidden or private if set to true "))

    class Meta:
        ordering = ['-published_at']

    def __str__(self):
        return self.title
