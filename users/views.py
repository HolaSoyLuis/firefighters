from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import profile
from .forms import profile_form
from django.views.generic import CreateView, ListView

def main_page(request):
    return render(request, 'index.html')

def create_profile(request):
    if request.method == 'POST':
        formulario = profile_form(request.POST, request.FILES)
        if formulario.is_valid():
            formulario.save()
            return redirect('profile_list')
    else:
        formulario = profile_form()
    return render(request, 'create_profile.html', {'formulario': formulario})

def profile_list(request):
    profile_list = profile.objects.all()
    return render(request, 'profile_list.html', {'profile_list': profile_list})