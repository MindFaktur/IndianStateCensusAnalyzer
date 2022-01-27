import csv
import logging

#logging.basicConfig(filename='services/services_log.log', filemode='a', format=f'%(asctime)s - %(message)s',
 #                       level=logging.DEBUG)


class StateCensusAnalyzer:

    @staticmethod
    def csv_loader(file_name):
        """
        Prints the csv file and checks if data in csv file is correct or not
        :return: nothing
        """
        try:
            csv_file = open(file_name, 'r')
            file_reader = csv.reader(csv_file)
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
        except Exception:
            logging.exception("Error at record checker")



