

import random
import copy
import unittest
import json
import os
from database import data

# guyprefers = data().guyprefers
# galprefers = data().galprefers
# capacity = data().capacity

# guys = sorted(guyprefers.keys())
# gals = sorted(galprefers.keys())



# guyprefers= {
#  'abe':  ['abi', 'cath', 'bea'],
#  'bob':  ['cath', 'abi', 'bea'],
#  'col':  ['abi', 'bea', 'cath'],
#  'dan':  ['bea', 'cath', 'abi'],
#  'ed':   ['bea', 'cath', 'abi'],
#  'fred': ['bea', 'abi', 'cath'],
#  'gav':  ['bea', 'cath', 'abi'],
#  'hal':  ['abi', 'cath', 'bea'],
#  'ian':  ['cath', 'bea', 'abi'],
#  'jon':  ['abi', 'bea', 'cath'],
#  }

# galprefers = {
#  'abi':  ['bob', 'fred', 'jon', 'gav', 'ian', 'abe', 'dan', 'ed', 'col', 'hal'],
#  'bea':  ['bob', 'abe', 'col', 'fred', 'gav', 'dan', 'ian', 'ed', 'jon', 'hal'],
#  'cath': ['fred', 'bob', 'ed', 'gav', 'hal', 'col', 'ian', 'abe', 'dan', 'jon'],
#  }

# capacity = {
#     'abi':  4,
#     'bea':  3,
#     'cath': 1,
# }

###############################################################################

def inversedict(dico):
    """ Inverse la clef et la valeur d'un dico """
    inversedico = {}
    for she,they in dico.items():
        for he in they:
            inversedico[he] = she
    return inversedico
 
def check(engaged, guyprefers, galprefers):
    """ Teste la stability du dictionnaire de match 'engaged' 
        Le dictionnaire engaged est de la forme {'fille' : ['garcon1', 'garcon2', 'garcon3']}
    """
    # On commence par creer le dictionnaire de match reciproque
    # Il est de la forme {'garcon': 'fille'}
    inverseengaged = inversedict(engaged)
    for she, they in engaged.items():
        # pour chaque garcon dans sa liste de partenaires
        for he in they:
            # on regarde la liste de preferences de la fille 'she'
            shelikes = galprefers[she]
            # on regarde parmi sa liste de preference lesquelles sont mieux classes que son partenaire actuel 'he'
            shelikesbetter = shelikes[:shelikes.index(he)]
            # on regarde la liste de preference de 'he'
            helikes = guyprefers[he]
            # on regarde parmi sa liste de preference lesquelles sont mieux classees que sa partenaire actuel 'she'
            helikesbetter = helikes[:helikes.index(she)]
            # pour chaque garcon qu'elle prefere plus que son partenaire actuel 'he'
            for guy in shelikesbetter:
                # s'il ne figure pas dans la liste de ses partenaires actuels
                if guy not in engaged[she]:
                    # si 'guy' possede une partenaire
                    if guy in inverseengaged.keys():
                        # on regarde qui est la partenaire actuelle de ce garcon 'guy'
                        guysgirl = inverseengaged[guy]
                        # On regarde sa liste de preference de filles
                        guylikes = guyprefers[guy]
                        # si sa partenaire actuelle est moins bien classee que 'she' dans sa liste de preference
                        # cela signifie qu'ils pourraient respectivement lacher leur partenaire actuel pour se mettre
                        # en couple tous les 2 car ils s'aiment plus qu'ils n'aiment leur partenaire actuel
                        if guylikes.index(guysgirl) > guylikes.index(she):
                            print("%s and %s like each other better than "
                                  "their present partners: %s and %s, respectively"
                                  % (she, guy, he, guysgirl))
                            # le match est donc instable
                            return False
                    # si 'guy' est sans partenaire
                    else:
                        # alors le match n'est pas stable car 'she' prefererait etre en couple avec 'guy' plutot que 'he'
                        return False
            # pour chaque fille qu'il prefere a sa partenaire actuelle 'she'
            for gal in helikesbetter:
                # on regarde le partenaire actuel de cette fille 'gal'
                girlsthey = engaged[gal]
                # on regarde la liste de preference de cette fille 'gal'
                gallikes = galprefers[gal]
                # pour chaque garcon 'girlsguy' dans sa liste de partenaires actuels
                for girlsguy in girlsthey:
                    # si son partenaire actuel 'girlsguy' est moins bien classe que 'he' dans sa liste de preference
                    # cela signifie qu'ils pourraient respectivement lacher leur partenaire actuel pour se mettre
                    # en couple tous les 2 car ils s'aiment plus qu'ils n'aiment leur partenaire actuel
                    if gallikes.index(girlsguy) > gallikes.index(he):
                        print("%s and %s like each other better than "
                              "their present partners: %s and %s, respectively"
                              % (he, gal, she, girlsguy))
                        # le match est donc instable
                        return False
    return True

