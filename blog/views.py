from django.shortcuts import render

from .models import Post

# Create your views here.

def index(request):
    latest_post_list = Post.objects.order_by('-date')[:15]
    context = {'latest_post_list': latest_post_list}
    return render(request, 'blog/index.html', context)


def detail(request, post_id):
    return HttpResponse("You're looking at post %s." % post_id)
