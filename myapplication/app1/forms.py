import datetime

from django import forms
from django.contrib.auth import authenticate
from django.contrib.auth.forms import UserCreationForm, PasswordChangeForm
from django.db.models import Q
from django.forms import ModelForm, ClearableFileInput

from .models import *


class RegistrationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'password1', 'password2']

    def clean(self):
        symbols = ['@', '{', '}', '[', ']', '(', ')', '*', '/', '+', '-', '#', '&']
        contain_symbol = False
        contain_upper = False

        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')

        if password1 != password2:
            raise forms.ValidationError("Passwords didn't match")

        if len(str(password1)) < 5:
            raise forms.ValidationError("password too short")

        for char in str(password1):
            if char in symbols:
                contain_symbol = True
                break

        if not contain_symbol:
            raise forms.ValidationError("password must contain at least one symbol")

        for char in str(password1):
            if str(char).isupper():
                contain_upper = True
                break

        if not contain_upper:
            raise forms.ValidationError("password must contain at least one upper case letter")


class LoginForm(forms.Form):
    username = forms.CharField(max_length=20, error_messages={
        "required": "Please enter your username"
    })
    password = forms.CharField(required=True, error_messages={
        "required": "Please enter your password"
    })

    """
    def clean(self):
        username = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')

        user = authenticate(username=username, password=password)

        if not user or not user.is_active:
            raise forms.ValidationError("Invalid username or password. Please try again.")

        return self.cleaned_data
        """


class PartieModelForm(ModelForm):
    titre = forms.CharField(max_length=20, error_messages={'required': 'Veuillez specifier un nom '})
    budget = forms.IntegerField(error_messages={'required': 'Veuillez specifier un budget '})

    class Meta:
        model = Partie
        fields = ['titre', 'budget']
        exclude = ['nbchap', 'debit', 'credit', 'solde']


    def clean_titre(self):
        titre = self.cleaned_data.get('titre')

        for x in str(titre):
            if x != " " and not x.isalnum():
                raise forms.ValidationError("Nom invalide")

        # check if it already exists
        if Partie.objects.filter(titre=titre).exists():
            raise forms.ValidationError("Ce nom existe déja")

        return titre

    def clean_budget(self):
        budget = self.cleaned_data.get('budget')
        budget_object = Budget.objects.first()

        if budget <= 0:
            raise forms.ValidationError("Budget invalide")

        if budget > budget_object.solde:
            raise forms.ValidationError("Budget dépasse le budget restant")

        return budget


class PartieUpdateForm(forms.ModelForm):
    titre = forms.CharField(max_length=20, error_messages={'required': 'Veuillez specifier un nom '})
    budget = forms.IntegerField(error_messages={'required': 'Veuillez specifier un budget '})

    class Meta:
        model = Partie
        fields = ['titre', 'budget']
        exclude = ['nbchap', 'debit', 'credit', 'solde']

    def clean_titre(self):
        titre = self.cleaned_data.get('titre')

        for x in str(titre):
            if x != " " and not x.isalnum():
                raise forms.ValidationError("Nom invalide")

        # check if it already exists
        if self.instance.titre != titre and Partie.objects.filter(titre=titre).exists():
            raise forms.ValidationError("Ce nom existe déja")

        return titre

    def clean_budget(self):
        budget = self.cleaned_data.get('budget')

        if budget <= 0:
            raise forms.ValidationError("Budget invalide")

        return budget

class ChapitreModelForm(ModelForm):
    titre = forms.TextInput()

    budget = forms.IntegerField(error_messages={
        'required': 'Veuillez specifier un budget'
    })

    class Meta:
        model = Chapitre
        fields = ['titre', 'partie', 'budget']
        exclude = ['nbart', 'debit', 'credit', 'solde']

    def clean_titre(self):
        titre = self.cleaned_data.get('titre')

        for x in str(titre):
            if x != " " and not x.isalnum():
                raise forms.ValidationError("Nom invalide")

        # check if it already exists
        if Chapitre.objects.filter(titre=titre).exists():
            raise forms.ValidationError("Ce nom existe déja!")

        return titre

    def clean_budget(self):
        budget = self.cleaned_data.get('budget')
        partie = self.cleaned_data.get('partie')

        if budget <= 0:
            raise forms.ValidationError("Budget invalide")

        if budget > partie.budget_restant:
            raise forms.ValidationError("Budget dépasse le budget restant de cette partie")

        return budget


