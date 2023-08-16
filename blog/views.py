from django.shortcuts import render, get_object_or_404
from .models import Post
from django.urls import reverse
from django.views import generic, View
from django.utils import timezone
from django.views.generic.detail import SingleObjectMixin
from django.views.generic import FormView
from django.contrib.auth.mixins import LoginRequiredMixin

from blog.forms import PostCommentForm

# Create your views here.

def render_posts(request):
    posts = Post.objects.all()
    return render(request, 'post.html', {'posts': posts})

def post_detail(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    return render(request, 'post_detail.html', {"post": post})

class PostDetailView(generic.DetailView):
    model = Post
    queryset = Post.objects.filter(
        #pub_date__lte = timezone.now()
    )

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = PostCommentForm
        return context

class PostCommentFormView(LoginRequiredMixin, SingleObjectMixin, FormView):
    template_name = 'blog/post.html'
    form_class = PostCommentForm
    model = Post

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        return super().post(request, *args, **kwargs)
    
    def form_valid(self, form):
        f = form.save(comit=False)
        f.author = self.request.user
        f.post = self.object
        f.save()
        return super().form_valid(form)
    
    def get_success_url(self):
        return reverse('blog:post', kwargs={'slug': self.object.slug}) + '#comments-section'


class PostView(View):

    def get(self, request, *args, **kwargs):
        view = PostDetailView.as_view()
        return view (request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        view = PostCommentFormView.as_view()
        return view (request, *args, **kwargs)

