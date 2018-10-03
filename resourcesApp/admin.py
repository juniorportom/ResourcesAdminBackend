# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

# Register your models here.
from resourcesApp.models import Tipo_Recurso, Estado, Rol, Responsable, Recurso, Recurso_Responsable, \
    Recurso_Intermedio, Lista_Chequeo, Resultado_ListaChequeo

admin.site.register(Tipo_Recurso);
admin.site.register(Estado);
admin.site.register(Rol);
admin.site.register(Responsable);
admin.site.register(Recurso);
admin.site.register(Recurso_Responsable);
admin.site.register(Recurso_Intermedio);
admin.site.register(Lista_Chequeo);
admin.site.register(Resultado_ListaChequeo);