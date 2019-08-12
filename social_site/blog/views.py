from django.shortcuts import render
from blog.models import Post, Comment
from django.contrib.auth.mixins import LoginRequiredMixin
from blog.forms import PostForm, CommentForm
from django.views.generic import (TemplateView,ListView,
                                    DetailView, CreateView,
                                    UpdateView, DeleteView)

class AboutView(TemplateView):
    template_name = "about.html"

class PostListView(ListView):
    model = "Post"

    def get_queryset(self):
        return Post.objects.filter(published_date__lte = timezone.now()).order_by('-published_date'))
        # Equivalent to select * from posts ordered_by published_date in descending order

class PostDetailView(DetailView):
    model = "Post"

class CreatePostView(CreateView, LoginRequiredMixin):
    login_url = '/login/'
    redirect_field_name = '/blog/post_detail.html'

    form_class = PostForm
    model = Post

class PostUpdateView(UpdateView, LoginRequiredMixin):
    login_url = '/login/'
    redirect_field_name = '/blog/post_detail.html'

    form_class = PostForm
    model = Post

class PostDeleteView(DeleteView, LoginRequiredMixin):
    model = Post
    success_url = reverse_lazy('post_list')

class DraftListView(LoginRequiredMixin, ListView):
    login_url = '/login/'
    redirect_field_name = 'blog/post_draft_list.html'
    model = Post

    def get_queryset(self):
        return Post.objects.filter(published_date_isnull = True).order_by('created_date')


# Create your views here.
