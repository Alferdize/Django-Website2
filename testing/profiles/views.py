from django.shortcuts import render

# Create your views here.

def home(request):
    title = 'Home'
    context = {'title': title}
    template = 'home.html'
    return render(request,template,context)


def about(request):
    title = 'About'
    context = {'title': title}
    template = 'about.html'
    return render(request,template,context)