class ChapitreUpdateForm(ModelForm):
    titre = forms.CharField(max_length=200, error_messages={
        'required': 'Veuillez specifier un titre'
    })

    budget = forms.IntegerField(error_messages={
        'required': 'Veuillez specifier un budget'
    })

    class Meta:
        model = Chapitre
        fields = ['titre', 'partie', 'budget']
        exclude = ['nbart', 'debit', 'credit', 'solde']

    def clean_titre(self):
        titre = self.cleaned_data.get('titre')

        for x in str(titre):
            if x != " " and not x.isalnum():
                raise forms.ValidationError("Nom invalide")

        # check if it already exists
        if self.instance.titre != titre and Chapitre.objects.filter(titre=titre).exists():
            raise forms.ValidationError("Ce nom existe déja!")

        return titre

    def clean_budget(self):
        budget = self.cleaned_data.get('budget')

        if budget <= 0:
            raise forms.ValidationError("Budget invalide")

        return budget


class ArticleModelForm(ModelForm):
    contenu = forms.TextInput()

    budget = forms.IntegerField(error_messages={
        "required": "Veuillez specifier un budget"
    })

    montant = forms.IntegerField(error_messages={
        "required": "Veuillez specifier un montant"
    })

    class Meta:
        model = Article
        fields = ['contenu', 'chapitre', 'budget', 'montant']
        exclude = ['debit', 'credit', 'solde']

    def clean_budget(self):
        budget = self.cleaned_data.get('budget')
        chapitre = self.cleaned_data.get('chapitre')

        if budget <= 0:
            raise forms.ValidationError("Budget invalide")

        if budget > chapitre.budget_restant:
            raise forms.ValidationError("Budget dépasse le budget restant de ce chapitre ")

        return budget

    def clean_montant(self):
        montant = self.cleaned_data.get('montant')

        if montant <= 0:
            raise forms.ValidationError("Montant invalide")

        return montant


class ArticleUpdateForm(ModelForm):
    class Meta:
        model = Article
        fields = '__all__'
        exclude = ['debit', 'credit', 'solde']

    def clean(self):
        budget = self.cleaned_data.get("budget")
        montant = self.cleaned_data.get("montant")

        if int(budget) < int(montant):
            raise forms.ValidationError("budget ne peut pas etre inferieur au montant")


class ChangePasswordForm(PasswordChangeForm):
    old_password = forms.PasswordInput()
    new_password1 = forms.PasswordInput()
    new_password2 = forms.PasswordInput()

    class Meta:
        model = User
        fields = ["old_password", "new_password1", "new_password2"]


    def clean_new_password(self):
        new_password = self.cleaned_data.get("new_password")
        old_password = self.cleaned_data.get("old_password")

        if new_password == old_password:
            raise forms.ValidationError("Old password is same as new_password")

        return new_password

    def clean_confirm_password(self):
        confirm_password = self.cleaned_data.get("confirm_password")
        new_password = self.cleaned_data.get("new_password")

        if confirm_password != new_password:
            raise forms.ValidationError("The two passwords didn't match")

        return confirm_password



class ResetPasswordForm(forms.Form):
    email = forms.EmailField()


class EmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = '__all__'
        exclude = ['photo']


    def clean_nom(self):
        nom = self.cleaned_data.get("nom")

        for x in str(nom):
            if x.isdigit() or (x != " " and not x.isalnum()):
                raise forms.ValidationError("Nom invalide")

        return nom

    def clean_prenom(self):
        prenom = self.cleaned_data.get("prenom")

        for x in str(prenom):
            if x.isdigit() or (x != " " and not x.isalnum()):
                raise forms.ValidationError("Prénom invalide")

        return prenom

    def clean_email(self):
        email = self.cleaned_data.get("email")
        if User.objects.filter(email=email).exists():
            print("exists")
            raise forms.ValidationError("Un utilisateur existe déjà avec cet email")


        return email

    def clean_date_naissance(self):
        date_naissance = self.cleaned_data.get("date_naissance")
        today = datetime.date.today()
        age = int((today - date_naissance).days/365.25)

        if age < 23 or age > 60:
            raise forms.ValidationError("L'age doit etre entre 23 et 60 ans")

        return date_naissance


class EmployeeEditForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = '__all__'
        exclude = ['photo']

    def clean_nom(self):
        nom = self.cleaned_data.get("nom")

        for x in str(nom):
            if x.isdigit() or (x != " " and not x.isalnum()):
                raise forms.ValidationError("Nom invalide")

        return nom

    def clean_prenom(self):
        prenom = self.cleaned_data.get("prenom")

        for x in str(prenom):
            if x.isdigit() or (x != " " and not x.isalnum()):
                raise forms.ValidationError("Prénom invalide")

        return prenom

    def clean_email(self):
        email = self.cleaned_data.get("email")

        if self.instance.email != email and User.objects.filter(email=email).exists():
            raise forms.ValidationError("Un utilisateur existe déjà avec cet email")

        return email

    def clean_date_naissance(self):
        date_naissance = self.cleaned_data.get("date_naissance")
        today = datetime.date.today()
        age = int((today - date_naissance).days / 365.25)

        if age < 23 or age > 60:
            raise forms.ValidationError("L'age doit etre entre 23 et 60 ans")

        return date_naissance


class DemandeForm(forms.ModelForm):
    class Meta:
        model = Demande
        fields = ["commentaire"]


class AccepterDemandeForm(forms.ModelForm):
    class Meta:
        model = Demande
        fields = ["date_paiement", "mode_paiement"]

    def clean_date_paiement(self):
        date = self.cleaned_data.get("date_paiement")
        today = datetime.datetime.now(datetime.timezone.utc)
        dif = int((today - date).days)

        if dif > 0:
            raise forms.ValidationError("Date de paiment invalide")

        return date


class PretForm(forms.ModelForm):
    class Meta:
        model = Pret
        fields = ["montant", "commentaire"]


class  AccepterPretForm(forms.ModelForm):
    class Meta:
        model = Pret
        fields = ["date_paiement"]


    def clean_date_paiement(self):
        date = self.cleaned_data.get("date_paiement")
        today = datetime.datetime.now(datetime.timezone.utc)
        dif = int((today - date).days)

        if dif > 0:
            raise forms.ValidationError("Date de paiment invalide")

        return date


class AnnonceForm(forms.ModelForm):
    class Meta:
        model = Annonce
        fields = ["titre", "budget", "date_debut", "date_fin"]


    def clean_titre(self):
        titre = self.cleaned_data["titre"]

        if Annonce.objects.filter(titre=titre).exists():
            raise forms.ValidationError("Une annonce existe déjà avec ce nom")

        return titre

    def clean_date_debut(self):
        date_debut = self.cleaned_data.get("date_debut")
        today = datetime.datetime.now(datetime.timezone.utc)

        dif = int((today-date_debut).days)
        if dif > 0:
            raise forms.ValidationError("Date début invalide")

        return date_debut


    def clean(self):
        date_debut = self.cleaned_data.get("date_debut")
        date_fin = self.cleaned_data.get("date_fin")

        if str(date_debut) > str(date_fin):
            raise forms.ValidationError("La date fin ne peut pas etre inférieure à la date début")


class UpdateAnnonceForm(forms.ModelForm):
    class Meta:
        model = Annonce
        fields = ["titre", "budget", "date_debut", "date_fin"]


    def clean_titre(self):
        titre = self.cleaned_data["titre"]

        if self.instance.titre != titre and Annonce.objects.filter(titre=titre).exists():
            raise forms.ValidationError("Une annonce existe déjà avec ce nom")

        return titre

    def clean_date_debut(self):
        date_debut = self.cleaned_data.get("date_debut")
        today = datetime.datetime.now(datetime.timezone.utc)

        dif = int((today-date_debut).days)
        if dif > 0:
            raise forms.ValidationError("Date début invalide")

        return date_debut


    def clean(self):
        date_debut = self.cleaned_data.get("date_debut")
        date_fin = self.cleaned_data.get("date_fin")

        if str(date_debut) > str(date_fin):
            raise forms.ValidationError("La date fin ne peut pas etre inférieure à la date début")



class PvModelForm(forms.ModelForm):
    class Meta:
        model = Pv
        fields = ["pv", "titre"]

    def clean_titre(self):
        titre = self.cleaned_data["titre"]

        if Pv.objects.filter(titre=titre).exists():
            raise forms.ValidationError("Ce titre existe déjà")

        return titre


class PvUpdateModelForm(forms.ModelForm):
    class Meta:
        model = Pv
        fields = ["pv", "titre"]

    def clean_titre(self):
        titre = self.cleaned_data["titre"]

        if self.instance.titre != titre and Pv.objects.filter(titre=titre).exists():
            raise forms.ValidationError("Ce titre existe déjà")

        return titre


class UpdateImageForm(forms.Form):
    image_file = forms.FileField()
