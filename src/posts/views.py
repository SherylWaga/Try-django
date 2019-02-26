from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
# Create your views here.
from .models import Post
def post_create(request):
	return HttpResponse("<h1>HELLO<h1>")
def post_detail(request, id=None):
	instance = get_object_or_404(Post,id=id)
	content = {
	    "title": instance.title,
	    "instance":instance,
	}
	return render(request,'detail.html',content)
def post_list(request):
	queryset = Post.objects.all()
	content = {
	     "object_list":queryset,
	     "title":"list"
	}
	return render(request,"index.html",content)
def post_update(request):
	return HttpResponse("<h1>update<h1>")
def post_delete(request):
	return HttpResponse("<h1>delete<h1>")