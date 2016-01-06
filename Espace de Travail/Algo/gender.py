from profile import man, woman
# il faut que le fichier "profile.py" soit placé dans le même dossier que "gender.py"
import random

male_names = ['lucien', 'pierre bastard' ,'andréas', 'clément', 'léo', 'adrien', 'pierre', 'remi', 'dan']
female_names = ['claire', 'solène', 'anna', 'marion', 'caro', 'gaelle', 'sonia', 'aude']

subjects_guy = ['french', 'english', 'maths', 'physiques', 'biology', 'spanish', 'phylosophy', 'economy', 'sport']
subjects_girl = ['international', 'price', 'prestige', 'doubledegree', 'accessibility', 'campus', 'bite']


guys = []
girls = []

for name in male_names:
	guy = man(name)
	guy.set_results(subjects_guy)
	guy.set_standards(subjects_girl)
	guys.append(guy)
for name in female_names:
	girl = woman(name)
	girl.set_results(subjects_girl)
	girl.set_standards(subjects_guy)
	girls.append(girl)


guyprefers = {}
galprefers = {}


for guy in guys:
	guy.grade(girls)
	guy.classify()
	guyprefers[guy.name] = guy.preferences

for girl in girls:
	girl.grade(guys)
	girl.classify()
	galprefers[girl.name] = girl.preferences

print('\n', guyprefers, '\n', galprefers)

capacity = {}
for name in female_names:
	capacity[name] = 1

class preferences:
	def __init__(self):
		self.guyprefers = guyprefers
		self.galprefers = galprefers
		self.capacity = capacity





