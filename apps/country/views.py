from django.shortcuts import render
from .models import *
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.urls import reverse_lazy
# specific to this view
from django.views.generic import ListView,DetailView,CreateView
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.db.models.query_utils import Q
from django.contrib.auth.forms import UserCreationForm
from logs.log import *


@method_decorator(login_required, name='dispatch')
class IndexView(ListView):
    """List view with country name search & pagination"""
    model = CountryInfo
    template_name = 'index.html'
    context_object_name = 'countries'
    fields = ('name', 'alphacode2','capital','population','timezones','flag')
    paginate_by = 20

    def get_queryset(self):
        query_param = self.request.GET.get("q", None) # get country search query
        if query_param is not None:
            return CountryInfo.objects.filter(Q(name__icontains=query_param)).order_by('name')
        return CountryInfo.objects.all().order_by('name')

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


@method_decorator(login_required, name='dispatch')
class CountryDetailView(DetailView):
    """Country details page view"""
    model = CountryInfo
    template_name = 'country_details.html'
    context_object_name = 'country'


class RegisterView(CreateView):
    """ User creation page view"""
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'register.html'
