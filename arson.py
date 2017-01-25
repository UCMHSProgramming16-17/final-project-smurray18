#import modules

import pandas as pd
import bokeh

# create a reader for the data

df = pd.read_csv('crimedata.csv')

# import the plotting tools

from bokeh.charts import Bar, output_file, save

p = Bar(df, label='county_name', values='ARSON', title='The Amount of Arson in the Country', color='pink')

# you need to be able to save the file

output_file('arsondata.html')

save(p)