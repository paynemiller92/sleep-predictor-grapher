import csv

class Response:
    week_day_hrs_of_sleep = 0
    week_day_minutes_of_naptime = 0
    week_day_minutes_of_exercises = 0

    @staticmethod
    def from_csv_record(record):
        response = Response()
        response.week_day_hrs_of_sleep = record['Q5']
        response.week_day_minutes_of_naptime = record['q8']
        response.week_day_minutes_of_exercises = record['Q38']
        return response
