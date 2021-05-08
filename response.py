import csv

class Response:
    week_day_hrs_of_sleep = 0
    week_day_mins_of_exercises = 0

    @staticmethod
    def from_csv_record(record):
        response = Response()
        response.week_day_mins_of_exercises = 0
        response.week_day_hrs_of_sleep = record['Q5']
        return response
