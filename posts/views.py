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
            'posts': [
                {
                    'id' : post.id,
                    'title' : post.title,
                    'rate' : post.rate,
                    'image' : post.image,
                    'hashtags' : post.hashtags.all
        }
        for post in posts
    ]
}

        return render(request, 'posts/posts.html', context=context)


def post_detail_view(request, id):
    if request.method == 'GET':
       post = Posts.objects.get(id=id)

       context = {
           'post': post,
           'comments': post.comments.all()
       }

       return render(request, 'posts/detail.html', context=context)
