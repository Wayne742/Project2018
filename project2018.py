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
print("The Sum for all Sepal Lengths is:" , sumseplen)
print("")

print("Analysis of Sepal Width")
print("Average Sepal Width is:", meansepwid)
print("The Maximum Sepal Width is:" , maxsepwid)
print("The Minimum Sepal Width is:" , minsepwid)
print("The Standard Deviation of the Sepal Width is:" , stdsepwid)
print("The Sum for all Sepal Widths is:" , sumsepwid)
print("")

print("Analysis of Petal Length")
print("Average Petal Length is:", meanpetlen)
print("The Maximum Petal Length is:" , maxpetlen)
print("The Minimum Petal Length is:" , minpetlen)
print("The Standard Deviation of the Petal Length is:" , stdpetlen)
print("The Sum for all Petal Lengths is:" , sumseplen)
print("")

print("Analysis of Petal Width")
print("Average Petal Width is:", meanpetwid)
print("The Maximum Petal Width is:" , maxpetwid)
print("The Minimum Petal Width is:" , minpetwid)
print("The Standard Deviation of the Petal Width is:" , stdpetwid)
print("The Sum for all Petal Widths is:" , sumpetwid)
print("")




