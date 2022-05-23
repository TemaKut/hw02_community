from django.shortcuts import render, get_object_or_404
from .models import Post, Group


def index(request):
    posts_index = Post.objects.order_by('-pub_date')[:10]
    context = {
        'title': "Это главная страница проекта Yatube",
        'posts': posts_index
    }
    return render(request, "posts/index.html", context)


def group_posts(request, slug):

    group = get_object_or_404(Group, slug=slug)
    posts = Post.objects.filter(group=group).order_by('-pub_date')[:10]

    context_group = {
        'group': group,
        'posts': posts,
    }
    return render(request, "posts/group_list.html", context_group)
