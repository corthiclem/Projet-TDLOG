import copy
import random
import unittest

class Profile():
	""" Cette class definit la structure de n'impote quel profil, homme ou femme, etudiant ou université. """
	def __init__(self, name='', gender=None, capacity=1):
		self.gender = gender
		self.name = name
		self.capacity = capacity
		self.results = {} # dictionnaire de résultats
		self.standards = {} # dictionnaire de criteres
		self.rating = {} # dictionnaire des moyennes des profils étudiés
		self.preferences = [] # liste de preference parmi les profils étudiés

	def classify(self):
		""" Etablie la liste de preferences à partir de la liste des moyennes de chaque profil étudié """
		rating_sorted_by_value = sorted(self.rating.items(), key=lambda x: x[1], reverse=True)
		print("\n%s's rating sorted by value:" % self.name)
		print(' ', rating_sorted_by_value)
		for name, average in rating_sorted_by_value:
			self.preferences.append(name)
		print("\nList of %s's preferences:" % self.name)
		print(' ', self.preferences)

	def grade(self, profiles):
		""" Donne une moyenne à chaque profil étudié """
		for profile in profiles:
			numerator = 0
			denominator = 0
			average = 0
			for subject in self.standards.keys():
				if subject in profile.results.keys():
					result = profile.results[subject]
					coeff = self.standards[subject]
					numerator += result * coeff
					denominator += coeff
			if denominator != 0:
				average = numerator / denominator
			else: 
				print("\n %s n'a pas pu évaluer %s et lui a donc mis une moyenne par default de 0."% (self.name, profile.name))
			self.rating[profile.name] = average

	def set_results(self, subjects):
		for subject in subjects:
			self.results[subject] = random.randint(0, 20) # Loi normale tu connais ? random.normalvariate(nu, sigma)

	def set_standards(self, subjects):
		k = random.randint(0, len(subjects))
		random_subjects = random.sample(subjects, k) # On crée une liste de k éléments issus de la liste subjects pour modéliser
													 # le fait que chaque personne ne regarde pas les mêmes critères
		for subject in random_subjects:
			self.standards[subject] = random.randint(0, 10) / 10 # Indice compris entre 0 et 1

	def set_capacity(self):
		if self.gender == 'female':
			self.capacity = random.randint(1,3)


class man(Profile):
	def __init__(self, name):
		super().__init__(name, 'male')

class woman(Profile):
	def __init__(self, name):
		super().__init__(name, 'female')
		self.set_capacity()