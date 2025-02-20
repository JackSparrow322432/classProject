from django.shortcuts import render, redirect, get_object_or_404
from .models import Thread, Post

def redirect_to_threads(request):
    return redirect('thread-list')

def thread_list(request):
    threads = Thread.objects.all()
    return render(request, 'post/thread_list.html', {'threads': threads})

def thread_detail(request, id):
    thread = get_object_or_404(Thread, id=id)
    return render(request, 'post/thread_detail.html', {'thread': thread})

def thread_delete(request, id):
    thread = get_object_or_404(Thread, id=id)
    thread.delete()
    return redirect('thread-list')

def thread_edit(request, id):
    thread = get_object_or_404(Thread, id=id)
    if request.method == 'POST':
        thread.name = request.POST.get('name')
        thread.description = request.POST.get('description')
        thread.save()
        return redirect('thread-detail', id=id)
    return render(request, 'post/thread_edit.html', {'thread': thread})

def post_delete(request, id):
    post = get_object_or_404(Post, id=id)
    thread_id = post.thread.id
    post.delete()
    return redirect('thread-detail', id=thread_id)

def post_edit(request, id):
    post = get_object_or_404(Post, id=id)
    if request.method == 'POST':
        post.title = request.POST.get('title')
        post.description = request.POST.get('description')
        post.author = request.POST.get('author')
        if 'picture' in request.FILES:
            post.picture = request.FILES['picture']
        post.save()
        return redirect('thread-detail', id=post.thread.id)
    return render(request, 'post/post_edit.html', {'post': post})

