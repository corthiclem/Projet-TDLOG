import json
import os
import random
import threading

names = ['lucien', 'pierre bastard' ,'andreas', 'clement', 'leo', 'adrien', 'pierre', 'remi', 'dan', 'tom', 'bob', 'thomas', 'louis', 'nicolas', 'hippolyte',
		 'claire', 'solene', 'gaelle', 'anna', 'thibault', 'lucas', 'sonia', 'marion', 'oussman', 'robin', 'pichon', 'simon', 'aude', 'davide', 'bobby']
subjects = ['french', 'english', 'maths', 'physics', 'biology', 'spanish', 'phylosophy', 'economy', 'sport', 'musique',]

save_path = 'data/guys'

def set_results():
	results = {}
	for subject in subjects:
		results[subject] = random.randint(0, 20)
	return results

def set_profile(name):
	profile = {}
	profile['gender'] = 'male'
	profile['name'] = name
	profile['results'] = set_results()
	profile['preferences'] = []
	return profile

def create_profile():
	global verrou
	verrou.acquire()
	for name in names:
		filename = name
		completeName = os.path.join(save_path, filename+".json")
		out_file = open(completeName, "w")
		data = set_profile(name)
		json.dump(data, out_file, indent=4)
	verrou.release()

verrou = threading.Lock()
t = threading.Thread(target=create_profile)
t.start()
t.join()
