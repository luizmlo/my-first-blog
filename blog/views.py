from django.shortcuts import render
from django.utils import timezone
from .models import Post

def home(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'blog/home.html', {'posts': posts})

def rid_1(request):
    return render(request, 'blog/rid_1.html')

def rid_2(request):
    return render(request, 'blog/rid_2.html')

def rid_3(request):
    return render(request, 'blog/rid_3.html')

def rid_4(request):
    return render(request, 'blog/rid_4.html')

def rid_5(request):
    return render(request, 'blog/rid_5.html')

def rid_6(request):
    return render(request, 'blog/rid_6.html')

def rid_7(request):
    return render(request, 'blog/rid_7.html')

def rid_8(request):
    return render(request, 'blog/rid_8.html')

def rid_9(request):
    return render(request, 'blog/rid_9.html')

def rid_10(request):
    return render(request, 'blog/rid_10.html')