def orderlist(she, fiances, galprefers):
    """ordonne la liste des fiances dans l'ordre de preference"""
    liste = []
    for guy in galprefers[she]:
        if guy in fiances:
            liste.append(guy)
    return liste

def matchmaker(guyprefers, galprefers, capacity):
    guys = sorted(guyprefers.keys())
    gals = sorted(galprefers.keys())
    # on injecte tous les garcons dans la boucle de match
    guysfree = guys[:]
    # on initialise le dictionnaire de match
    engaged  = dict((she,[]) for she in gals)
    guyprefers2 = copy.deepcopy(guyprefers)
    galprefers2 = copy.deepcopy(galprefers)
    # tant qu'il y a des garcon dans la boucle de match, on continue
    while guysfree:
        # on sort le premier garcon de la boucle
        guy = guysfree.pop(0)
        # on regarde sa liste de preferences
        guyslist = guyprefers2[guy]
        # il se dirige vers la fille qu'il n'a jamais encore rencontre et qui est situee le plus haut sur sa liste de preference
        gal = guyslist.pop(0)
        # on regarde la liste des fiances actuels de cette fille 'gal'
        fiances = engaged.get(gal)
        # si la fille a moins de fiances qu'elle n'aimerait en avoir
        if len(fiances) < capacity[gal]:
            # alors on engage 'guy' avec 'gal'
            engaged[gal].append(guy)
            # et on reordonne sa liste de fiances dans l'ordre de ses preferences
            engaged[gal] = orderlist(gal, engaged[gal], galprefers)
            print("  %s and %s" % (guy, gal))
        # si la fille a deja atteint sont nombre limite de fiances
        else:
            # on regarde parmi ses fiances celui qu'elle prefere le moins
            lastfiance = engaged[gal][-1]
            # on regarde sa liste de preferences
            galslist = galprefers2[gal]
            # si elle prefere le nouveau garcon 'guy' a 'lastfiances'
            if galslist.index(lastfiance) > galslist.index(guy):
                # alors elle retire 'lastfiances' de sa liste de fiances
                del engaged[gal][-1]
                # pour se fiancer avec 'guy'
                engaged[gal].append(guy)
                # puis elle remet de l'ordre dans sa liste de fiances
                engaged[gal] = orderlist(gal, engaged[gal], galprefers)
                print("  %s dumped %s for %s" % (gal, lastfiance, guy))

                # si 'lastfiances' a encore des filles a aller voir
                if guyprefers2[lastfiance]:
                    # alors on le reinjecte dans la boucle de match
                    guysfree.append(lastfiance)

            # sinon, si la fille reste fidele a sa liste de fiances
            else:
                # si 'guy' a encore des filles a aller voir
                if guyslist:
                    # alors on le reinjecte dans la boucle de match
                    guysfree.append(guy)

    rejected = rejectedGuys(engaged, guys)
    displayCouples(engaged)
    displayRejected(rejected)
    print_results(engaged, rejected)
    return engaged, rejected

def displayCouples(engaged):     
    print('\nCouples:')
    for she,they in sorted(engaged.items()):
        print('  ' + ',\n  '.join('%s is engaged to %s' % (she,he)
                                  for he in they))
    print()

def rejectedGuys(engaged, guys):
    rejected = []
    inverseengaged = inversedict(engaged)
    for guy in guys:
        if guy not in inverseengaged.keys():
            rejected.append(guy)
    return rejected

def displayRejected(rejected):
    print('\nRejected Guys:')
    print(' ' + ',\n '.join('%s is rejected' % guy
                                for guy in rejected))
    print()


####################################################################################################
# PRINT RESULTS IN A FILE

save_path = 'data/results'

def print_results(engaged, rejected):
    print_engaged(engaged)
    print_inverseengaged(engaged)
    print_rejected(rejected)

def print_engaged(engaged):
    filename = 'engaged'
    completeName = os.path.join(save_path, filename+".json")
    out_file = open(completeName, "w")
    data = engaged
    json.dump(data, out_file, indent=4)

def print_inverseengaged(engaged):
    filename = 'inverseengaged'
    completeName = os.path.join(save_path, filename+".json")
    out_file = open(completeName, "w")
    data = inversedict(engaged)
    json.dump(data, out_file, indent=4)

def print_rejected(rejected):
    filename = 'rejected'
    completeName = os.path.join(save_path, filename+".json")
    out_file = open(completeName, "w")
    data = rejected
    json.dump(data, out_file, indent=4)
