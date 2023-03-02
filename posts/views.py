from django.shortcuts import render, redirect
from posts.models import Posts, Comment
from posts.forms import PostCreateForm, CommentCreateForm
from posts.constants import PAGINATION_LIMIT


# Create your views here.


def main_page_view(request):
    if request.method == 'GET':
        return render(request, 'layouts/index.html')


def posts_view(request):
    if request.method == 'GET':
        posts = Posts.objects.all().order_by('-created_date')
        search = request.GET.get('search')
        page = int(request.GET.get('page', 1))

        if search:
            posts = posts.filter(title__contains=search) | posts.filter(description__contains=search)

        max_page = posts.__len__() / PAGINATION_LIMIT
        if round(max_page) < max_page:
            max_page = round(max_page) + 1
        else:
            max_page = round(max_page)

        posts = posts[PAGINATION_LIMIT * (page - 1): PAGINATION_LIMIT * page]

        context = {
            'posts': [
                {
                    'id': post.id,
                    'title': post.title,
                    'rate': post.rate,
                    'image': post.image,
                    'hashtags': post.hashtags.all
                }
                for post in posts
            ],
            'user': request.user,
            'pages': range(1, max_page+1)
        }

        return render(request, 'posts/posts.html', context=context)


def post_detail_view(request, id):
    if request.method == 'GET':
        post = Posts.objects.get(id=id)

        context = {
            'post': post,
            'comments': post.comments.all(),
            'form': CommentCreateForm
        }

        return render(request, 'posts/detail.html', context=context)

    if request.method == 'POST':
        data = request.POST
        form = CommentCreateForm(data=data)
        post = Posts.objects.get(id=id)

        if form.is_valid():
            Comment.objects.create(
                text=form.cleaned_data.get('text'),
                post=post
            )

        context = {
            'post': post,
            'comment': post.comments.all(),
            'form': form
        }

        return render(request, 'posts/detail.html', context=context)


def create_post_view(request):
    if request.method == 'GET':
        context = {
            'form': PostCreateForm
        }

        return render(request, 'posts/create.html', context=context)

    if request.method == 'POST':
        data, files = request.POST, request.FILES

        form = PostCreateForm(data, files)

        if form.is_valid():
            Posts.objects.create(
                image=form.cleaned_data.get('image'),
                title=form.cleaned_data.get('title'),
                description=form.cleaned_data.get('description'),
                rate=form.cleaned_data.get('rate')
            )
            return redirect('/posts')

        return render(request, 'posts/create.html', context={
            'form': form
        })