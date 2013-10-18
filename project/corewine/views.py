from django.shortcuts import render
from django.views.generic.edit import FormView

from .forms import WineForm
from .models import Wine, Cepage

from rest_framework.generics import (
	ListCreateAPIView,
	RetrieveUpdateDestroyAPIView
)


def index(request):
    return render(request, 'corewine/index.html')


class TastingView(FormView):
    template_name = 'corewine/tasting.html'
    form_class = WineForm
    success_url = '/wine'

    def form_valid(self, form):
        form.save()
        return super(TastingView, self).form_valid(form)


class CepageCreateReadView(ListCreateAPIView):
	model = Cepage
	


