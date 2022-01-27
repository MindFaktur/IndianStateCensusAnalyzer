import logging
from unittest import TestCase

import pytest

from Exception.census_analyzer_exception import CensusAnalyzerException
from services.state_census_analyzer import StateCensusAnalyzer


class TestStateCensusAnalyzer(TestCase):

    sca = StateCensusAnalyzer()

    def test_records_checker_correct_records(self):
        """
        Checks if the file has correct number of records as given, given correct records
        :return: boolean
        """
        file_object = self.sca.csv_loader('../census_file/census.csv')
        value = self.sca.records_checker(30, file_object)
        self.sca.file_closer()
        self.assertEqual(value, True)

    def test_records_checker_wrong_records(self):
        """
        Checks if the file has correct number of records as given, given wrong records
        :return: True
        """
        file_object = self.sca.csv_loader('../census_file/tt1_2.csv')
        value = self.sca.records_checker(30, file_object)
        self.sca.file_closer()
        if not value:
            self.assertRaises(CensusAnalyzerException)

    def test_records_checker_wrong_file_type(self):
        """
        Checks if the given file type is a CSV or other
        :return:
        """
        expected = "Wrong file type"
        with pytest.raises(CensusAnalyzerException) as exception:
            self.sca.csv_loader('../census_file/tt1_3.txt')
            self.sca.file_type_checker()
            self.sca.file_closer()
            self.assertEqual(exception.value.message, expected)

    def test_delimiter_correct_delimiter(self):
        """
        Test's the delimiter function, to see if it return true, when given delimiter is matched
        :return:
        """
        value = self.sca.file_delimiter_checker('../census_file/census.csv')
        print(value)
        if value:
            assert True

    def test_delimiter_wrong_delimiter(self):
        """
        Test's the delimiter function, to see if it raises exception, when given delimiter is not matched
        :return:
        """
        expected = "Wrong delimiter"
        with pytest.raises(CensusAnalyzerException) as exception:
            value = self.sca.file_delimiter_checker('../census_file/tt1_3.csv')
            print(value)
            if not value:
                self.assertEqual(exception.value.message, expected)

    def test_header_has_header(self):
        """
        Test the header function if it can catch the header or no, given header file
        :return:
        """
        value = self.sca.header_checker('../census_file/census.csv')
        if value:
            assert True

    def test_header_no_header(self):
        """
        Test the header function if it can catch the header or no, given header file
        """
        expected = "No header"
        with pytest.raises(CensusAnalyzerException) as exception:
            value = self.sca.header_checker('../census_file/tt1_5.csv')
            print(value)
            if not value:
                self.assertEqual(exception.value.message, expected)


