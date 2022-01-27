import logging
from unittest import TestCase
from services.state_census_analyzer import StateCensusAnalyzer


class TestStateCensusAnalyzer(TestCase):

    sca = StateCensusAnalyzer()

    def test_records_checker_correct_records(self):
        file_object = self.sca.csv_loader('../census_file/census.csv')

    def test_records_checker_wrong_records(self):
        file_object = self.sca.csv_loader('../census_file/tt1_2.csv')
        value = self.sca.records_checker(30, file_object)
        self.sca.file_closer()
        self.assertEqual(value, False)
