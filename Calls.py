import csv


class Calls:

    def from_csvTolist(csvFile):
        with open(csvFile) as csv_file:
            csv_reader = csv.reader(csv_file)
            rows = list(csv_reader)
        return rows

    def allocate(src, dest):
        if (src < dest):  # Up
            return 0
        else:
            return 1

    def write_tofile(rows):
        with open('Ex1_Output/Ex1_Calls_case_1_b.csv', 'w', encoding='UTF8', newline='') as csv_file:
            write = csv.writer(csv_file)
            write.writerows(rows)
