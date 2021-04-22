#import libraries and practice data set
import matplotlib.pyplot as plt
from pydataset import data

# Import the mpg dataframe from the pydataset
mpg = data('mpg')

# Rename columns for better readability
mpg = mpg.rename(columns = {'cty':'city', 'hwy':'highway', 'cyl':'cylinder', 'drv':'drive'})

# Create average mileage and mileage difference columns
mpg['average_mileage'] = mpg[['highway','city']].mean(axis = 1)
mpg['mileage_difference'] = mpg['highway'].sub(mpg['city'], axis = 0)

# set a figure size large enough to look at data sets
plt.figure(figsize = (15,10))

# all the average mileages for each car grouped by automaker
yaudi= mpg[mpg['manufacturer'] == 'audi'].average_mileage.array
yhonda = mpg[mpg['manufacturer'] == 'honda'].average_mileage.array
yvolks = mpg[mpg['manufacturer'] == 'volkswagen'].average_mileage.array
yhyun = mpg[mpg['manufacturer'] == 'hyundai'].average_mileage.array
ysub = mpg[mpg['manufacturer'] == 'subaru'].average_mileage.array
ytoy = mpg[mpg['manufacturer'] == 'toyota'].average_mileage.array
ypont = mpg[mpg['manufacturer'] == 'pontiac'].average_mileage.array
yniss = mpg[mpg['manufacturer'] == 'nissan'].average_mileage.array
ychev = mpg[mpg['manufacturer'] == 'chevrolet'].average_mileage.array
yford = mpg[mpg['manufacturer'] == 'ford'].average_mileage.array
ymerc = mpg[mpg['manufacturer'] == 'mercury'].average_mileage.array
yjeep = mpg[mpg['manufacturer'] == 'jeep'].average_mileage.array
ydodg = mpg[mpg['manufacturer'] == 'dodge'].average_mileage.array
ylinc = mpg[mpg['manufacturer'] == 'lincoln'].average_mileage.array
yland = mpg[mpg['manufacturer'] == 'land rover'].average_mileage.array

# same as above except for x values, using displacement as the variable
xaudi= mpg[mpg['manufacturer'] == 'audi'].displ.array
xhonda = mpg[mpg['manufacturer'] == 'honda'].displ.array
xvolks = mpg[mpg['manufacturer'] == 'volkswagen'].displ.array
xhyun = mpg[mpg['manufacturer'] == 'hyundai'].displ.array
xsub = mpg[mpg['manufacturer'] == 'subaru'].displ.array
xtoy = mpg[mpg['manufacturer'] == 'toyota'].displ.array
xpont = mpg[mpg['manufacturer'] == 'pontiac'].displ.array
xniss = mpg[mpg['manufacturer'] == 'nissan'].displ.array
xchev = mpg[mpg['manufacturer'] == 'chevrolet'].displ.array
xford = mpg[mpg['manufacturer'] == 'ford'].displ.array
xmerc = mpg[mpg['manufacturer'] == 'mercury'].displ.array
xjeep = mpg[mpg['manufacturer'] == 'jeep'].displ.array
xdodg = mpg[mpg['manufacturer'] == 'dodge'].displ.array
xlinc = mpg[mpg['manufacturer'] == 'lincoln'].displ.array
xland = mpg[mpg['manufacturer'] == 'land rover'].displ.array

# plot xy values for each manufacturer 
plt.scatter(xaudi, yaudi, label = 'Audi', marker = '.', linewidths = 5)
plt.scatter(xhonda, yhonda, label = 'Honda', marker = '.', linewidths = 5)
plt.scatter(xvolks, yvolks, label = 'Volkswagen', marker = '.', linewidths = 5)
plt.scatter(xhyun, yhyun, label = 'Hyundai', marker = '.', linewidths = 5)
plt.scatter(xsub, ysub, label = 'Subaru', marker = '.', linewidths = 5)
plt.scatter(xtoy, ytoy, label = 'Toyota', marker = '.', linewidths = 5)
plt.scatter(xpont, ypont, label = 'Pontiac', marker = '.', linewidths = 5)
plt.scatter(xniss, yniss, label = 'Nissan', marker = '.', linewidths = 5)
plt.scatter(xchev, ychev, label = 'Chevy', marker = '^')
plt.scatter(xford, yford, label = 'Ford', marker = '^')
plt.scatter(xmerc, ymerc, label = 'Mercedes', marker = '^')
plt.scatter(xjeep, yjeep, label = 'Jeep', marker = '^')
plt.scatter(xdodg, ydodg, label = 'Dodge', marker = '^')
plt.scatter(xlinc, ylinc, label = 'Lincoln', marker = '^')
plt.scatter(xland, yland, label = 'Land Rover', marker = '^')

#change xy tick font size
plt.xticks(fontsize = 15)
plt.yticks(fontsize = 15)

# add title and axis labels, changed size, font, and padding for readability
plt.title('Engine Displacement and the Effect on MPG', fontsize = 25, fontname = 'DIN Alternate', pad = 20)
plt.xlabel('Engine Displacement (L)', fontsize = 20, fontname = 'DIN Alternate', labelpad = 15)
plt.ylabel('Miles per Gallon', fontsize = 20, fontname = 'DIN Alternate', labelpad = 15)

#add a legend
plt.legend(fontsize = 'large')

#show it 
plt.show()