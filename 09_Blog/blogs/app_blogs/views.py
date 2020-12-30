from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.utils.decorators import method_decorator

from django.views.generic import ListView, DetailView, CreateView

from .forms import PostForm
from .models import Post


class PostListView(ListView):
    model = Post


class PostDetailView(DetailView):
    model = Post


def post_create(request):
    form = PostForm(request.POST, request.FILES)
    if request.method == 'POST':
        pass
    else:
        form = PostForm
    return render(request, 'app_blogs/post_create.html', context={'form': form})


@method_decorator(login_required(login_url='login'), name='dispatch')
class PostCreateView(CreateView):
    model = Post
    form_class = PostForm

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.user = self.request.user
        obj.save()
        return redirect('posts_list_url')
