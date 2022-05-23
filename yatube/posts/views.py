from django.shortcuts import render, get_object_or_404

from .models import Post, Group


MAX_POST_COUNT = 10


def index(request):
    posts_index = Post.objects.order_by('-pub_date')[:MAX_POST_COUNT]
    context = {
        'posts': posts_index,
    }

    return render(request, "posts/index.html", context)


def group_posts(request, slug):
    group = get_object_or_404(Group, slug=slug)
    posts = (Post.objects.filter(group=group)
             .order_by('-pub_date')[:MAX_POST_COUNT])

    context_group = {
        'group': group,
        'posts': posts,
    }
    return render(request, "posts/group_list.html", context_group)
