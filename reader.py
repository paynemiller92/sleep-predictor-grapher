import csv
from response import Response


def read_questionnaire():
    responses = []
    with open('questionnaire.csv', newline='') as csv_file:
        reader = csv.DictReader(csv_file, delimiter=',', quotechar='|')
        for row in reader:
            responses.append(Response.from_csv_record(row))
    return responses
