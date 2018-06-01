from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import profile, Persona
from .forms import profile_form
from django.views.generic import CreateView, ListView, FormView
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout
from django.utils import timezone

from django.conf import settings
from io import BytesIO
from reportlab.pdfgen import canvas
from django.views.generic import View


class ReportePersonasPDF(View):

    def cabecera(self,pdf):
        #Utilizamos el archivo logo_django.png que está guardado en la carpeta media/imagenes
        archivo_imagen = settings.MEDIA_ROOT+'/imagenes/logo.png'
        #Definimos el tamaño de la imagen a cargar y las coordenadas correspondientes
        pdf.drawImage(archivo_imagen, 40, 750, 120, 90,preserveAspectRatio=True)

        #Establecemos el tamaño de letra en 16 y el tipo de letra Helvetica
        pdf.setFont("Helvetica", 14)
        #Dibujamos una cadena en la ubicación X,Y especificada
        pdf.drawString(200, 800, u"Bomberos Boluntarios San Pedro Sacatepequez San Marcos")
        pdf.setFont("Helvetica", 14)
        pdf.drawString(200, 770, u"REPORTE DE ALERTAS")


    def get(self, request, *args, **kwargs):
        #Indicamos el tipo de contenido a devolver, en este caso un pdf
        response = HttpResponse(content_type='application/pdf')
        #La clase io.BytesIO permite tratar un array de bytes como un fichero binario, se utiliza como almacenamiento temporal
        buffer = BytesIO()
        #Canvas nos permite hacer el reporte con coordenadas X y Y
        pdf = canvas.Canvas(buffer)
        #Llamo al método cabecera donde están definidos los datos que aparecen en la cabecera del reporte.
        self.cabecera(pdf)
        y = 600
        self.tabla(pdf, y)
        #Con show page hacemos un corte de página para pasar a la siguiente
        pdf.showPage()
        pdf.save()
        pdf = buffer.getvalue()
        buffer.close()
        response.write(pdf)
        return response


    def tabla(self,pdf,y):
        #Creamos una tupla de encabezados para neustra tabla
        encabezados = ('Nombre', 'Telefono', 'Coordenadas', 'Direccion', 'Emergencia')
        '''
        #Creamos una lista de tuplas que van a contener a las personas
        detalles = [(Persona.nombre, Persona.telefono, Persona.coordenadas, Persona.direccion, Persona.emergencia) for persona in Persona.objects.all()]
        #Establecemos el tamaño de cada una de las columnas de la tabla
        detalle_orden = Table([encabezados] + detalles, colWidths=[2 * cm, 5 * cm, 5 * cm, 5 * cm])
        #Aplicamos estilos a las celdas de la tabla
        detalle_orden.setStyle(TableStyle(
        [
                #La primera fila(encabezados) va a estar centrada
                ('ALIGN',(0,0),(3,0),'CENTER'),
                #Los bordes de todas las celdas serán de color negro y con un grosor de 1
                ('GRID', (0, 0), (-1, -1), 1, colors.black),
                #El tamaño de las letras de cada una de las celdas será de 10
                ('FONTSIZE', (0, 0), (-1, -1), 10),
                ]
        ))
        '''
        space = 25
        for n in range(5):
            pdf.setFont("Helvetica", 14)
            pdf.drawString(space, y + 35, encabezados[n])
            space += 100

        x = 25
        for persona in Persona.objects.all():
            pdf.setFont("Helvetica", 14)
            pdf.drawString(x, y, persona.nombre)
            pdf.drawString(x + 75, y, persona.telefono)
            pdf.drawString(x + 150, y, persona.coordenadas)
            pdf.drawString(x + 300, y, persona.direccion)
            pdf.drawString(x + 450, y, persona.emergencia)
            y -= 40

            '''
        #Establecemos el tamaño de la hoja que ocupará la tabla
        detalle_orden.wrapOn(pdf, 800, 600)
        #Definimos la coordenada donde se dibujará la tabla
        detalle_orden.drawOn(pdf, 60,y)}
        '''


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
    data = Persona.objects.filter(date__range=[timezone.now(), timezone.now()])

    return render(request, 'alerts.html', {'data':data})




def bomberos_list(request):
    profile_list = profile.objects.all()
    return render(request, 'bomberos_list.html', {'profile_list': profile_list})

def logout_user(request):
    logout(request)
    return redirect('main')

class es_atendido(View):
    def get(self, request, *args, **kwargs):
        todo = Persona.objects.get(id=kwargs['id'])
        todo.Atendido = True
        todo.save()
        return redirect('alert')

def alerts_list_first_aid(request):
    data = Persona.objects.filter(emergencia = 'Primeros Auxilios')
    return render(request, 'alerts_by_first_aid.html', {'data':data})

def alerts_list_fire(request):
    data = Persona.objects.filter(emergencia = 'Incendio')
    return render(request, 'alerts_by_fire.html', {'data':data})

def alerts_list_maternity(request):
    data = Persona.objects.filter(emergencia = 'Maternidad')
    return render(request, 'alerts_by_maternity.html', {'data':data})

def alerts_list_transit(request):
    data = Persona.objects.filter(emergencia = 'Transito')
    return render(request, 'alerts_by_transit.html', {'data':data})