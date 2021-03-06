import unittest
import match
import copy
import random
from database import data

# mode TEST
TEST = False

d = data()
guyprefers = d.guyprefers
galprefers = d.galprefers
capacity = d.capacity


class TestDeCase(unittest.TestCase):
    """Test la fiabilite du match"""
    def setUp(self):
        self.engaged, self.rejected = match.matchmaker(guyprefers, galprefers, capacity)
    
    def test_1_check_stability(self):
        """Verifie que la stabilite du match"""
        self.assertTrue(match.check(self.engaged, guyprefers, galprefers))
        print('Engagement stability check PASSED'
          if match.check(self.engaged, guyprefers, galprefers) else 'Engagement stability check FAILED')
        print()

    def test_2_check_instability(self):
        """Verifie l'instabilite du match si l'on introduit volontairement une erreur"""
        for _ in range(10):
            gals = self.engaged.keys()
            engaged2 = copy.deepcopy(self.engaged)
            she1,she2 = random.sample(gals, 2)
            index1 = random.randint(0, len(engaged2[she1])-1)
            index2 = random.randint(0, len(engaged2[she2])-1)
            print('\n\nSwapping two fiances to introduce an error')
            engaged2[she1][index1], engaged2[she2][index2] = engaged2[she2][index2], engaged2[she1][index1]
            for gal in (she1,she2):
                for guy in engaged2[gal]:
                    if guy not in self.engaged[gal]:
                        print('  %s is now engaged to %s' % (gal, guy))
            print()
            self.assertTrue(not match.check(engaged2, guyprefers, galprefers))
            print('Engagement instability check PASSED'
                  if not match.check(engaged2, guyprefers, galprefers) else 'Engagement instability check FAILED')


###################################### MAIN ########################################
if __name__ == '__main__':
    if not TEST:
        # si le mode test n'est pas active
        engaged, rejected = match.matchmaker(guyprefers, galprefers, capacity)
    else:
        unittest.main()
