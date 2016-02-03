from profile import man, woman
# il faut que le fichier "profile.py" soit placé dans le même dossier que "database.py"
import random
import json

male_names = ['lucien', 'pierre bastard' ,'andréas', 'clément', 'léo', 'adrien', 'pierre', 'remi', 'dan', 'tom', 'bob', 'thomas', 'louis', 'nicolas', 'hyppolite']
female_names = ['claire', 'solène', 'anna', 'marion']

subjects_guy = ['french', 'english', 'maths', 'physiques', 'biology', 'spanish', 'phylosophy', 'economy', 'sport']
subjects_girl = ['international', 'price', 'prestige', 'doubledegree', 'accessibility', 'campus']

class data:
	def __init__(self):
		self.guys = []
		self.girls = []
		self.guyprefers = {}
		self.galprefers = {}
		self.capacity = {}

		# on lance la génération de profiles
		self.rundata()

	def rundata(self):
		self.set_profiles()
		self.set_preferences()
		self.set_capacity()

	def set_profiles(self):
		for name in male_names:
			guy = man(name)
			guy.set_results(subjects_guy)
			guy.set_standards(subjects_girl)
			self.guys.append(guy)
		for name in female_names:
			girl = woman(name)
			girl.set_results(subjects_girl)
			girl.set_standards(subjects_guy)
			self.girls.append(girl)

	def set_capacity(self):
		for girl in self.girls:
			self.capacity[girl.name] = girl.capacity

	def set_preferences(self):
		for guy in self.guys:
			guy.grade(self.girls)
			guy.classify()
			self.guyprefers[guy.name] = guy.preferences
		for girl in self.girls:
			girl.grade(self.guys)
			girl.classify()
			self.galprefers[girl.name] = girl.preferences

