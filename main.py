from reader import read_questionnaire
from grapher import graph_average_hours_of_sleep

if __name__ == '__main__':
    responses = read_questionnaire()
    graph_average_hours_of_sleep(responses)
