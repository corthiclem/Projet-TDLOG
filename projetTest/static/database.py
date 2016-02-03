from profile import man, woman
# il faut que le fichier "profile.py" soit place dans le meme dossier que "database.py"
#import random_girls, random_guys
import random
import json
import os



class data:
	def __init__(self):
		self.guys = []
		self.girls = []
		self.guyprefers = {}
		self.galprefers = {}
		self.capacity = {}

		# on lance la generation de profiles
		self.rundata()

	def rundata(self):
		self.set_guy_profiles()
		self.set_girl_profiles()
		self.set_preferences()
		self.set_capacity()


	def set_guy_profiles(self):
		for root, dirs, files in os.walk('data/guys'): #### les profiles sont dans 'data_test'
			for name in files:
				doc = os.path.join(root, name)
				try:
					with open(doc, 'r') as f:
						profile = json.load(f)
						guy = man(profile)
						self.guys.append(guy)
				except Exception as e:
					print(" *** Erreur :", e, doc)

	def set_girl_profiles(self):
		for root, dirs, files in os.walk('data/girls'): #### les profiles sont dans 'data_test'
			for name in files:
				doc = os.path.join(root, name)
				try:
					with open(doc, 'r') as f:
						profile = json.load(f)
						girl = woman(profile)
						self.girls.append(girl)
				except Exception as e:
					print(" *** Erreur :", e, doc)

	def set_preferences(self):
     
         for guy in self.guys:                 
             if not guy.preferences:
                 names = list(girl.name for girl in self.girls)
                 guy.preferences = random.sample(names, len(names))
             self.guyprefers[guy.name] = guy.preferences
             print("Preference de" + guy.name +" est:")
             print(guy.preferences)
                 
           
         for girl in self.girls:
             girl.grade(self.guys)
             girl.classify()
             self.galprefers[girl.name] = girl.preferences

	def set_capacity(self):
		for girl in self.girls:
			self.capacity[girl.name] = girl.capacity

