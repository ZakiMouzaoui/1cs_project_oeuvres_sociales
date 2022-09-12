from django.core import validators
from django.core.validators import FileExtensionValidator
from django.contrib.auth.models import User
from django.db import models


# Parties (numpart, titre, nbchap(nombre de chapitres dans la partie))
class Partie(models.Model):
    titre = models.CharField(max_length=200)
    nbchap = models.IntegerField(null=True, blank=True, default=0)
    budget = models.IntegerField(null=True, default=0,
                                 validators=[validators.int_list_validator(sep=', ', message=None, code='invalid',
                                                                           allow_negative=False)])

    budget_restant = models.PositiveIntegerField(null=True)
    solde = models.IntegerField(null=True, blank=True,
                                validators=[validators.int_list_validator(sep=', ', message=None, code='invalid',
                                                                          allow_negative=False)])
    debit = models.IntegerField(null=True, blank=True, default=0,
                                validators=[validators.int_list_validator(sep=', ', message=None, code='invalid',
                                                                          allow_negative=False)])
    credit = models.IntegerField(null=True, blank=True, default=0,
                                 validators=[validators.int_list_validator(sep=', ', message=None, code='invalid',

                                                                           allow_negative=False)])

    class Meta:
        ordering = ['titre']

    def __str__(self):
        return str(self.titre)

# chapitres (numchap, titre, nbart(nobre d'articles), #numpart)
class Chapitre(models.Model):
    titre = models.CharField(max_length=200)
    nbart = models.IntegerField(null=True, blank=True, default=0)
    partie = models.ForeignKey(Partie, on_delete=models.CASCADE, null=True)
    budget = models.IntegerField(null=True, default=0,
                                 validators=[validators.int_list_validator(sep=', ', message=None, code='invalid',
                                                                           allow_negative=False)])

    budget_restant = models.PositiveIntegerField(null=True)
    solde = models.IntegerField(null=True, blank=True,
                                validators=[validators.int_list_validator(sep=', ', message=None, code='invalid',
                                                                          allow_negative=False)])
    debit = models.IntegerField(null=True, blank=True, default=0,
                                validators=[validators.int_list_validator(sep=', ', message=None, code='invalid',
                                                                          allow_negative=False)])
    credit = models.IntegerField(null=True, blank=True, default=0,
                                 validators=[validators.int_list_validator(sep=', ', message=None, code='invalid',
                                                                           allow_negative=False)])

    def __str__(self):
        return str(self.titre)


# Articles(numart, contenu(tableau/text numchap)
class Article(models.Model):
    numero_article = models.IntegerField(null=True)
    contenu = models.TextField()
    chapitre = models.ForeignKey(Chapitre, on_delete=models.CASCADE)
    budget = models.IntegerField(null=True,
                                 validators=[validators.int_list_validator(sep=', ', message=None, code='invalid',
                                                                           allow_negative=False)])
    montant = models.IntegerField(null=True,
                                  validators=[validators.int_list_validator(sep=', ', message=None, code='invalid',
                                                                            allow_negative=False)])
    solde = models.IntegerField(null=True, blank=True,
                                validators=[validators.int_list_validator(sep=', ', message=None, code='invalid',
                                                                          allow_negative=False)])
    debit = models.IntegerField(null=True, blank=True, default=0,
                                validators=[validators.int_list_validator(sep=', ', message=None, code='invalid',
                                                                          allow_negative=False)])
    credit = models.IntegerField(null=True, blank=True, default=0,
                                 validators=[validators.int_list_validator(sep=', ', message=None, code='invalid',
                                                                           allow_negative=False)])


    def __str__(self):
        return "المادة "+str(self.numero_article)

# Demande(montant, date, user, commentaire, article, etat)
class Demande(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    montant = models.IntegerField(null=True,
                                  validators=[validators.int_list_validator(sep=', ', message=None, code='invalid', allow_negative=False)])
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)
    commentaire = models.TextField(null=True, blank=True, max_length=60)
    ETAT_CHOICES = [
        ('non traitée', 'non traitée'),
        ('refusée', 'refusée'),
        ('acceptée', 'acceptée')
    ]

    etat = models.CharField(
        max_length=12,
        choices=ETAT_CHOICES,
        default="non traitée",
    )

    date_paiement = models.DateTimeField(null=True)

    MODE_CHOICES = [
        ('Virement', 'Virement'),
        ('Espèces', 'Espèces'),
        ('Chèque', 'Chèque')
    ]

    mode_paiement = models.CharField(
        max_length=8,
        choices=MODE_CHOICES,
        null=True
    )

    def __str__(self):
        return str(self.pk)


# Paiement: demande, date_paiement, mode_paiement:virement,especes,cheque
class Paiement(models.Model):
    demande = models.ForeignKey(Demande, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)
    MODE_CHOICES = [
        ('Virement', 'Virement'),
        ('Espèces', 'Espèces'),
        ('Chèque', 'Chèque')
    ]

    mode_paiement = models.CharField(
        max_length=8,
        choices=MODE_CHOICES,
    )

    def __str__(self):
        return str(self.pk)


