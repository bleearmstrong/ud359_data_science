from pandas import *
from ggplot import *

import pandas

def lineplot(hr_year_csv):
    
    hr_year_data = pandas.read_csv(hr_year_csv)
    gg = ggplot(aes(x = 'yearID', y = 'HR'), data = hr_year_data) + geom_point(aes(color = 'red')) + \
    geom_line(aes(color = 'red')) + \
    ggtitle('Homeruns by Year') + \
    xlab('Year') + \
    ylab('Homeruns')
    return gg
