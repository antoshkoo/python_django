from django.views.generic import DetailView, ListView

from .models import News, NewsComments


class NewsListView(ListView):
    model = News


class NewsDetailView(DetailView):
    model = News

    comments = NewsComments.objects.filter(news_id=pk)
    extra_context = {'comments': comments}
