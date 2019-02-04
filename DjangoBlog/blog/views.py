from django.shortcuts import render
#from django.http import HttpResponse
from django.views.generic import ListView, DetailView, CreateView
from .models import Post

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

class PostDetailView(DetailView):
	model = Post

class PostCreateView(CreateView):
	model = Post
	fields = ['title', 'content']


def about(request):
	return render(request, 'blog/about.html', {'title':'About'})#HttpResponse("<h1> Blog About </h1>")
