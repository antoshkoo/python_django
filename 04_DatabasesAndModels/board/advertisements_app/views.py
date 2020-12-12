from django.views.generic import ListView, DetailView

from .models import Advertisement


class AdvertisementListView(ListView):
    model = Advertisement
    queryset = Advertisement.objects.all()[:30]
    context_object_name = 'advertisements'


class AdvertisementDetailView(DetailView):
    model = Advertisement
    context_object_name = 'advertisement'
