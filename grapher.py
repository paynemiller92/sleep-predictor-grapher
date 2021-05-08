import plotly.express as plotly

WHITE_COLOR = 'white'
BLACK_COLOR = 'black'
VALUE_FONT_SIZE = 20
LEGEND_FONT_SIZE = 24


def graph_average_hours_of_sleep(responses):
    number_of_participants_under_5hrs_of_sleep = 0
    number_of_participants_under_6hrs_of_sleep = 0
    number_of_participants_under_7hrs_of_sleep = 0
    number_of_participants_under_8hrs_of_sleep = 0
    number_of_participants_over_8hrs_of_sleep = 0
    number_of_erroneous_inputs = 0
    for response in responses:
        try:
            hours = float(response.week_day_hrs_of_sleep) / 60.0
            if hours < 5.0:
                number_of_participants_under_5hrs_of_sleep += 1
            elif hours < 6.0:
                number_of_participants_under_6hrs_of_sleep += 1
            elif hours < 7.0:
                number_of_participants_under_7hrs_of_sleep += 1
            elif hours < 8.0:
                number_of_participants_under_8hrs_of_sleep += 1
            else:
                number_of_participants_over_8hrs_of_sleep += 1
        except ValueError:
            number_of_erroneous_inputs += 1
    data_frame = {
        "Hours of Sleep": [number_of_participants_under_5hrs_of_sleep,
                           number_of_participants_under_6hrs_of_sleep,
                           number_of_participants_under_7hrs_of_sleep,
                           number_of_participants_under_8hrs_of_sleep,
                           number_of_participants_over_8hrs_of_sleep],
        "Labels": ["Under five hours",
                   "Between five and six hours",
                   "Between six and seven hours",
                   "Between seven and eight hours",
                   "Over eight hours"]
    }
    pie_chart = plotly.pie(data_frame, values='Hours of Sleep', names='Labels', title='Avg. hours of sleep per weekday')
    pie_chart.for_each_trace(lambda trace: trace.update(textfont_color=WHITE_COLOR, textfont_size=VALUE_FONT_SIZE))
    pie_chart.update_layout(legend=dict(font=dict(size=LEGEND_FONT_SIZE, color=BLACK_COLOR)),
                            legend_title=dict(font=dict(size=LEGEND_FONT_SIZE, color=BLACK_COLOR)))
    pie_chart.show()

def graph_average_minutes_of_exercise(responses):
    


def round_value(value):
    return 0.0
