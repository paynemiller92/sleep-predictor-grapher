from reader import read_questionnaire
from grapher import graph_average_hours_of_sleep
from grapher import graph_average_minutes_of_exercise
from grapher import graph_exercise_to_sleep_scatter_plot
from grapher import graph_naps_to_sleep_scatter_plot
from grapher import graph_drinks_to_sleep_scatter_plot
from grapher import graph_screen_time_to_sleep_hours

if __name__ == '__main__':
    responses = read_questionnaire()
    graph_average_hours_of_sleep(responses)
    graph_average_minutes_of_exercise(responses)
    graph_exercise_to_sleep_scatter_plot(responses)
    graph_naps_to_sleep_scatter_plot(responses)
    graph_drinks_to_sleep_scatter_plot(responses)
    graph_screen_time_to_sleep_hours(responses)
