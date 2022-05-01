import numpy as np
from django.core.management.base import BaseCommand

from experiments.models import Project, Hypothesis, Run, RLRun


class Command(BaseCommand):

    def handle(self, *args, **kwargs):
        # Create project
        Project.objects.get_or_create(
                name="NoisedLines", 
                description="Comparison of random noises. Test case."
        )
        self._add_noised_lines()
        self._add_sin_lines()

    def _add_noised_lines(self):
        hyp, _ = Hypothesis.objects.get_or_create(name="Noised Lines")

        # Create experiments
        system_data = {"CPU": "Intel i5", "RAM": "2GB"}
        x = np.arange(0, 10, 0.1)
        for i, sigma in enumerate([0.1, 0.5, 1, 2, 3]):
            scalar_data = {
                    "x": x.tolist(),
                    "y": (x + np.random.randn(x.size) * sigma).tolist()
            }
            Run.objects.get_or_create(
                name=f"noised_line",
                hypothesis=hyp,
                scalars=scalar_data,
                system=system_data,
                seed=i,
            )

    def _add_sin_lines(self):
        hyp, _ = Hypothesis.objects.get_or_create(name="Sin Lines")

        # Create experiments
        system_data = {"CPU": "Intel i5", "RAM": "2GB"}
        x = np.arange(0, 10, 0.1)
        for i, ar in enumerate([0.1, 0.5, 1, 2, 3]):
            scalar_data = {
                    "x": x.tolist(),
                    "y": np.sin(x * ar).tolist()
            }
            Run.objects.get_or_create(
                name=f"sin_line",
                hypothesis=hyp,
                scalars=scalar_data,
                system=system_data,
                seed=i,
            )
