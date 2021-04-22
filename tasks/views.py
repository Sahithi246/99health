from django.shortcuts import render,redirect
from django.http import JsonResponse
from django.core import serializers
from django.http import HttpResponse
from .models import Post
from .forms import createform


#def posts(request):
    #posts = Post.objects.filter(completed=False)
    #post_list = serializers.serialize('json', posts)
    #return HttpResponse(post_list, content_type="text/json-comment-filtered")

def create(request):
	form=createform()

	if request.method == "POST":
		form=createform(request.POST)
		#id = Post.objects.only('id').get({{form.title}}).id
		
		if form.is_valid():
			form1=form.save()
			#place = Post.objects.get(name='kansas')
			#tasks=Post.objects.only('id').get(title='country').id
			#print(tasks) 
			showall=Post.objects.all()
			#return HttpResponse(tasks)
			#return redirect('create')

			return JsonResponse(form1.id,safe=False,status=201)
			#return render(request,'create.html',{"data":showall})

	context={'form':form}
	return render(request,'home.html',context)
def all(request):
	#showall=Post.objects.all()
	data= list(Post.objects.values())
	return JsonResponse(data,safe=False,status=200)
	#return render(request,'all.html',{"data":showall},status=200)
    #posts = Post.objects.all()
    #post_list = serializers.serialize('json', posts)
    #return HttpResponse(post_list, content_type="text/json-comment-filtered")
	
def update(request,id):
	update=Post.objects.get(id=id)
	form=createform(request.POST,instance=update)
	if form.is_valid():
		form.save()
		return HttpResponse(status=204)
	context={'form':form}
	return render(request,'home.html',context)

def deleteid(request,id):
	deleteid=Post.objects.get(id=id)
	deleteid.delete()
	return HttpResponse(status=400)

def show(request,id):
	show=Post.objects.get(id=id)
	return HttpResponse(show)
	#return JsonResponse(show,safe=False,status=201)
