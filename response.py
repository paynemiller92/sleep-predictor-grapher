

class Response:
    week_day_hrs_of_sleep = 0
    week_day_minutes_of_naptime = 0
    week_day_minutes_of_exercises = 0
    number_of_drinks_consumed = 0
    minutes_of_screentime = 0

    @staticmethod
    def from_csv_record(record):
        response = Response()
        response.week_day_hrs_of_sleep = record['Q5']
        response.week_day_minutes_of_naptime = record['q8']
        response.number_of_drinks_consumed = record['q28']
        response.week_day_minutes_of_exercises = record['Q38']
        response.minutes_of_screentime = record['Q43B']
        return response
