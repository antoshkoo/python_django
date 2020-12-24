from django.contrib.auth.decorators import permission_required, login_required
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.utils.decorators import method_decorator
from django.views import View
from django.views.generic import DetailView, ListView

from .forms import NewsForm, NewsCommentsForm
from .models import News, NewsComments, NewsTags
from users.models import Profile


class NewsListView(View):
    model = News

    def get(self, request):
        tags = NewsTags.objects.all()
        tag = self.request.GET.get('tag', False)
        order_by = self.request.GET.get('order_by', False)
        order = '-created_at' if order_by == 'ASC' else 'created_at'
        if tag and order_by:
            queryset = News.objects.filter(tags__slug=tag, is_active=1).order_by(order)
        elif tag:
            queryset = News.objects.filter(tags__slug=tag, is_active=1)
        elif order_by:
            queryset = News.objects.filter(is_active=1).order_by(order)
        else:
            queryset = News.objects.filter(is_active=1)

        return render(request, 'news_app/news_list.html', context={
            'news_list': queryset,
            'tags': tags,
        })


class NewsDetailView(DetailView):
    model = News
    context_object_name = 'news'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        comment_form = NewsCommentsForm
        context['comment_form'] = comment_form
        return context


class NewsTagsListView(ListView):
    model = NewsTags
    context_object_name = 'tags_list'


class NewsTagsDetailView(DetailView):
    model = NewsTags

    def get(self, request, slug):
        tag = NewsTags.objects.get(slug=slug)
        return render(request, 'news_app/newstags_detail.html', context={'tag': tag})


@method_decorator(permission_required('news_app.add_news'), name="dispatch")
class NewsCreateFormView(View):

    def get(self, request):
        news_form = NewsForm()
        return render(request, 'news_app/news_create.html', context={'news_form': news_form})

    def post(self, request):
        news_form = NewsForm(request.POST)

        if news_form.is_valid():
            News.objects.create(**news_form.cleaned_data)
            current_user = Profile.objects.get(user_id=request.user.id)
            current_user.news_count += 1
            current_user.save()
        return HttpResponseRedirect(reverse('news-list'))


@method_decorator(permission_required('news_app.change_news'), name="dispatch")
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
