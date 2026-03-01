from django.shortcuts import render, redirect, get_object_or_404
from .models import Post
from .forms import PostForm

# List all posts
def post_list(request):
    posts = Post.objects.all().order_by('-created_at')
    return render(request, 'list.html', {'posts': posts})

# Create post
def add_post(request):
    form = PostForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('list')
    return render(request, 'form.html', {'form': form})

# View single post
def post_detail(request, id):
    post = get_object_or_404(Post, id=id)
    return render(request, 'detail.html', {'post': post})