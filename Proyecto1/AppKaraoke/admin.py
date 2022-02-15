from django.contrib import admin
from  .models import * #importamos el archivo models

# Register your models here.

admin.site.register(Karaoke)
admin.site.register(Participantes)
admin.site.register(Ganadores)


