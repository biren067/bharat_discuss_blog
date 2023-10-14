from django.shortcuts import render, HttpResponse
from .models import Post

posts = [
    {
        'author': 'CoreyMS',
        'title': 'Blog post 1',
        'content': 'First post content',
        'date_posted': 'August 23, 2018'
    },
    {
        'author': 'Jane Doe',
        'title': 'Blog post 2',
        'content': 'Second post content',
        'date_posted': 'August 27, 2018'
    }
]


def get_post(request):
    # return HttpResponse("<h1>Welcome to new Blog</h1>")
    context = {'posts': Post.objects.all(), 'title': 'Django Blog'}

    return render(request, template_name='blog/home.html', context=context)


def about(request):
    # return HttpResponse("<h1> It is our About page</h1>")
    return render(request, template_name='blog/about.html', context={'name': 'birendra', 'title': "About"})
