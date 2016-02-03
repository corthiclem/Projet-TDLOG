from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render, render_to_response
from django.core.context_processors import csrf
from polls.models import  School
from polls.forms import ConfForm, SorteForm
from django.forms import formset_factory, BaseFormSet
from django.template import Template, RequestContext
from .forms import *
import json
import unittest
import sys
sys.path.insert(0, '../projetTest/projetTest/static')
from match import matchmaker
import copy
import random
from database import data

def index_student(request):

    class RequiredFormSet(BaseFormSet):
        def __init__(self, *args, **kwargs):
            super(RequiredFormSet, self).__init__(*args, **kwargs)
            for form in self.forms:
                form.empty_permitted = False

    # Creation du dictionnaire JSON etudiant
    student = {}
    
    student["preferences"] = []
    
    # Initialisation du FORMSET dynamique
    DisciFormSet = formset_factory(SorteForm, extra = 1, max_num=10, formset=RequiredFormSet)
    School_list = School.objects.all()
    
    if request.method == 'POST': # If the form has been submitted...
        infos_form = ConfForm(request.POST) # A form bound to the POST data
        # Create a formset from the submitted data
        disci_formset = DisciFormSet(request.POST, request.FILES)
        
        if infos_form.is_valid() and disci_formset.is_valid():
            #Entree des donnees soumises par l'utilisateur
            student["name"] = infos_form.cleaned_data['first_name'] + '_' + infos_form.cleaned_data['last_name']
            student["results"] = {}
            student["gender"] = "male"
            
            # On parcourt tous les formset crees 
            for form in disci_formset.forms:
                student['results'][str(form.cleaned_data['disci'])] = form.cleaned_data['note']
                print(form.cleaned_data)
                
            
            # On recupere la liste des preferences via des input HTML "hidden"
            var = request.POST.getlist("alist")

            prefer = []
            #Entree des donnees soumises par l'utilisateur
            for i in var:
                s_name = School.objects.get(auto_id = int(i)).name
                prefer.append(s_name)

            student["preferences"] = prefer
            
            
            # Ecriture du Fichier JSON
            with open('data/guys/'+student["name"]+'.json', 'w', encoding='utf-8') as f:
                json.dump(student, f, indent=4, ensure_ascii=False)
            
            return HttpResponse('thanks') # Redirect to a 'success' page
            
    else:
        infos_form = ConfForm()
        disci_formset = DisciFormSet()
    if request.method == 'GET':
        pass
    
    # For CSRF protection
    c = {'infos_form': infos_form,
         'disci_formset': disci_formset,
         'School_list': School_list
        }
    c.update(csrf(request))

    return render_to_response(r'index2.html', c, context_instance=RequestContext(request) )

def index_school(request):
    class RequiredFormSet(BaseFormSet):
        def __init__(self, *args, **kwargs):
            super(RequiredFormSet, self).__init__(*args, **kwargs)
            for form in self.forms:
                form.empty_permitted = False
    # Creation du dictionnaire JSON ecole
    school = {}
    StandFormSet = formset_factory(StandardsForm, extra = 1, max_num=10, formset=RequiredFormSet)
    if request.method == 'POST': # If t form has been submitted...
        infos_form = InfoForm(request.POST) # A form bound to the POST data
        # Create a formset from the submitted data
        stand_formset = StandFormSet(request.POST, request.FILES)
        
        
        
        if infos_form.is_valid() and stand_formset.is_valid():
            
            #Entree des donnees soumises par l'utilisateur
            school["name"] = infos_form.cleaned_data['name']
            school["capacity"] = infos_form.cleaned_data['capacity']
            school["standards"] = {}
            school["gender"] = "female"
            # On parcourt tous les formset crees 
            for form in stand_formset.forms:
                school["standards"][str(form.cleaned_data['disci'])] = form.cleaned_data['standard']
                
            # Ecriture du Fichier JSON
            with open('data/girls/'+school["name"]+'.json', 'w', encoding='utf-8') as f:
                json.dump(school, f, indent=4, ensure_ascii=False)
            
            
            #On enregistre l'ecole creee
            s = School(name = school["name"], capacity = school["capacity"], descrip = infos_form.cleaned_data['descrip'])
            s.save()
            return HttpResponse('thanks') # Redirect to a 'success' page
            
    else:
        infos_form = InfoForm()
        stand_formset = StandFormSet()
    
    c = {'infos_form': infos_form,
         'stand_formset': stand_formset,
        }
    c.update(csrf(request))

    return render_to_response(r'index_school.html', c, context_instance=RequestContext(request) )


#Affichage des resultats
def results(request):
    
    # On lance l'algorithme des mariages stables sur l'ensemble des ecoles et 
    # etudiants inscrits
    d = data()
    guyprefers = d.guyprefers
    galprefers = d.galprefers
    capacity = d.capacity
    engaged, rejected = matchmaker(guyprefers, galprefers, capacity)
    
    #On affiche le resultat et on transmet l'information a la partie HTML
    print(engaged)
    
    c = {'engaged': engaged,
         'rejected': rejected,
        }
    return render_to_response(r'results.html', c)
