from pandas import *
from ggplot import *

def plot_weather_data(turnstile_weather):

    plot = ggplot(aes(x = 'Hour', y = 'ENTRIESn_hourly'), data = turnstile_weather) + geom_point(aes(alpha = .5)) + \
    ggtitle('Entries by Hour') + xlab('Hour') + ylab('Number of Entries per Day')
    return plot
