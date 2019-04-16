# Import figure from bokeh.plotting
from bokeh.plotting import figure, ColumnDataSource

# Import output_file and show from bokeh.io
from bokeh.io import output_file, show

#Import CategoricalColorMapper from bokeh.models
from bokeh.models import CategoricalColorMapper

import pandas as pd

data_dir = "/Users/wel51x/Box Sync/MyBox/Code/DataCamp/bokeh/Data/"
output_dir = "/Users/wel51x/Box Sync/MyBox/Code/DataCamp/bokeh/Output/"

# Read in the CSV file: df
#df = pd.read_csv('autos.csv')
df = pd.read_csv(data_dir+'auto.csv')

# Convert df to a ColumnDataSource: source
source = ColumnDataSource(df)

# Make a CategoricalColorMapper object: color_mapper
color_mapper = CategoricalColorMapper(factors=['Europe', 'Asia', 'US'],
                                      palette=['red', 'green', 'blue'])

# Create the figure: p
#p = figure(x_axis_label='Displacement', y_axis_label='MPG')
p = figure(x_axis_label='Weight', y_axis_label='MPG', title="Weight vs MPG")
p.title.align='center'

# Plot mpg vs hp by color
#p.circle(df.displacement, df.mpg, color=df['color'], size=10)
p.circle('weight', 'mpg', source=source,
            color=dict(field='origin', transform=color_mapper),
            legend='origin')

# Specify the name of the output file and show the result
output_file(output_dir+'ex4auto-colormap.html')
show(p)
