class Profile():
	""" Cette class definit la structure de n'impote quel profil, homme ou femme, etudiant ou université. """
	def __init__(self, name):
		self.name = name
		self.results = {} # dictionnaire de résultats
		self.standards = {} # dictionnaire de criteres
		self.rating = {} # dictionnaire des moyennes des profils étudiés
		self.preferences = [] # liste de preference parmi les profils étudiés

	def classify(self):
		rating_sorted_by_value = sorted(self.rating.items(), key=lambda x: x[1])
		print("\n%s's rating sorted by value:" % self.name)
		print(' ', rating_sorted_by_value)
		for name, average in rating_sorted_by_value:
			self.preferences.append(name)
		print("\nList of %s's preferences:" % self.name)
		print(' ', self.preferences)

	def grade(self, profiles):
		for profile in profiles:
			numerator = 0
			denominator = 0
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
				average = 0
			self.rating[profile.name] = average

class man(Profile):
	def __init__(self, name):
		super().__init__(name)

class woman(Profile):
	def __init__(self, name):
		super().__init__(name)