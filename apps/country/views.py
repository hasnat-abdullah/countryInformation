from django.shortcuts import render
from .models import *
#from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
# specific to this view
from django.views.generic import ListView,DetailView
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage

from logs.log import *


class IndexView(ListView):
    """"""
    model = CountryInfo
    template_name = 'index.html'
    context_object_name = 'countries'
    fields = ('name', 'alphacode2','capital','population','timezones','flag')
    paginate_by = 20

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        countries = self.get_queryset()
        page = self.request.GET.get('page')
        paginator = Paginator(countries, self.paginate_by)
        try:
            countries = paginator.page(page)
        except PageNotAnInteger:
            # logger
            Log.info("Warning| Page number is not an integer", self.request)
            countries = paginator.page(1)
        except EmptyPage:
            # logger
            Log.info("Warning| Empty page", self.request)
            countries = paginator.page(paginator.num_pages)
        context['countries'] = countries
        # logger
        Log.info("Success| Successfully returned.", self.request)
        return context


class CountryDetailView(DetailView):
    """"""
    model = CountryInfo
    template_name = 'country_details.html'
    context_object_name = 'country'
