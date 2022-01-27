import csv
import random


class CensusGenerator:
    list_of_states = ["UttarPradesh", "Maharashtra", "Bihar", "WestBengal", "MadhyaPradesh", "TamilNadu",
                      "Rajasthan", "Karnataka", "Gujarat", "AndhraPradesh", "Odisha", "Telangana", "Kerala",
                      "Jharkhand", "Assam", "Punjab", "Chattisgarh", "Haryana", "JammuandKashmir", "Uttarakhand",
                      "HimachalPradesh", "Tripura", "Meghalaya", "Manipur", "Nagaland", "Goa", "ArunachalPradesh",
                      "Mizoram", "Sikkim"]

    @staticmethod
    def generate_random_population_number():
        return random.randrange(1000000, 1000000000)

    def csv_generator(self):
        with open('census.csv', 'w', newline='') as csv_file:
            header = ["States", "Population", "StateCode"]
            writer_object = csv.writer(csv_file, delimiter=',', )
            writer_object.writerow(header)
            for state in self.list_of_states:
                data = [state, self.generate_random_population_number(), random.randrange(100000, 999999)]
                writer_object.writerow(data)


CensusGenerator().csv_generator()