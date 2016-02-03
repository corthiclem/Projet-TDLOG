import copy
import random
import unittest

class man:
	def __init__(self, profile):
		assert(profile['gender'] == 'male')
		self.gender = 'male'
		self.name = profile['name']
		self.results = profile['results']
		self.preferences = profile['preferences']


class woman():
	def __init__(self, profile):
		assert(profile['gender'] == 'female')
		self.gender = 'female'
		self.name = profile['name']
		self.standards = profile['standards']
		self.capacity = profile['capacity']
		self.rating = {}
		self.preferences = []

	def classify(self):
		""" Etablie la liste de preferences a partir de la liste des moyennes de chaque profil etudie """
		rating_sorted_by_value = sorted(self.rating.items(), key=lambda x: x[1], reverse=True)
		print("\n%s's rating sorted by value:" % self.name)
		print(' ', rating_sorted_by_value)
		for name, average in rating_sorted_by_value:
			self.preferences.append(name)
		print("\nList of %s's preferences:" % self.name)
		print(' ', self.preferences)

	def grade(self, guys):
		""" Donne une moyenne a chaque profil etudie """
		for guy in guys:
			numerator = 0
			denominator = 0
			average = 0
			for subject in self.standards.keys():
				if subject in guy.results.keys():
					result = guy.results[subject]
					coeff = self.standards[subject]
					numerator += result * coeff
					denominator += coeff
			if denominator != 0:
				average = numerator / denominator
			else: 
				print("\n %s n'a pas pu evaluer %s et lui a donc mis une moyenne par default de 0."% (self.name, guy.name))
			self.rating[guy.name] = average

	def set_standards(self, subjects):
		k = random.randint(0, len(subjects))
		random_subjects = random.sample(subjects, k) # On cree une liste de k elements issus de la liste subjects pour modeliser
													 # le fait que chaque personne ne regarde pas les memes criteres
		for subject in random_subjects:
			self.standards[subject] = random.randint(0, 10) / 10 # Indice compris entre 0 et 1

	def set_capacity(self):
		self.capacity = random.randint(1,3)