# Pret(montant, date_deb, idcompteuser, justificatif, etat)
class Pret(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    montant = models.IntegerField(
        validators=[validators.int_list_validator(sep=', ', message=None, code='invalid', allow_negative=False)])
    date = models.DateField(auto_now_add=True)
    commentaire = models.TextField(null=True, blank=True)
    ETAT_CHOICES = [
        ('non traitée', 'non traitée'),
        ('refusée', 'refusée'),
        ('acceptée', 'acceptée')
    ]

    etat = models.CharField(
        max_length=12,
        choices=ETAT_CHOICES,
        default="non traitée",
    )

    MODE_CHOICES = [
        ('Virement', 'Virement'),
        ('Espèces', 'Espèces'),
        ('Chèque', 'Chèque')
    ]

    mode_paiement = models.CharField(
        max_length=8,
        choices=MODE_CHOICES,
        null=True
    )

    date_paiement = models.DateTimeField(null=True)

    def __str__(self):
        return str(self.pk)


class Fichier(models.Model):
    document = models.FileField(upload_to="files", null=True)
    demande = models.ForeignKey(Demande, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.document.url)

class Fichier_Pret(models.Model):
    document = models.FileField(upload_to="files", null=True)
    pret = models.ForeignKey(Pret, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.document.url)


# remboursement de pret(nb mois,montant, date debut)
class Remboursement(models.Model):
    nombre_mois = models.IntegerField(null=True)
    montant = models.IntegerField(null=True,
                                  validators=[validators.int_list_validator(sep=', ', message=None, code='invalid',
                                                                            allow_negative=False)])
    date_debut = models.DateField(auto_now_add=True)
    pret = models.ForeignKey(Pret, on_delete=models.CASCADE, null=True)


class Reponse_demande(models.Model):
    motif = models.CharField(max_length=1000)
    demande = models.OneToOneField(Demande, on_delete=models.CASCADE, null=True)


# Employee (idemp, nom,  prénom,date-naiss, adresse, sex, poste, ccp, num-sc email,  numtél, date-début, date-sortie,
# #idcompte....)
class Employee(models.Model):
    nom = models.CharField(max_length=100)
    prenom = models.CharField(max_length=100)
    date_naissance = models.DateField(null=True)
    adresse = models.CharField(max_length=400)
    poste = models.CharField(max_length=100)
    ccp = models.IntegerField(verbose_name="num compte postal")
    nss = models.IntegerField(verbose_name="num sécurité sociale")
    email = models.EmailField()
    num_tel = models.IntegerField(verbose_name="num tel")
    photo = models.ImageField(null=True, upload_to="images/")

    SEX_CHOICES = [
        ('Homme', 'Homme'),
        ('Femme', 'Femme')
    ]

    sex = models.CharField(
        max_length=5,
        choices=SEX_CHOICES
    )

    class Meta:
        ordering = ["nom", "prenom"]

    def __str__(self):
        return str(self.nom) + " " + str(self.prenom)


class Annonce(models.Model):
    titre = models.CharField(max_length=200, null=True)
    detail = models.ImageField(null=True, upload_to="")
    date_debut = models.DateTimeField()
    date_fin = models.DateTimeField()
    photo = models.ImageField(null=True, upload_to="")
    users = models.ManyToManyField(User)
    admis = models.ManyToManyField(User, related_name="admis")
    budget = models.IntegerField(null=True)

    class Meta:
        ordering = ["date_debut"]

    def __str__(self):
        return str(self.titre)


class Inscription(models.Model):
    annonce = models.ForeignKey(Annonce, on_delete=models.CASCADE)
    date_inscription = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    montant = models.IntegerField(null=True)


# Caisse(débit, crédit, bilan(pdf))
class Caisse(models.Model):
    montant_initial = models.IntegerField(null=True,
                                          validators=[
                                              validators.int_list_validator(sep=', ', message=None, code='invalid',
                                                                            allow_negative=False)])
    debit = models.IntegerField(null=True,
                                validators=[validators.int_list_validator(sep=', ', message=None, code='invalid',
                                                                          allow_negative=False)])
    credit = models.IntegerField(null=True,
                                 validators=[validators.int_list_validator(sep=', ', message=None, code='invalid',
                                                                           allow_negative=False)])
    date_debut = models.DateField(auto_now=True)
    bilan_pdf = models.FileField(null=True,
                                 upload_to='user_directory_path',
                                 validators=[FileExtensionValidator(['pdf'])])


class Recette(models.Model):
    subvention = models.CharField(max_length=500)
    montant = models.IntegerField(validators=[validators.int_list_validator(sep=', ', message=None, code='invalid',
                                                                            allow_negative=False)])
    date= models.DateTimeField(null=True)

    def __str__(self):
        return str(self.subvention)


class Budget(models.Model):
    date = models.DateTimeField(auto_now_add=True)
    montant = models.IntegerField(
        validators=[validators.int_list_validator(sep=', ', message=None, code='invalid', allow_negative=False)])
    solde = models.IntegerField(
        validators=[validators.int_list_validator(sep=', ', message=None, code='invalid', allow_negative=False)])
    credit = models.IntegerField(
        validators=[validators.int_list_validator(sep=', ', message=None, code='invalid', allow_negative=False)])
    debit = models.IntegerField(
        validators=[validators.int_list_validator(sep=', ', message=None, code='invalid', allow_negative=False)])

    def __str__(self):
        return str(self.pk)


"""
# Dossier(numdoss,  documents(pdf),#numdemande)
class Dossier(models.Model):
    numdoss = models.AutoField(primary_key=True)
    doc_pdf = models.FileField(null=True,
                               upload_to='user_directory_path',
                               validators=[FileExtensionValidator(['pdf'])])
    demande = models.ForeignKey(Demande, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.numdoss)
"""

"""
# Pvs(numpv, objet, date, huere-déb, huere-fin, pv(pdf))
class Pv(models.Model):
    numpv = models.IntegerField(primary_key=True)
    objet = models.CharField(max_length=200)
    date = models.DateField(auto_now=True)
    huere_deb = models.TimeField()
    huere_fin = models.TimeField()
    pv_pdf = models.FileField(null=True,
                              upload_to='user_directory_path',
                              validators=[FileExtensionValidator(['pdf'])])

    def __str__(self):
        return str(self.objet)
        
"""

class Pv(models.Model):
    date = models.DateField(auto_now=True)
    titre = models.CharField(max_length=20, null=True)
    pv = models.FileField(null=True, upload_to="",
                          validators=[FileExtensionValidator(['pdf'])])

    def __str__(self):
        return str(self.titre)

# documents-finaciére(numdoc, type(fiche de paie....), document(pdf))
class Doc_finace(models.Model):
    numdoc = models.IntegerField(primary_key=True)
    doc_pdf = models.FileField(null=True,
                               upload_to='user_directory_path',
                               validators=[FileExtensionValidator(['pdf'])])

    TYPE_CHOICES = [
        ('fiche de paie', 'fiche de paie'),
        ('attestation de solde', 'attestation de solde'),
        ('relevé de compte', 'relevé de compte'),
        ('reçu de cheque', 'reçu de cheque')
    ]

    type = models.CharField(
        max_length=20,
        choices=TYPE_CHOICES
    )


# Question( idquestion #idcompte, date, contenu)
class Question(models.Model):
    idquestion = models.IntegerField(primary_key=True)
    date = models.DateTimeField(auto_now=True)
    contenu = models.TextField()
    idcompteuser = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.contenu)


