from typing import Any, Dict

from django.shortcuts import render, get_object_or_404
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.urls import reverse_lazy


from .models import Run, Hypothesis


def index(request):
    context = {
    }

    return render(request, 'experiments/index.html', context=context)


class PageTitleMixin():
    page_title = ''

    def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context["page_title"] = self.page_title
        return  context


class BrowseView(PageTitleMixin, ListView):
    model = Hypothesis
    success_url = reverse_lazy('browse')
    # paginate_by = 10
    page_title = "Browse"
    pk_url_kwarg = 'id'

    def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
        context = super().get_context_data(**kwargs)
        _id = self.kwargs.get('id')

        if _id:
            context["runs"] = Run.objects.filter(hypothesis__id=_id)
            
            obj1 = Run.objects.first()

            context["trace1_data"] = {
              "x": obj1.scalars["x"],
              "y": obj1.scalars["y"],
              "mode": "lines",
              "name": "Fair", 
              "type": "scatter"
            };

        return context


class RunDetailView(PageTitleMixin, DetailView):
    template_name = 'experiments/run.html'
    model = Run
    context_object_name = "run"
    pk_url_kwarg = 'id'
    page_title = "Run Detail"

    def get_object(self, **kwargs):
        _id = self.kwargs.get('id')
        return get_object_or_404(Run, id=str(_id))


