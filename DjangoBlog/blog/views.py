from django.shortcuts import render,get_object_or_404
#from django.http import HttpResponse
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Post
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.models import User
# Create your views here.
# posts = [
# 	{
# 		'author': 'Satyajit Kamble',
# 		'title': 'Using Django for Developing a Blog',
# 		'content': ' Used Python, Bootstrap and Django to create a blog. It is fab!',
# 		'date_posted': 'January 31, 2019'
# 	},

# 	{
# 		'author': 'Amey Meher',
# 		'title': 'Climbing the Himalayas',
# 		'content': 'The Kedarkantha trek was an experience of a lifetime',
# 		'date_posted': 'February 1, 2019'
# 	},

# 	{
# 		'author': 'Raj Nandu',
# 		'title': 'Being Single Forever',
# 		'content': 'My life is sad',
# 		'date_posted': 'February 2, 2019'
# 	},

# 	{
# 		'author': 'Saurabh Makwana',
# 		'title': 'Fly Abroad To Find Your Soulmate',
# 		'content': 'Not in India? No worrys!',
# 		'date_posted': 'February 3, 2019'
# 	},

# 	{
# 		'author': 'Aditya Ladage',
# 		'title': 'Why To Choose a Mac over Windows?',
# 		'content': 'I really dont have anything to say',
# 		'date_posted': 'February 4, 2019'
# 	}


# ]


def home(request):
	context = {
	'posts' : Post.objects.all() #posts
	}
	return render(request, 'blog/home.html', context)#HttpResponse("<h1> Blog Home </h1>")

class PostListView(ListView):
	model = Post
	template_name = 'blog/home.html'#<app>/<model>_<template>.html
	context_object_name = 'posts'#setting the name same as def home wala view
	ordering = ['-date_posted']#minus sign for newest to oldest
	paginate_by=4

class UserPostListView(ListView):
	model = Post
	template_name = 'blog/user_posts.html'#<app>/<model>_<template>.html
	context_object_name = 'posts'#setting the name same as def home wala view
	paginate_by=4

	def get_queryset(self):
		user = get_object_or_404(User, username=self.kwargs.get('username'))
		return Post.objects.filter(author=user).order_by('-date_posted')


class PostDetailView(DetailView):
	model = Post

class PostCreateView(LoginRequiredMixin, CreateView):
	model = Post
	fields = ['title', 'content']

	def form_valid(self, form):
		form.instance.author = self.request.user
		return super().form_valid(form)

class PostUpdateView(UserPassesTestMixin, LoginRequiredMixin,UpdateView):
	model = Post
	fields = ['title', 'content']

	def form_valid(self, form):
		form.instance.author = self.request.user
		return super().form_valid(form)

	def test_func(self):#prevents users from updating other user posts
		post = self.get_object()
		if self.request.user == post.author:
			return True
		return False


class PostDeleteView(UserPassesTestMixin, LoginRequiredMixin, DeleteView):
	model = Post
	success_url = "/"
	def test_func(self):#prevents users from updating other user posts
		post = self.get_object()
		if self.request.user == post.author:
			return True
		return False


def about(request):
	return render(request, 'blog/about.html', {'title':'About'})#HttpResponse("<h1> Blog About </h1>")