# Réponse( idreponse  #idcompteadmin, #idcompteuser date, contenu, #idquestion)
class Reponse(models.Model):
    date = models.DateTimeField(auto_now=True)
    contenu = models.TextField()
    idcompteuser = models.ForeignKey(User, on_delete=models.CASCADE)
    idquestion = models.ForeignKey(Question, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.contenu)


# Factures( idfac, #idcompteuser, #idcompteadmin date, mode-paiement, #numdemande)
class Facture(models.Model):
    idfac = models.IntegerField(primary_key=True)
    date = models.DateTimeField(auto_now=True)
    idcompteuser = models.ForeignKey(User, on_delete=models.CASCADE)
    numdemande = models.ForeignKey(Demande, on_delete=models.CASCADE)
    fac_pdf = models.FileField(null=True,
                               upload_to='user_directory_path',
                               validators=[FileExtensionValidator(['pdf'])])
    MODE_PAIEMENT_CHOICES = [
        ('cach', 'cach'),
        ('versement bancaire', 'versement bancaire'),
    ]

    mode_paiement = models.CharField(
        max_length=20,
        choices=MODE_PAIEMENT_CHOICES,
    )


"""
# historique(#idemployé ,#numdemande ,dons,  congés)
class Historique(models.Model):
    idemploye = models.ForeignKey('Employee', on_delete=models.CASCADE)
    numdemande = models.ForeignKey(Demande, on_delete=models.CASCADE)
    conges = models.TextField()
    dons = models.TextField()
"""


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    employe = models.OneToOneField(Employee, on_delete=models.CASCADE, null=True)
    profile_picture = models.ImageField(upload_to="images/", blank=True, null=True, default="images/default_image.jpg")

    def __str__(self):
        return str(self.employe)


class Person(models.Model):
    nom = models.CharField(max_length=20)
    prenom = models.CharField(max_length=20)
    age = models.IntegerField()

    def __str__(self):
        return "{} {} {}".format(self.nom, self.prenom, self.age)


class Message(models.Model):
    sender = models.ForeignKey(User, on_delete=models.CASCADE, related_name='sender')
    receiver = models.ForeignKey(User, on_delete=models.CASCADE, related_name='receiver')
    message = models.CharField(max_length=1200, null=False, blank=False)
    timestamp = models.DateTimeField(auto_now_add=True)
    is_read = models.BooleanField(default=False)

    def __str__(self):
        return str(self.message)

    class Meta:
        ordering = ['-timestamp']