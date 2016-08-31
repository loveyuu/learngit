from django.shortcuts import render

from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from .models import Blog


def index(request):
    blog_list = Blog.objects.all()
    paginator = Paginator(blog_list, 2)
    page = request.GET.get('page')
    try:
        show_lines = paginator.page(page)
    except PageNotAnInteger:
        show_lines = paginator.page(1)
    except EmptyPage:
        show_lines = paginator.page(paginator.num_pages)
    return render(request, 'index.html', {'show_lines': show_lines})
