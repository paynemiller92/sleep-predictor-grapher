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
    number_of_participants_under_15minutes_of_exercise = 0
    number_of_participants_under_30minutes_of_exercise = 0
    number_of_participants_under_45minutes_of_exercise = 0
    number_of_participants_under_60minutes_of_exercise = 0
    number_of_participants_over_60minutes_of_exercise = 0
    number_of_erroneous_inputs = 0

    for response in responses:
        try:
            minutes = float(response.week_day_minutes_of_exercises)
            if minutes < 15.0:
                number_of_participants_under_15minutes_of_exercise += 1
            elif minutes < 30.0:
                number_of_participants_under_30minutes_of_exercise += 1
            elif minutes < 45.0:
                number_of_participants_under_45minutes_of_exercise += 1
            elif minutes < 60.0:
                number_of_participants_under_60minutes_of_exercise += 1
            else:
                number_of_participants_over_60minutes_of_exercise += 1
        except ValueError:
            number_of_erroneous_inputs += 1

    data_frame = {
        "Minutes of Exercise": [number_of_participants_under_15minutes_of_exercise,
                                number_of_participants_under_30minutes_of_exercise,
                                number_of_participants_under_45minutes_of_exercise,
                                number_of_participants_under_60minutes_of_exercise,
                                number_of_participants_over_60minutes_of_exercise],
        "Labels": ["Under fifteen minutes",
                   "Between fifteen and thirty minutes",
                   "Between thirty and forty-five minutes",
                   "Between forty-five and sixty minutes",
                   "Over sixty minutes"]
    }

    graph_pie_chart(data_frame, "Average minutes of exercise per weekday", "Minutes of Exercise", "Labels")


def graph_exercise_to_sleep_scatter_plot(responses):
    exercise_minutes = []
    sleep_hours = []
    for response in responses:
        try:
            exercise_minutes.append(float(response.week_day_minutes_of_exercises))
        except ValueError:
            exercise_minutes.append(0)

        try:
            sleep_hours.append(float(response.week_day_hrs_of_sleep) / 60.0)
        except ValueError:
            sleep_hours.append(0)

    data_frame = {
        "Minutes of Exercise": exercise_minutes,
        "Hours of Sleep": sleep_hours
    }
    graph_scatter_plot_with_regression(data_frame, "Hours of Sleep by Exercise Minutes", "Minutes of Exercise", "Hours of Sleep", "lowess")


def graph_naps_to_sleep_scatter_plot(responses):
    nap_minutes = []
    sleep_hours = []
    for response in responses:
        try:
            nap_minutes.append(float(response.week_day_minutes_of_naptime))
        except ValueError:
            nap_minutes.append(0)

        try:
            sleep_hours.append(float(response.week_day_hrs_of_sleep) / 60.0)
        except ValueError:
            sleep_hours.append(0)

    data_frame = {
        "Minutes of Nap Time": nap_minutes,
        "Hours of Sleep": sleep_hours
    }
    graph_scatter_plot_with_regression(data_frame, "Hours of Sleep by Napping Minutes", "Minutes of Nap Time", "Hours of Sleep", "ols")

def graph_pie_chart(data_frame, title, values, names):
    pie_chart = plotly.pie(data_frame, values=values, names=names, title=title)
    pie_chart.for_each_trace(lambda trace: trace.update(textfont_color=WHITE_COLOR, textfont_size=VALUE_FONT_SIZE))
    pie_chart.update_layout(legend=dict(font=dict(size=LEGEND_FONT_SIZE, color=BLACK_COLOR)),
                            legend_title=dict(font=dict(size=LEGEND_FONT_SIZE, color=BLACK_COLOR)))
    pie_chart.show()


def graph_scatter_plot_with_regression(data_frame, title, x_key, y_key, regression):
    scatter_plot = plotly.scatter(data_frame, x=x_key, y=y_key, title=title, trendline=regression)
    scatter_plot.update_traces(
        marker=dict(size=12, line=dict(width=2, color='DarkSlateGrey'))
    )
    scatter_plot.show()
