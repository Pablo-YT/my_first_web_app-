from django.urls import path
from random import randint
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render


def home_page(request):
	context = {'name': 'Betty Maker'}
	return render(request, 'index.html', context)

def portfolio_page(request):
	image_urls = []
	for i in range(5):
		random_number = randint(0,100),
		image_urls.append("https://picsum.photos/400/600/?image={}".format(random_number))
		context = {'gallery_images': image_urls}
	return render(request, 'gallery.html', context)

def about_me(request):
	context = {'name', 'Betty Parker'}
	return render(request, 'about.html')

def favourites(request):
		fave_link = {}
		return render(request, 'fav.html',)

def root(request):
	return HttpResponseRedirect('home')

def gallery_redirect(request):
	return HttpResponseRedirect('/portfolio/')