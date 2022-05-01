from django.core.management.base import BaseCommand

from experiments.models import Project, Hypothesis, Run


class Command(BaseCommand):

    def handle(self, *args, **kwargs):
        Project.objects.all().delete()
        Hypothesis.objects.all().delete()
        Run.objects.all().delete()

