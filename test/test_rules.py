''' 
Unit test for value module

copyright 2010 by Jonathan Lundell
'''
import unittest
import sys, os
path = os.path.normpath(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))
if path not in sys.path: sys.path.insert(0, os.path.normpath(path))

from packages import rules as R
from packages.rules.meek import Rule as Meek
from packages.rules.mpls import Rule as Mpls
from packages.rules.wigm import Rule as WIGM


class RuleTest(unittest.TestCase):
    "test rules class methods"
    
    def testMeekReportMode(self):
        "meek.Rule report mode is meek"
        self.assertEqual(Meek.reportMode(), 'meek')

    def testWIGMReportMode(self):
        "meek.Rule report mode is meek"
        self.assertEqual(WIGM.reportMode(), 'wigm')

    def testMplsReportMode(self):
        "meek.Rule report mode is meek"
        self.assertEqual(Mpls.reportMode(), 'wigm')

    def testMeekNameClass(self):
        "test name to class"
        self.assertEqual(R.electionRule('meek'), Meek)
        
    def testWIGMNameClass(self):
        "test name to class"
        self.assertEqual(R.electionRule('wigm'), WIGM)
        
    def testMplsNameClass(self):
        "test name to class"
        self.assertEqual(R.electionRule('mpls'), Mpls)
        
if __name__ == '__main__':
    unittest.main()