import csv

class calls:


    def from_csv(csvFile):
        with open(csvFile) as mycsv_file:
            csv_reader = csv.reader(mycsv_file)
            callsLine=list(csv_reader)
        return callsLine




