from turtle import pos, title
from unicodedata import category
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render, get_object_or_404
from django.http import HttpResponse
from .models import Category, Post, Comment
from .froms import SignupForm, AddPost, EditPost, AddComment


# def say_hello(request):
#     return HttpResponse("hello word")

def say_hello(request):
    x = 1
    return render(request, "hello.html", {'name': "quoc"})


def index(request):
    post = Post.objects.all()
    categories = Category.objects.all()
    return render(request, "index.html", context={
        'posts': post,
        'categories': categories,
    })


def detail_post(request, pk):
    
    form = AddComment()
    post = get_object_or_404(Post, pk=pk)
    comments = Comment.objects.filter(post=post)
    related_post = Post.objects.filter(
        category=post.category).exclude(pk=pk)[0:3]
    

    return render(request, "detail_post.html", {
        'related_post': related_post,
        'post': post,
        'form': form,
        'comments': comments
        
    })


@login_required
def add_post(request):
    if request.method == 'POST':
        form = AddPost(request.POST, request.FILES)
        # print(request.POST, request.FILES)

        if form.is_valid():
            post = form.save(commit=False)
            post.create_by = request.user
            post.save()

            return redirect(f'/blog/detail-post/{post.id}')
    else:
        form = AddPost()

    return render(request, "add_post.html", {
        'title': "Add Post",
        'form': form
    })


@login_required
def edit_post(request, pk):
    post = get_object_or_404(Post, pk=pk, create_by=request.user)

    if request.method == "POST":
        form = EditPost(request.POST, request.FILES, instance=post)

        if form.is_valid():
            form.save()

            return redirect(f'/blog/detail-post/{pk}')
    else:
        form = EditPost(instance=post)

    return render(request, "add_post.html", {
        'title': "Edit",
        'form': form
    })


def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)

        if form.is_valid():
            form.save()

            return redirect('/blog/login/')
    else:
        form = SignupForm()

    return render(request, 'signup.html', {
        'form': form
    })


def search(request):
    category = request.GET.get('category', '')
    query = request.GET.get('query', '')
    post = Post.objects.all()
    categories = Category.objects.all()

    if query:
        post = post.filter(title__icontains=query)
        
    if category:
        post = post.filter(category__name__icontains=category)

    return render(request, "index.html", context={
        'posts': post,
        'categories': categories,
    })
    
@login_required    
def add_comment(request, pk):
    if request.method == 'POST':
        form = AddComment(request.POST)
        
        if form.is_valid():
            post = get_object_or_404(Post, pk=pk)
            comment = form.save(commit=False)
            comment.user = request.user
            comment.post = post
            comment.save()
            
            return redirect(f'/blog/detail-post/{pk}')
        
        
