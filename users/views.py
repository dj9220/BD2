from datetime import date

from django.contrib.auth.decorators import login_required
from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.views import View

from .models import Profile, Message

# Create your views here.
from users.forms import MessageForm, ProfileForm, LoginForm
from django.contrib import messages


def login_page(request):
    forms = LoginForm()
    if request.method == 'POST':
        forms = LoginForm(request.POST)
        if forms.is_valid():
            username = forms.cleaned_data['username']
            password = forms.cleaned_data['password']
            user = authenticate(username=username, password=password)
            messages.success(request, f'Sveiki atvykę')
            if user:
                login(request, user)
                return redirect('dashboard')
    context = {'form': forms}
    return render(request, 'users/login.html', context)


def logout_page(request):
    logout(request)
    return redirect('login')
@login_required
def profile_page(request):
    profile = Profile.objects.filter(user=request.user)
    return render(request,'users/Profile-page.html', {'profile':profile})

@login_required
def write_message(request):
    if request.method=='POST':
        form = MessageForm(request.POST)
        if form.is_valid():
            form = form.save(commit=False)
            form.sender = request.user
            form.save()
            messages.success(request, f'Skelbimas sėkmingai paskelbtas')
            return redirect('inbox')
    else:
        form = MessageForm()

    return render(request,'users/send-message.html', {'form':form})
@login_required
def get_inbox(request):
    msg = Message.objects.all().order_by('-created_at')
    return render(request, 'users/inbox.html', {'msg':msg})

@login_required
def all_profiles(request):
    profiles = Profile.objects.all()
    return render(request, 'users/all-profiles.html', {'profiles':profiles})


