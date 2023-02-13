from django.shortcuts import render
from posts.models import Posts

# Create your views here.


def main_page_view(request):
    if request.method == 'GET':
        return render(request, 'layouts/index.html')


def posts_view(request):
    if request.method == 'GET':
        posts = Posts.objects.all()

        context = {
            'posts': posts
        }

        return render(request, 'posts/posts.html', context=context)
