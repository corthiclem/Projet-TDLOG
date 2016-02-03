from django import forms
from .models import *

############################Formulaire etudiant################################

#Informations generales
class ConfForm(forms.Form):
    """
    Formulaire de configuration du module
    """
    
    first_name = forms.CharField( label="Prénom",required=False, widget=forms.TextInput(attrs={'placeholder':'','class':'form-control input-sm'}) )
    last_name = forms.CharField( label="Nom", required=True, widget=forms.TextInput(attrs={'placeholder':'','class':'form-control input-sm'}) )
    departement = forms.CharField(label="Département", required = False)    
    
#Formset d'inscription de disciplines
class SorteForm(forms.Form):

    #Champs multiples
    disci = forms.ModelChoiceField(queryset=Discipline.objects.all(), label="Matière")
    note = forms.FloatField( label="Note sur 20 obtenue",required=False, min_value=0, max_value=20)
    
    
############################Formulaire ecole##################################
#Informations generales
class InfoForm(forms.Form):
    name = forms.CharField( label="Nom", required=True, widget=forms.TextInput(attrs={'placeholder':'','class':'form-control input-sm'}) )
    capacity= forms.IntegerField(label= "Capacité", required = True, min_value =0)
    descrip = forms.CharField(label = "Description", widget=forms.Textarea(attrs={'rows': 6, 'cols': 800}))
#Formset d'inscription de disciplines
class StandardsForm(forms.Form):
    disci = forms.ModelChoiceField(queryset=Discipline.objects.all(), label="Matière")
    standard = forms.FloatField(label = "Coefficient", required = True, min_value = 0, max_value = 1)