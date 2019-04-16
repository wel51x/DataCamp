from bokeh.io import output_file, show
from bokeh.plotting import figure
from bokeh.models import CategoricalColorMapper
from bokeh.sampledata.iris import flowers

data_dir = "/Users/wel51x/Box Sync/MyBox/Code/DataCamp/bokeh/Data/"
output_dir = "/Users/wel51x/Box Sync/MyBox/Code/DataCamp/bokeh/Output/"

mapper = CategoricalColorMapper(factors=['setosa',
                                         'virginica',
                                         'versicolor'],
                                palette=['green',
                                         'blue',
                                         'red'])

plot = figure(x_axis_label='Petal Length', y_axis_label='Sepal Length')
plot.circle(flowers['petal_length'], flowers['sepal_length'], size=10)

# Specify the name of the file & plot it

plot.circle('petal_length', 'sepal_length',
            size=8, source=flowers,
            legend = 'species',
            color={'field': 'species',
                   'transform': mapper})
plot.legend.location = "top_left"

output_file(output_dir+'lec4petals.html')
show(plot)
