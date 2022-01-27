from services.state_census_analyzer import StateCensusAnalyzer


if __name__ == "__main__":
    sca = StateCensusAnalyzer()
    sca_reader = sca.csv_loader('census_file/census.csv')
    print(sca.records_checker(30, sca_reader))

