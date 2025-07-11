from django.shortcuts import render, get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.http import HttpResponse
from .models import Post
from django.contrib.auth.models import User
from django.views.generic import (
ListView, 
DetailView, 
CreateView,
UpdateView,
DeleteView
)

# posts = [
#     {
#         "title": "Blog post 1",
#         "author": "Corey MS",
#         "content": "lorem ipsum...",
#         "date_posted": "2 June 2025"
#     },
#         {
#         "title": "Blog post 2",
#         "author": "John Doe",
#         "content": "some random contents....",
#         "date_posted": "12 March 2025"
#     },
# ]

# Create your views here.
def home(request):
    context = {
        "posts": Post.objects.all()
    }
    return render(request, "blog/home.html", context )

class PostListView(ListView):
    model = Post
    template_name = 'blog/home.html' #<app>/<model>_<viewtype>.html
    context_object_name = 'posts'
    ordering = ['-date_posted']
    paginate_by=5
    
class UserPostListView(ListView):
    model = Post
    template_name = 'blog/user_posts.html'  # <app>/<model>_<viewtype>.html
    context_object_name = 'posts'
    paginate_by = 5

    def get_queryset(self):
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        return Post.objects.filter(author=user).order_by('-date_posted')
    
class PostDetailView(DetailView):
    model = Post
    
class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    fields=['title', 'content']
    
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
    
class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    fields=['title', 'content']
    
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
    
    def test_func(self):
        post = self.get_object()
        
        if self.request.user == post.author:
            return True
        else:
            return False

class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    
    def test_func(self):
        post = self.get_object()
        
        if self.request.user == post.author:
            return True
        else:
            return False
    success_url= '/'
        
def about(request):
    return render(request, "blog/about.html", {"title": "about"})

