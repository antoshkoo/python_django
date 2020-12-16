from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.views import View
from django.views.generic import DetailView, ListView

from .forms import NewsForm, NewsCommentsForm
from .models import News, NewsComments


class NewsListView(ListView):
    model = News
    context_object_name = 'news_list'


class NewsDetailView(DetailView):
    model = News
    context_object_name = 'news'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        comment_form = NewsCommentsForm
        context['comment_form'] = comment_form
        return context


class NewsCreateFormView(View):

    def get(self, request):
        news_form = NewsForm()
        return render(request, 'news_app/news_create.html', context={'news_form': news_form})

    def post(self, request):
        news_form = NewsForm(request.POST)

        if news_form.is_valid():
            News.objects.create(**news_form.cleaned_data)
            return HttpResponseRedirect(reverse('news-list'))


class NewsEditFormView(View):

    def get(self, request, news_id):
        news = News.objects.get(id=news_id)
        news_form = NewsForm(instance=news)
        return render(request, 'news_app/news_edit.html', context={'news_form': news_form, 'news_id': news_id})

    def post(self, request, news_id):
        news = News.objects.get(id=news_id)
        news_form = NewsForm(request.POST, instance=news)

        if news_form.is_valid():
            news.save()
        return HttpResponseRedirect(reverse('news-detail', args=[news_id]))


class NewsCommentsFormView(View):

    def post(self, request, news_id):
        comment_form = NewsCommentsForm(request.POST)
        if comment_form.is_valid():
            NewsComments.objects.create(**comment_form.cleaned_data)
            return HttpResponseRedirect(reverse('news-detail', args=[news_id]))
