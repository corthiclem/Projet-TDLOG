import unittest
import match
import copy
import random


class TestDeCase(unittest.TestCase):
    """Test la fiabilite du match"""
    
    def test_1_check_stability(self):
        """Verifie que la stabilite du match"""
        self.assertTrue(match.check(engaged))
        print('Engagement stability check PASSED'
          if match.check(engaged) else 'Engagement stability check FAILED')
        print()

    def test_2_check_instability(self):
        """Verifie l'instabilite du match si l'on introduit volontairement une erreur"""
        gals = engaged.keys()
        engaged2 = copy.deepcopy(engaged)
        she1,she2 = random.sample(gals, 2)
        index1 = random.randint(0, len(engaged[she1])-1)
        index2 = random.randint(0, len(engaged[she2])-1)
        print('\n\nSwapping two fiances to introduce an error')
        engaged2[she1][index1], engaged2[she2][index2] = engaged2[she2][index2], engaged2[she1][index1]
        for gal in (she1,she2):
            for guy in engaged2[gal]:
                if guy not in engaged[gal]:
                    print('  %s is now engaged to %s' % (gal, guy))
        print()
        self.assertTrue(not match.check(engaged2))
        print('Engagement instability check PASSED'
              if not match.check(engaged2) else 'Engagement instability check FAILED')


###################################### MAIN ########################################
if __name__ == '__main__':
    engaged = match.matchmaker()
    match.displayCouples(engaged)
    unittest.main()