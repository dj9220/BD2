from django.shortcuts import render,redirect

# Create your views here.
from users.forms import RegisterForm
from django.contrib import messages

def register(request):
    if request.method=='POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request,f'Wlcome {username}, your account is created')
            return redirect('login')

    else:
        form = RegisterForm()
    return render(request, 'users/register.html', {'form':form})