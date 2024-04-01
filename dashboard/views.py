from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from blog.models import Post, Category

# Create your views here.


@login_required
def index(request):
    post = Post.objects.filter(create_by=request.user)
    categories = Category.objects.all()

    return render(request, 'dashboard/index.html', context={
        'posts': post,
        'categories': categories,
    })


@login_required
def delete(request, pk):
    post = get_object_or_404(Post, pk=pk, create_by=request.user)
    post.delete()
    
    return redirect('/dashboard/')
