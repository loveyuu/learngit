# encoding=utf-8
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout, authenticate, login
from django.http import HttpResponse
from django.http import HttpResponseRedirect

from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.shortcuts import render
from django.views.generic import DetailView
from django.views.generic import ListView

from .forms import BlogForm
from .models import Blog


@login_required(login_url='/login_to/')
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


def out(request):
    logout(request)
    return HttpResponseRedirect('/login_to/')


def login_to(request):
    return render(request, 'login.html')


def show(request):
    if request.method == 'POST':
        form = BlogForm(request.POST)
        if form.is_valid():
            _ = form.save()
            _.save()
            return HttpResponseRedirect('/index/')
        return HttpResponse("not good to new")
    else:
        form = BlogForm()
    return render(request, 'base/show.html', {'form': form})


def user_login(request):
    print request.COOKIES
    username = request.POST.get('inputUsername')
    password = request.POST.get('inputPassword')
    user = authenticate(username=username, password=password)
    if user is not None:
        if user.is_active:
            login(request, user)
            print request.COOKIES
            return HttpResponseRedirect('/index/')
        else:
            return HttpResponseRedirect('/login_to/')
    else:
        return HttpResponseRedirect('/login_to/')


@login_required(login_url='/login_to/')
def new_blog(request):
    if request.method == 'POST':
        form = BlogForm(request.POST)
        if form.is_valid():
            _ = form.save()
            _.save()
            return HttpResponseRedirect('/index/')
        return HttpResponse("not good to new")
    else:
        form = BlogForm()
    return render(request, 'new_blog.html', {'form': form})


class BlogListView(ListView):
    template_name = 'blog_list.html'
    model = Blog
    paginate_by = 10


class BlogDetailView(DetailView):
    template_name = 'blog_detail.html'
    model = Blog

