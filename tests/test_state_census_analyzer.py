import logging
from unittest import TestCase
from services.state_census_analyzer import StateCensusAnalyzer


class TestStateCensusAnalyzer(TestCase):

    sca = StateCensusAnalyzer()

    def test_records_checker(self):
        file_object = self.sca.csv_loader('../census_file/census.csv')
        if self.sca.records_checker(30, file_object):
            assert True

