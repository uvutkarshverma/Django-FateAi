from django.http import HttpResponse
from .models import AItools
from django.shortcuts import render,get_object_or_404,redirect
from django.contrib import messages
import json
from django.http import JsonResponse
from django.core import serializers
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.core.files.storage import default_storage
from django.db.models import Q
# Create your views here.
def index(request):
    tools = AItools.objects.all()[::-1]
    return render(request, "index.html", {'data': tools})
def About(request):
    return render(request, "about.html")
def Contact(request):
    return render(request, "contact.html")
def Admin(request):
    if request.user.is_authenticated:
        if (request.method == "POST") & ('submit-delete' in request.POST):
            id = request.POST.get('id')
            tools = AItools.objects.get(id=id)
            if str(request.user) == str(tools.user):
                obj = get_object_or_404(AItools, pk=id)
                obj.delete()
                messages.success(request, 'Your Listing has been deleted Succesfully')
        tools = AItools.objects.filter(user=request.user)[::-1]
        return render(request, "admin.html", {'data': tools})
    return redirect('/accounts/google/login/')

def Addlisting(request):
    if request.user.is_authenticated:
        if request.method == "POST":
            current_user = request.user
            title = request.POST.get('title')
            description = request.POST.get('description')
            url = request.POST.get('url')
            image = request.FILES.get('image')
            AItools.objects.create(user=current_user, name=title, description=description, link=url, img=image)
            messages.success(request, 'Form Has Been submitted successfully.')
            return redirect(reverse('Admin')) 
        return render(request, "addlisting.html")
    return redirect('/accounts/google/login/')

def Updatelisting(request, id):
    if request.user.is_authenticated:
        tools = AItools.objects.get(id=id)
        if str(request.user) == str(tools.user):
            if request.method == "POST":
                if 'submit-data' in request.POST:
                    obj = get_object_or_404(AItools, pk=id)
                    obj.name = request.POST.get('title')
                    obj.description = request.POST.get('description')
                    obj.link = request.POST.get('url')
                    obj.save()
                    messages.success(request, 'Details Has Been Updated successfully.')
                    tools = AItools.objects.get(id=id)
                    return render(request, "updatelisting.html", {'data': tools})
                elif 'submit-img' in request.POST:
                    obj = get_object_or_404(AItools, pk=id)
                    new_image = request.FILES['image']
                    obj.img.save(new_image.name, new_image, save=True)
                    messages.success(request, 'Image Has Been Updated successfully.')
                    old_image_path = tools.img.path
                    default_storage.delete(old_image_path)
                    tools = AItools.objects.get(id=id)
                    return render(request, "updatelisting.html", {'data': tools})
            return render(request, "updatelisting.html", {'data': tools})
        else:
            messages.warning(request, 'Dekho ye Galat baat hai, Dusro ki cheeze nahi chute.')
            return redirect(reverse('Admin')) 
    return redirect('/accounts/google/login/')
    
def Search(request):
    if request.method == "POST":
        input=request.POST.get('input')
        tools = AItools.objects.filter(Q(name__icontains=input) | Q(description__icontains=input))[::-1]
        return render(request, "searchresult.html", {'data': tools, 'name':input})
    return HttpResponse("Please input some data")

def Disclaimer(request):
    return render(request, "disclaimer.html")
def PrivacyPolicy(request):
    return render(request, "privacypolicy.html")

        
        
        