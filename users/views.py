from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import UserRegisterform, UserUpdateForm, ProfileUpdateForm
from django.contrib.auth.decorators import login_required


# Create your views here.
def register(request):
    if request.method == "POST":
        form = UserRegisterform(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get("username")
            messages.success(request, f"Account created for {username}!")
            return redirect("user-login")
            
    else:
        form = UserRegisterform() 
    return render(request, 'users/register.html', {"form": form} )

@login_required
def profile(request):
    if request.method == "POST":
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)
        if u_form.is_valid() or p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, f"Profile is successfully updated!")
            return redirect("user-profile")
    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(request.FILES, instance=request.user.profile)       
    
    context = {
        'u_form': u_form,
        'p_form': p_form
    }
    return render(request, 'users/profile.html', context)