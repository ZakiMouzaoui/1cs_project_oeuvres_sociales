from django.contrib import admin

# Register your models here.

from django.contrib import admin
from .models import *

admin.site.register(Partie)
admin.site.register(Chapitre)
admin.site.register(Caisse)
admin.site.register(Doc_finace)
admin.site.register(Facture)
admin.site.register(Annonce)
admin.site.register(Article)
admin.site.register(Demande)
admin.site.register(Question)
admin.site.register(Reponse)
admin.site.register(Employee)
admin.site.register(Budget)
admin.site.register(Recette)
admin.site.register(Reponse_demande)
admin.site.register(UserProfile)
admin.site.register(Person)
admin.site.register(Remboursement)
admin.site.register(Fichier)
admin.site.register(Paiement)
admin.site.register(Pv)
admin.site.register(Pret)
admin.site.register(Fichier_Pret)
admin.site.register(Message)
admin.site.register(Inscription)
