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
def meanall(n):
  ans = np.mean(n)
  return ans

# Find the maximum value in each column.
def maxall(n):
  ans = np.max(n)
  return ans  

# Find the minimum value in each column.
def minall(n):
  ans = np.min(n)
  return ans

# Calculate the Standard Deviation (Std Dev) of each column.
def stdall(n):
  ans = np.std(n)
  return ans

# Calculate the Sum of the values in each column.
def sumall(n):
  ans = np.sum(n)
  return ans  
 
print("This is the analysis of the complete data set.")
print("The total number of rows in the data set is:" , np.count_nonzero(seplen))
print("\n")

print("Analysis of Sepal Length")
print("Average Sepal Length is:", meanall(seplen))
print("The Maximum Sepal Length is:" , maxall(seplen))
print("The Minimum Sepal Length is:" , minall(seplen))
print("The Standard Deviation of the Sepal Length is:" , stdall(seplen))
print("The Sum for all Sepal Lengths is:" , sumall(seplen))
print("\n")

print("Analysis of Sepal Width")
print("Average Sepal Width is:", meanall(sepwid))
print("The Maximum Sepal Width is:" , maxall(sepwid))
print("The Minimum Sepal Width is:" , minall(sepwid))
print("The Standard Deviation of the Sepal Width is:" , stdall(sepwid))
print("The Sum for all Sepal Widths is:" , sumall(sepwid))
print("\n")

print("Analysis of Petal Length")
print("Average Petal Length is:", meanall(petlen))
print("The Maximum Petal Length is:" , maxall(petlen))
print("The Minimum Petal Length is:" , minall(petlen))
print("The Standard Deviation of the Petal Length is:" , stdall(petlen))
print("The Sum for all Petal Lengths is:" , sumall(seplen))
print("\n")

print("Analysis of Petal Width")
print("Average Petal Width is:", meanall(petwid))
print("The Maximum Petal Width is:" , maxall(petwid))
print("The Minimum Petal Width is:" , minall(petwid))
print("The Standard Deviation of the Petal Width is:" , stdall(petwid))
print("The Sum for all Petal Widths is:" , sumall(petwid))
print("\n")

# Plotting Histogram for Sepal Lenght
plt.hist(seplen)
plt.xlabel('Sepal Length')
plt.ylabel('Count')
plt.title('Histogram of Sepal Length')
# plt.show()I 'commented' this command out, because it left my PC hanging for ages!
# According to my Google searches there is an issue with integrating event loops. See link.
# https://github.com/ipython/ipython/issues/9659

# Plotting Histogram for Sepal Width
plt.hist(sepwid)
plt.xlabel('Sepal Width')
plt.ylabel('Count')
plt.title('Histogram of Sepal Width')
# plt.show()

# Plotting Histogram for Petal Lenght
plt.hist(petlen)
plt.xlabel('Petal Length')
plt.ylabel('Count')
plt.title('Histogram of Petal Length')
# plt.show()

# Plotting Histogram for Petal Width
plt.hist(petwid)
plt.xlabel('Petal Width')
plt.ylabel('Count')
plt.title('Histogram of Petal Width')
# plt.show()


