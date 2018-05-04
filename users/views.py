from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import profile
from .forms import profile_form
from django.views.generic import CreateView

def main_page(request):
    return render(request, 'index.html')

class c_profile(CreateView):
    model = profile
    form_class = profile_form
    template_name = 'create_profile.html'
    success_url = 'main'

def create_profile(request):
    if request.method == 'POST':
        formulario = profile_form(request.POST, request.FILES)
        if formulario.is_valid():
            formulario.save()
            return redirect('main')
    else:
        formulario = profile_form()
    return render(request, 'create_profile.html', {'formulario': formulario})

def new_profile(request):
    if request.method=='POST':
        formulario = profile_form(request.POST, request.FILES)
        if formulario.is_valid():
            formulario.save()
            return redirect('main')
    else:
        formulario = profile_form()
    context = {'formulario': formulario}
    return render(request, 'create_profile.html', context)