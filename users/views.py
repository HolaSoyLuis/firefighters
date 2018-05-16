from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import profile, Persona
from .forms import profile_form
from django.views.generic import CreateView, ListView, FormView
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout

def main_page(request):
    return render(request, 'new_index.html')

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
    return render(request, 'new_profile_list.html', {'profile_list': profile_list})

def show_notification(request):
    return render(request, 'notifications.html')

def delete_profile(request):
    if request.method == 'POST':
        form = profile_form()
        inventory = profile_form.objects.all()
        item_id = int(request.POST.get('item_id'))  
        item = profile_form.objects.get(id=item_id)       
        item.delete()
        return render_to_response('inventory.html', {'form':form, 'inventory':inventory}, RequestContext(request))
    
    
class LoginView(FormView):
    template_name = 'login.html'
    form_class = AuthenticationForm
    success_url = 'main'

    def form_valid(self, form):
        login(self.request, form.get_user())
        return super(LoginView, self).form_valid(form)

def alerts_list(request):
    data = Persona.objects.all()
    return render(request, 'alerts.html', {'data':data})

def bomberos_list(request):
    profile_list = profile.objects.all()
    return render(request, 'bomberos_list.html', {'profile_list': profile_list})

def logout_user(request):
    logout(request)
    return redirect('main')