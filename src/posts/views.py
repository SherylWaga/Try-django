from django.contrib import messages
from django.shortcuts import render, get_object_or_404,redirect
from django.http import HttpResponse,HttpResponseRedirect

# Create your views here.
from .models import Post
from .forms import PostForm
def post_create(request):
	form = PostForm(request.POST or None)
	if form.is_valid():
		instance = form.save(commit=False)
		instance.save()
		messages.success(request,"created successfully")
		return HttpResponseRedirect(instance.get_obsolute_url())
	else:
		messages.error(request,"failed")
	content = {
		"form":form,
	}
	return render(request,"post_form.html",content)
def post_detail(request, id):
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
	return render(request,"post_list.html",content)
def post_update(request,id):
	instance = get_object_or_404(Post,id=id)
	form = PostForm(request.POST or None, instance=instance)
	if form.is_valid():
		instance = form.save(commit=False)
		instance.save()
		messages.success(request,"updated")
		return HttpResponseRedirect(instance.get_obsolute_url())
	content = {
		"title":instance.title,
		"content":instance,
		"form":form,
	}
	return render(request,"post_form.html",content)
def post_delete(request,id):
	instance = get_object_or_404(Post,id=id)
	instance.delete()
	messages.success(request,"deleted")
	return redirect("posts:post_list")