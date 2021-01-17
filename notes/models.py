from django.db import models
from django.utils.translation import gettext as _


class Note(models.Model):
    title = models.CharField(
        max_length=100, unique=True, help_text=_("The title of the note")
    )
    writer = models.ForeignKey(
        "accounts.CustomUser",
        on_delete=models.CASCADE,
        help_text=_("Author of the note"),
    )
    published_at = models.DateTimeField(
        auto_now_add=True, help_text=_("The date and time the note was published at")
    )
    body = models.TextField(help_text=_("Main body of the note"))
    draft = models.BooleanField(
        default=False,
        help_text=_("Whether the note is a to be saved as a draft or published"),
    )
    updated_at = models.DateTimeField(
        auto_now=True, help_text=_("The date and time the note was updated at")
    )
    hidden = models.BooleanField(
        default=False, help_text=_("Whether the file will be hidden")
    )

    class Meta:
        ordering = ["-published_at"]

    def __str__(self):
        return self.title
