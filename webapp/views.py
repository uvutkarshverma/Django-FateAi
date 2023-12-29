from django.http import HttpResponse
from .models import AItools
from django.shortcuts import render, redirect
from django.contrib import messages



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
        if request.method == "POST":
            title = request.POST.get('title')
            description = request.POST.get('description')
            url = request.POST.get('url')
            image = request.FILES.get('image')
            AItools.objects.create(name=title, description=description, link=url, img=image)
            messages.success(request, 'Form Has Been submitted successfully.')
            return HttpResponseRedirect(reverse("views.Admin"))
        return render(request, "admin.html")
    return redirect('/accounts/google/login/')