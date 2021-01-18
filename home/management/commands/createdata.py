import random

from django.contrib.auth import get_user_model
from django.core.management.base import BaseCommand
from django.utils.translation import gettext
from faker import Faker
from mdgen import MarkdownPostProvider
from notes import models as notes_models


class Command(BaseCommand):

    help = gettext(
        "Create instances of accounts.CustomUser, notes.Note. "
        "By default 15 instances of each are created. Can be changed by passing "
        "the -i argument to the command."
    )

    def add_arguments(self, parser):
        parser.add_argument(
            "-i",
            "--instances",
            default=15,
            dest="instances",
            help=gettext("The number of data instances to be created."),
        )

    def handle(self, *args, **options):
        instances = int(options["instances"])

        fake = Faker()
        fake.add_provider(MarkdownPostProvider)
        CustomUser = get_user_model()

        users = []
        for __ in range(1, instances + 1):
            user = CustomUser.objects.create_user(
                first_name=fake.first_name(),
                last_name=fake.last_name(),
                email=fake.email(),
                password=fake.password(),
            )
            users.append(user)
        self.stdout.write(self.style.SUCCESS(f"\nCreated {instances} custom users"))

        notes = [  # noqa
            notes_models.Note.objects.create(
                title=fake.sentence(),
                writer=random.choice(users),
                updated_at=fake.future_date(),
                body=fake.post(size="large"),
                draft=fake.boolean(chance_of_getting_true=75),
                hidden=fake.boolean(chance_of_getting_true=25),
            )
            for _ in range(instances)
        ]
        self.stdout.write(self.style.SUCCESS(f"\nCreated {instances} notes"))
