import csv
import logging
from Exception.census_analyzer_exception import CensusAnalyzerException

#logging.basicConfig(filename='services/services_log.log', filemode='a', format=f'%(asctime)s - %(message)s',
#                       level=logging.DEBUG)


class StateCensusAnalyzer:

    csv_file = 0

    def csv_loader(self, file_name):
        """
        Prints the csv file and checks if data in csv file is correct or not
        :return: nothing
        """
        try:
            self.csv_file = open(file_name, 'r')
            file_reader = csv.reader(self.csv_file)
            return file_reader
        except Exception:
            logging.exception("Error at loader")

    @staticmethod
    def records_checker(expected, file_reader_object):
        """
        Checks the number of rows present in the file and compares it with the expected number of rows
        :param expected: number of rows expected by user
        :param file_reader_object: loader data
        :return: boolean
        """
        number_of_records = 0
        try:
            for row in file_reader_object:
                number_of_records += 1

            if expected == number_of_records:
                return True
            else:
                raise CensusAnalyzerException("Wrong records")
        except CensusAnalyzerException as e:
            logging.exception(e)
        except Exception:
            logging.exception("Error at record checker")

    def file_closer(self):
        """
        Closes the file object
        :return:
        """
        self.csv_file.close()

    def file_type_checker(self):
        """
        check the file extension
        :return: true or raise exception
        """
        if self.csv_file.name.endswith(".csv"):
            return True
        else:
            raise CensusAnalyzerException("Wrong file type")

    @staticmethod
    def file_delimiter_checker(file_path):
        """
        File delimiter checker
        :param file_path:
        :return:
        """
        with open(file_path, newline='') as file:
            file_lines = csv.Sniffer().sniff(file.read())
            if file_lines.delimiter == ',':
                return True
            else:
                raise CensusAnalyzerException("Wrong delimiter")

    @staticmethod
    def header_checker(file_path):
        """
        Check if the given file has header
        :param file_path:
        :return:
        """
        with open(file_path, newline='') as file:
            file_lines = csv.Sniffer().has_header(file.read())
            if file_lines:
                return True
            else:
                raise CensusAnalyzerException("No header")





