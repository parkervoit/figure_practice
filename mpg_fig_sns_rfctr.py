# import all my libraries to use with importing and cleaning data
from pydataset import data
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

# Load the dataset from pydataset
mpg_df = data('mpg')

# Rename the columns into something more readable
mpg_df = mpg_df.rename(columns = {'cty':'city', 'hwy':'highway', 'cyl':'cylinder', 'drv':'drive'})

# Create two new columns calculating the average mileage and mileage difference
mpg_df['average_mileage'] = mpg_df[['highway','city']].mean(axis = 1)
mpg_df['mileage_difference'] = mpg_df['highway'].sub(mpg_df['city'], axis = 0)

#Create figure and style for readability and formatting
plt.figure(figsize = (10,10))
sns.set_style('whitegrid')

# Using seaborn, displacement and average mileage columns were graphed from the mpg_df dataframe
# Hue by manufacturer to compare diffference between manufacturers, and used a paired palette can be overlapping 
sns.relplot(data = mpg_df, x = 'displ',y = 'average_mileage', hue = 'manufacturer', palette = 'Paired')

# since the style has gridlines, I used a limit to make the grids seem more equal 
plt.xlim(1,7.5)

#add labels and title, resize for readability
plt.title('Relationship Between MPG and Displacement', fontsize = 13)
plt.xticks(fontsize = 10)
plt.yticks(fontsize = 10)
plt.ylabel('Miles per Gallon', fontsize =10)
plt.xlabel('Engine Displacement (L)', fontsize = 10)