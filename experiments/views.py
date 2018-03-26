from django.views.generic.list import ListView

from .models import Experiment


class ExperimentListView(ListView):
    model = Experiment