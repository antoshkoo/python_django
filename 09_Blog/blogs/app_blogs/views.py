from _csv import reader

from django.contrib.admin.views.decorators import staff_member_required
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.utils import timezone
from django.utils.decorators import method_decorator

from django.views.generic import ListView, DetailView, CreateView

from .forms import PostForm, PostFileUpload
from .models import Post, Gallery


class PostListView(ListView):
    model = Post
    queryset = Post.objects.filter(pub_date__lte=timezone.now())


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

    def post(self, request, *args, **kwargs):
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.user = self.request.user
            obj.save()
            if request.FILES:
                for f in request.FILES.getlist('files'):
                    fl = Gallery(post=obj, image=f)
                    fl.save()
            return redirect('posts_list_url')


@staff_member_required(login_url='login_url')
def post_upload(request):
    if request.method == 'POST':
        form = PostFileUpload(request.POST, request.FILES)
        if form.is_valid():
            file = form.cleaned_data['file'].read()
            file_str = file.decode('utf-8').split('\n')
            csv_reader = reader(file_str, delimiter=',', quotechar='"')
            new_posts = 0
            for col in csv_reader:
                Post.objects.create(user_id=request.user.id, title=col[0], body=col[1], pub_date=f'{col[2]}')
                new_posts += 1
            return HttpResponse(content=f'Записей добавлено: {new_posts}', status=200)

    else:
        form = PostFileUpload
    return render(request, 'app_blogs/post_upload.html', context={'form': form})
