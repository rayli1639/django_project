from django.shortcuts import render
from django.http import HttpResponse

posts = [
    {
        'author': 'Raymond',
        'title': 'My Story',
        'content': 'First Post Content',
        'date_posted': 'May 24, 2020'
    },
    {
        'author': 'Joe',
        'title': 'Joe\'s Story',
        'content': 'Joe First Post Content',
        'date_posted': 'May 25, 2020'
    }
]

def home(request):
    context = {'posts': posts}
    return render(request, 'blog/home.html', context) 

def about(request):
    context = {'title': 'About'}
    return render(request, 'blog/about.html', context)
