# Import figure from bokeh.plotting
from bokeh.plotting import figure
from datetime import *

# Import output_file and show from bokeh.io
from bokeh.io import output_file, show

data_dir = "/Users/wel51x/Box Sync/MyBox/Code/DataCamp/bokeh/Data/"
output_dir = "/Users/wel51x/Box Sync/MyBox/Code/DataCamp/bokeh/Output/"

price = [31.68, 29.66, 31.12, 30.56, 29.87, 29.66, 26.66, 29.72, 30.57, 29.5, 27.78, 29.29]

date = [ datetime(2000, 3, 1, 0, 0), datetime(2000, 3, 2, 0, 0), datetime(2000, 3, 3, 0, 0),
         datetime(2000, 3, 6, 0, 0), datetime(2000, 3, 7, 0, 0), datetime(2000, 3, 8, 0, 0),
         datetime(2000, 3, 9, 0, 0), datetime(2000, 3, 10, 0, 0), datetime(2000, 3, 13, 0, 0),
         datetime(2000, 3, 14, 0, 0), datetime(2000, 3, 15, 0, 0), datetime(2000, 3, 16, 0, 0)]

# Create the figure: p
p = figure(x_axis_type="datetime", x_axis_label='Date', y_axis_label='US Dollars')

# Add a circle glyph to the figure p
p.line(date, price)

# With date on the x-axis and price on the y-axis, add a white circle glyph of size 4
p.circle(date, price, fill_color="white", size=4)

# Call the output_file() function and specify the name of the file
output_file(output_dir+'ex2line.html')

# Display the plot
show(p)

#2 - 4 corners
'''
az_lons = [float(line.rstrip(',\n')) for line in open("az_lons")]
az_lats = [float(line.rstrip(',\n')) for line in open("az_lats")]
co_lons = [float(line.rstrip(',\n')) for line in open("co_lons")]
co_lats = [float(line.rstrip(',\n')) for line in open("co_lats")]
nm_lons = [float(line.rstrip(',\n')) for line in open("nm_lons")]
nm_lats = [float(line.rstrip(',\n')) for line in open("nm_lats")]
ut_lons = [float(line.rstrip(',\n')) for line in open("ut_lons")]
ut_lats = [float(line.rstrip(',\n')) for line in open("ut_lats")]
'''
filenames = ["az_lons", "co_lons", "nm_lons", "ut_lons", "az_lats", "co_lats", "nm_lats", "ut_lats"]
files = [open(data_dir+file) for file in filenames]
lats_and_lons = [[float(line.rstrip(',\n')) for line in file] for file in files]

# Create the figure: p
p = figure()

# Create a list of az_lons, co_lons, nm_lons and ut_lons: x
#x = [az_lons, co_lons, nm_lons, ut_lons]

# Create a list of az_lats, co_lats, nm_lats and ut_lats: y
#y = [az_lats, co_lats, nm_lats, ut_lats]

# Add patches to figure p with line_color=white for x and y
middle = int(len(lats_and_lons)/2)
p.patches(lats_and_lons[0:middle],
          lats_and_lons[middle:len(lats_and_lons)],
          line_color='white')

# Specify the name of the output file and show the result
output_file(output_dir+'ex2four_corners.html')
show(p)
