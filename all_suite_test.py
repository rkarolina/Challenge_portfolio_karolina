import unittest

from unittest.loader import makeSuite

from test_cases.add_a_new_match import TestAddNewMatch
from test_cases.download_players_csv_list import TestDownloadCsvFile
from test_cases.framework import Test
from test_cases.go_to_add_a_new_player import TestAddPlayer
from test_cases.go_to_edit_new_player import TestEditPlayer
from test_cases.login_to_the_system import TestLoginPage
from test_cases.filter_player import TestFilterPlayer


def full_suite():
   test_suite = unittest.TestSuite()
   test_suite.addTest(makeSuite(TestLoginPage))
   test_suite.addTest(makeSuite(TestDownloadCsvFile))
   test_suite.addTest(makeSuite(TestAddPlayer))
   test_suite.addTest(makeSuite(TestFilterPlayer))
   test_suite.addTest(makeSuite(TestAddNewMatch))
   test_suite.addTest(makeSuite(TestEditPlayer))
   return test_suite

if __name__ == '__main__':
   runner = unittest.TextTestRunner(verbosity=2)
   runner.run(full_suite())
