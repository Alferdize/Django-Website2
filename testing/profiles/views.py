from django.shortcuts import render


from django.contrib.auth.decorators import login_required
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

@login_required
def userProfile(request):
    user = request.user
    context = {'user': user}
    template = 'profile.html'
    return render(request,template,context)
