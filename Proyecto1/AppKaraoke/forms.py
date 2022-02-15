from django import forms


class KaraokeFormulario(forms.Form):
    nombreCancion   = forms.CharField()
    artista         = forms.CharField()


class ParticipantesFormulario(forms.Form):   
    nombre          = forms.CharField(max_length=30)
    edad            = forms.IntegerField()
    anioInscripcion = forms.IntegerField()
    email           = forms.EmailField()