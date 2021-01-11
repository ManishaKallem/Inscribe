from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm


class RequiredFieldsMixin:
    """This can be used as a mixin in forms to easily specify which fields
    are required through the ``required_fields`` attribute, in the ``Meta``
    class. Excluded fields are not touched."""

    def __init__(self, *args, **kwargs):

        super().__init__(*args, **kwargs)

        required_fields = getattr(self.Meta, "required_fields", None)
        if required_fields:
            if required_fields == "__all__":
                for key in self.fields:
                    self.fields[key].required = True
            for key in self.fields:
                if key in required_fields:
                    self.fields[key].required = True


class RegistrationForm(RequiredFieldsMixin, UserCreationForm):
    class Meta:
        model = get_user_model()
        fields = [
            "username",
            "first_name",
            "last_name",
            "email",
            "password1",
            "password2",
        ]
        required_fields = "__all__"

        def save(self, commit=True):
            user = super(RegistrationForm, self).save(commit=False)
            if commit:
                user.save()
            return user
