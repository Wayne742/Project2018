# Wayne Reilly 16/04/2018.
# Programming and Scritping, End of Module Project.

# Imports the Python module numpy.
import numpy as np
# Imports the Python module 
import matplotlib.pyplot as plt 
# Reads the data into array.
data = np.genfromtxt('data/iris.csv' , delimiter=',')

# Assigning the column data to variables. 
seplen = data[:,0] # The first column of values is the Sepal Length.
sepwid = data[:,1] # The second column of values is the Sepal Width.
petlen = data[:,2] # The third column of values is the Petal Length.
petwid = data[:,3] # The fourth column of values is the Petal Width.

# Calculate the average/mean of the values in each column.
meanseplen = np.mean(seplen) # Mean of the Sepal Length.
meansepwid = np.mean(sepwid) # Mean of the Sepal Width.
meanpetlen = np.mean(petlen) # Mean of the Petal Length.
meanpetwid = np.mean(petwid) # Mean of the Petal Width.

# Find the maximum value in each column.
maxseplen = np.max(seplen) # Maximum of the Sepal Length.
maxsepwid = np.max(sepwid) # Maximum of the Sepal Width.
maxpetlen = np.max(petlen) # Maximum of the Petal Length.
maxpetwid = np.max(petwid) # Maximum of the Petal Width.

# Find the minimum value in each column.
minseplen = np.min(seplen) # Minimum of the Sepal Length.
minsepwid = np.min(sepwid) # Minimum of the Sepal Width.
minpetlen = np.min(petlen) # Minimum of the Petal Length.
minpetwid = np.min(petwid) # Minimum of the Petal Width.

# Calculate the Standard Deviation (Std Dev) of each column.
stdseplen = np.std(seplen) # Std Dev of Sepal Length.
stdsepwid = np.std(sepwid) # Std Dev of Sepal Width.
stdpetlen = np.std(petlen) # Std Dev of Petal Length.
stdpetwid = np.std(petwid) # Std Dev of Petal Width.

print("This is the analysis of the complete data set.")
print("The total number of rows in the data set is:" , np.count_nonzero(seplen))
print("")

print("Analysis of Sepal Length")
print("Average Sepal Length is:", meanseplen)
print("The Maximum Sepal Length is:" , maxseplen)
print("The Minimum Sepal Length is:" , minseplen)
print("The Standard Deviation of the Sepal Length is:" , stdpetlen)
print("")

print("Average Sepal Width is:", meansepwid)
print("Average Petal Length is:", meanpetlen)
print("Average Petal Width is:", meanpetwid)
print("")
print("The minimum Sepal Length is:" , minseplen)
print("The maximum Sepal Length is:" , maxseplen)



