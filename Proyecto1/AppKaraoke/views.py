from ast import Return
from django.http import HttpResponse
from django.shortcuts               import render
from django.views.generic           import ListView
from django.views.generic.detail    import DetailView
from django.views.generic.edit      import UpdateView, DeleteView, CreateView
from .models                        import Karaoke, Participantes, Ganadores
from .forms                         import KaraokeFormulario

def inicio(request):
    return render(request, "AppKaraoke/inicio.html")
######################################################
# KARAOKE
######################################################
class KaraokeList(ListView):
      model         = Karaoke
      template_name = "AppKaraoke/karaoke_list.html"

class KaraokeDetail(DetailView):
      model         = Karaoke
      template_name = "AppKaraoke/Karaoke_detail.html"

class KaraokeUpdate(UpdateView):
      model         = Karaoke
      success_url   = '/AppKaraoke/listaKaraoke'
      fields        = ['nombreCancion', 'artista']

class KaraokeDelete(DeleteView):
      model         = Karaoke
      success_url   = '/AppKaraoke/listaKaraoke'
      template_name = 'AppKaraoke/Karaoke_confirm_delete.html'

class KaraokeCreate(CreateView):
      model         = Karaoke
      fields        = ['nombreCancion', 'artista']
      success_url   = '/AppKaraoke/listaKaraoke'

# BUSQUEDA DE CANCION
def busquedaCancion(request):
      return render(request, "AppKaraoke/busquedaCancion.html")

def buscar(request):
      if request.GET['nombreCancion']:
            #respuesta = f"Buscando la Canción: {request.GET['nombreCancion']}"
            nombreCancion     = request.GET['nombreCancion']
            karaokes          = Karaoke.objects.filter(nombreCancion__icontains=nombreCancion)
            return render(request, 'AppKaraoke/resultadosBusqueda.html', {"karaokes": karaokes, "nombreCancion":nombreCancion })
      else:
            respuesta = "No hay datos"

      return HttpResponse(respuesta)


def karaoke(request):
      if request.method == 'POST':

            miFormulario = KaraokeFormulario(request.POST)
            if miFormulario.is_valid:
                  informacion = miFormulario.cleaned_data
                  karaoke = Karaoke(nombreCancion=informacion['nombreCancion'], artista=informacion['artista']) 
                  karaoke.save()
                  return render(request, "AppKaraoke/inicio.html")
      else: 
            miFormulario= KaraokeFormulario()

      return render(request, "AppKaraoke/karaoke.html", {"miFormulario":miFormulario})

######################################################
# PARTICIPANTES
######################################################
class ParticipantesList(ListView):
      model         = Participantes
      template_name = "AppKaraoke/participantes_list.html"

class ParticipantesDetail(DetailView):
      model         = Participantes
      template_name = "AppKaraoke/participantes_detail.html"

class ParticipantesUpdate(UpdateView):
      model         = Participantes
      success_url   = '/AppKaraoke/listaParticipantes'
      fields        = ['nombre', 'edad', 'anioInscripcion', 'email']

class ParticipantesDelete(DeleteView):
      model         = Participantes
      success_url   = '/AppKaraoke/listaParticipantes'
      template_name = 'AppKaraoke/Participantes_confirm_delete.html'

class ParticipantesCreate(CreateView):
      model         = Participantes
      fields        = ['nombre', 'edad', 'anioInscripcion', 'email']
      success_url   = '/AppKaraoke/listaParticipantes'


######################################################
# GANADORES
######################################################
class GanadoresList(ListView):
      model         = Ganadores
      template_name = "AppKaraoke/ganadores_list.html"

class GanadoresDetail(DetailView):
      model         = Ganadores
      template_name = "AppKaraoke/ganadores_detail.html"

class GanadoresUpdate(UpdateView):
      model         = Ganadores
      success_url   = '/AppKaraoke/listaGanadores'
      fields        = ['nombre', 'nombreCancion', 'anioWin']

class GanadoresDelete(DeleteView):
      model         = Ganadores
      success_url   = '/AppKaraoke/listaGanadores'
      template_name = 'AppKaraoke/ganadores_confirm_delete.html'

class GanadoresCreate(CreateView):
      model         = Ganadores
      fields        = ['nombre', 'nombreCancion', 'anioWin']
      success_url   = '/AppKaraoke/listaGanadores'