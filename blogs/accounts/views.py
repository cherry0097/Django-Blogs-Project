from django.shortcuts import render, redirect
# from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout

# Create your views here.

def signup_views(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('accounts:login')
        
    else:
        form = UserCreationForm()
    return render(request,'accounts/signup.html',{'form': form})

def login_views(request):
    if request.method == 'POST':
        form = AuthenticationForm(data = request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request,user)
            if 'next' in request.POST:
                return redirect(request.POST.get('next'))
            else:
                return redirect('articles:article-list')
    else:
        form = AuthenticationForm()
    return render(request, 'accounts/login.html',{'form': form})

def logout_views(request):
    if request.method == 'POST':
        logout(request)
        return redirect('articles:article-list')



    