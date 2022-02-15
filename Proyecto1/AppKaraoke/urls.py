from django.urls import path
from . import views

urlpatterns = [

    path('', views.inicio, name="inicio"),
    path('karaoke', views.karaoke, name="Karaoke"),
    # PATH KARAOKE
    path('listaKaraoke', views.KaraokeList.as_view(), name='List'),
    path('detalleKaraoke/<pk>/', views.KaraokeDetail.as_view(), name='Detail'),
    path('crearKaraoke', views.KaraokeCreate.as_view(), name='New'),
    path('actualizaKaraoke/<pk>/', views.KaraokeUpdate.as_view(), name='Edit'),
    path('eliminaKaraoke/<pk>/', views.KaraokeDelete.as_view(), name='Delete'),
    # busqueda cancion
    path('busquedaCancion/', views.busquedaCancion, name="BusquedaCancion"),
    path('buscar/', views.buscar),

    # PATH PARTICIPANTES
    path('listaParticipantes', views.ParticipantesList.as_view(), name='ListP'),
    path('detalleParticipantes/<pk>/', views.ParticipantesDetail.as_view(), name='DetailP'),
    path('crearParticipantes', views.ParticipantesCreate.as_view(), name='NewP'),
    path('actualizaParticipantes/<pk>/', views.ParticipantesUpdate.as_view(), name='EditP'),
    path('eliminaParticipantes/<pk>/', views.ParticipantesDelete.as_view(), name='DeleteP'),

    # PATH GANADORES
    path('listaGanadores', views.GanadoresList.as_view(), name='ListG'),
    path('detalleGanadores/<pk>/', views.GanadoresDetail.as_view(), name='DetailG'),
    path('crearGanadores', views.GanadoresCreate.as_view(), name='NewG'),
    path('actualizaGanadores/<pk>/', views.GanadoresUpdate.as_view(), name='EditG'),
    path('eliminaGanadores/<pk>/', views.GanadoresDelete.as_view(), name='DeleteG'),
]