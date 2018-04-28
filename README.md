# Project2018
Programming and Scripting. End of Module Project 2018.
Wayne Reilly.

# Introduction.
This project is based on Ronald Fisher's Iris data set. The project contains research regarding the data set and some analysis of the data set using the Python programming language.

What is data analytics and why its important?

## Part 1.
This README is in two distinct sections. The first one is primarily concerning my approach, project plan and discussion on the data set including analysis conducted by others.

### Project Plan.
This is my overall project plan. This has seven stages and as with most projects it is likely that it will change as I work and will not necessarialy be carried out in the order listed. Throughout the project intermittment reviews of progress and tasks outstanding will be carried out.

* __Initial thoughts and Structure__ 
This is the begining for me, I spent some time thinking about how I would aproach the project and I quickly put a structure on the README.

* __Planning__ 
At this stage I identified the key stages for the project and some of the initial task that I would carry out as I worked towards completion. Old school pen and paper approach prior to typing up my work.

* __Break out of Tasks__
This is my list of smaller tasks and probaby the bulk of the work.
 * Research background information on the Data Set. And write this up.
 * Outline the Python Programming language and the libaries I have used. 
 * Research analysis conducted by others on the Data Set.
 * Download the Data Set and convert to CSV.
 * Consider ways to analyse the data.
 * Decide on what analysis I will conduct.
 * Start a Python file.
 * Read the data in to the file.
 * Write and test the scripts I want to run.
 * Write up my Approach. 
 * Write Methodology.
 * Consider professional applications for similar types of analysis.
 * References.

* __Start research of data set and analysis by others__

* __Work through each of the above tasks__

* __Write up Introduction and Conclusions__

* __Review and Edit__
  

### Methodology / Approach.
Discussion of the data set, its history. And it's importance in data analytics????
### Ronald Fisher and the Iris Flower Data Set.
Ronald Fisher (1890-1962) was a British Statistician and Geneticist. He is most famous for developing methods of 
multivariate analysis. He had a keen interest in genetics and applied his training in statistics to the Eugenics field including work on Charles Darmins theory on natural selection. [1]

He is credited with founding the Cambridge University Eugenics Society. In 1936, while Galton Professor of Eugenics at University College London he first introducted the Iris Flower Data Set in his paper "The use of multiple measurements in taxomony problems".[1]

The data set is sometimes called Andersons Iris Flower Data Set, because it was collected by Edgar Anderson to quantify the morphologic varations of Iris flower. The data set contains 50 samples from each of the three species of Iris (Iris Setosa, Iris Virginica and Iris Versicolor)[2]. The data set describes particular biological characteristics of various types of Iris flower. [3] For each sample the length and width of the Sepals and Petals were measured. 

The data set is widely used across the computer sciences including use in data minng and analytics.

### Python and the Python Libraries.
The programme I used to analyse the Iris Folwer data set is known as Python. Python is a programming language used 
for a variety of applcationts throughtout the IT industry and is described by the Python Foundation as "an interpreted, 
object oriented, high-level programming language"[4].

"Python is useful for accomplishing real-world task" [5] and can be found in several domains including 
Systems Programming, GUI's, Internet Scripting, Numeric and Scientific Programming, and Database Programming. [5]
The language is used by a multitude of IT industry leaders including, Google, Industrial Light and Magic, Jet Propulsion
Labs, and the ESRI. [5]

In analysing the data set I have used two of the modules for the Python programmng language standard library. Namely "Numpy" and  Python comes with a very extensive library of modules. Many of these modules provide standardised solutions to programming problems[6].

**NumPy** is a library of functions used for scientific computing.

**matplotlib.py** is a collection of command style functions that are used to generate visual representations of numercial data.

### Anaylsis by Others.
There appears to be ample amounts of analysis using the Iris Flower data set. After carrying out a couple of Google searches
I found three sets of analysis of note.

1. This analyst uses the data set to train and test a "Classifier" [7]. This work appears to have been carried out using the 
R programming language. I thought this was interesting as it showed how a well known and old (1936) data set is being used
in the development of machine learning. Something I'm sure Fisher wouldn't have imagined when he used the data set.

2. Statistical Analysis of the Iris Flower Data Set by Patrick Hoey[8]. The goal of this analyst was to create predictors
based on the analysis of the data set. He used Java as the programming language and 


## Part 2.
This section is about my work on the data set. What I did with the data, e.g sum, mean, median, etc.
My analysis of the data set is quite rudimentary. I have chosen to apply the following mathmatical operation;

### Sum.
I have summed each column of numbers. For example the sum of the Sepal Lengths is....

### Count.
Counted the total number of lines in the data set.

### Mean.
The mean is the most commonly used mathimatical measure of average (University of Leicester, 2018).

### Median.
The median refers to the middle value in the dataset, when the values are arranged in order of 
magnitude (University of Leicester, 2018).

### Mode.
The mode is the value that occurs with the greatest frequency in a dataest (University of Leicester, 2018)..

### Find the Highest number in each column.

### Find the lowest number in each column.

## Writting the Script.
When I started to write the script for this project I began with importing NumPy and matplotlib. I then used read the data
into an array that I could use with both modules. These are the line of code for that firs part;

### Imports the Python module numpy.<br/>
import numpy as np<br/>
### Imports the Python module pyplot.<br/>
import matplotlib.pyplot as plt <br/>
### Reads the data into array.<br/>
data = np.genfromtxt('data/iris.csv' , delimiter=',')<br/>

I created four variables for each column of the Iris Flower data set. Below is the variable Sepal Length and a brief
description of what each part of the code does.

seplen = data[:,0] # The first column of values is the Sepal Length.<br/>

seplen = This is the variable name. It represents the Sepal Length. When I need to use the data relating to the Sepal Length
I can use seplen.

data = This points the variable to the variable "data" I created earlier which generates a NumPy array with the data in the CSV file.

[:,0] = Creates a list and populates it with the data at index 0 i.e. the first column of numbers in the CSV file. This gives me all the numbers relating to the Sepal Length.

After creating this variable I can use it to write a simple piece of code to get at the data for the Sepal Length. For example if I wanted to display all the values for the Sepal Length all I need to do is type in the python command print(seplen) and I will get the following output;

![screenshot](https://github.com/Wayne742/Project2018/blob/master/Screen_Shot_seplen_Print.png)

I used the same process to create variables for Sepal Width, Petal Length and Petal Width.

As I continued to write my code I began with very basic and cumbersome code lines. Shown here;<br/>
meanseplen = np.mean(seplen) # Mean of the Sepal Length.<br?>  
meansepwid = np.mean(sepwid) # Mean of the Sepal Width.<br/>
meanpetlen = np.mean(petlen) # Mean of the Petal Length.<br/>
meanpetwid = np.mean(petwid) # Mean of the Petal Width.<br/>

print("Average Sepal Length is:", meanseplen)<br/>
print("Average Sepal Width is:", meansepwid)<br/>
print("Average Petal Length is:", meanpetlen)<br/>
print("Average Petal Width is:", meanpetwid)<br/>

It eventually dawned on me to use a Function, and after some online searches and a review of the course video on writing functions, I came up with this<br/>
This is the function to get the Mean of all the numbers in any column. By calling the function in the print statement below and replacing the n in the brackets with any of the four variables I created I can get the mean for the column.<br/> 
def meanall(n):<br/>
  ans = np.mean(n)<br/>
  return ans<br/>

print("Average Sepal Length is:", meanall(seplen))<br/>
print("Average Sepal Width is:", meanall(sepwid))<br/>
print("Average Petal Length is:", meanall(petlen))<br/>
print("Average Petal Width is:", meanall(petwid))<br/>  

Here is a screenshot of the output for the meanall function when the (n) is repalced with the variable seplen.<br/>
![meanseplen](https://github.com/Wayne742/Project2018/blob/master/screenshot_mean_seplen.png)


### Histograms.
For each columns in the Iris Flower data set I have included a short script to generate a Histogram. A Histogram is a visual representation of the distribution of numercial data. It is similar in apperance to a bar chart and was first intorduced by the mathematician Karl Pearson. Histrograms give a rough sense of the density of the underlying distribution of the data.[10] 

In order to generate the Histograms I used the python library "matplotlib mentioned in Part 1. An example of the script used 
to generate the Histograms is shown below. The script shown generates a Histogram of the Sepal Lengths and uses the variable
seplen to call out the relevant data from the data set. I repeated these lines of script for each column, Sepal Width, Petal Length and Petal Width. I updated the script with the required variable and changed the chart title and the axis label. 

### Plotting the Histogram for Sepal Lenght.
plt.hist(seplen) # The function to generate the Histogram.<br/>
plt.xlabel('Sepal Length') # Labels the X axis of the Histogram.<br/>
plt.ylabel('Count') # Labels the Y axis of the Histogram.<br/>
plt.title('Histogram of Sepal Length') # Inserts a title.<br/>
plt.show() # This line of code tells python to display the generated image.<br/>

![Histogram](https://github.com/Wayne742/Project2018/blob/master/Seplen_Hist.png)

![Histogram](https://github.com/Wayne742/Project2018/blob/master/Sepwid_Hist.png)

![Histogram](https://github.com/Wayne742/Project2018/blob/master/Petlen_Hist.png)

![Histogram](https://github.com/Wayne742/Project2018/blob/master/Petwid_Hist.png)

### Plotting a Scatter Plot.
I also included a Scatter Plot of the data set. This caused me some difficulty. While the lines of code for the script
were easy to find on the 'net' and it was fairly easy to understand what each line in hte script actully did my Scatter plot
did not generate as I wanted. 

Primarily the problem I had was that I wanted to plot each column and display each catrgory in a different colour. For example, Sepal Length would be Green and Sepal Width would be Red. However when I tried to run the script it 'crashed'.

To overcome this I tried to build the plot up one object at a time. I started with just the Sepal Lenght in Red. And ran the 
script, it worked perfectly. Then I added the Sepal Width, in Blue. Again the script ran fine. I continued to add the Petal
Length, in Green. Again the script ran fine. Lastly I added the Petal Width in Yellow. This crashed! I don't know why but
can only speculate that I'm trying to fit too much into the plot. When I take out one colour it seem to run fine although I 
am concerned that my Scatter plot is not as densely populated as some of the others I've seen online. 

![Scatter](https://github.com/Wayne742/Project2018/blob/master/Scatter.png)

## Conclusions.
What are the real world applications for similar types of analysis? 
How could I apply this type of analysis to my work in procurement?

## References.

[1] Encyclopaedia Briannica. Sir Ronald Alymer Fisher.
https://www.britannica.com/biography/Ronald-Aylmer-Fisher

[2] Wikipedia. Iris Flower Data Set.
https://en.wikipedia.org/wiki/Iris_flower_data_set

[3] Techopedia. Iris Flower Data Set.
https://www.techopedia.com/definition/32880/iris-flower-data-set

[4] Python Software Foundation. What is Python. Executive Summary.
https://www.python.org/doc/essays/blurb/

[5] Learning Python. Mark Lutz.
Pages (9 - 10) (11 - 14).

[6] Python Software Foundation. The Python Standard Library. 
https://docs.python.org/2/library/

[7] Data Analysis - Iris dataset[sic] 
https://www.kaggle.com/sridharcr/data-analysis-iris-dataset

[8] Statistical Analysis of the Iris Flower Data Set. Patrick S Hoey.
http://patrickhoey.com/downloads/Computer_Science/03_Patrick_Hoey_Data_Visualization_Dataset_paper.pdf

The Shape of data. 
https://shapeofdata.wordpress.com/2013/10/01/case-study-1-iris/

https://www.kaggle.com/mathewnik90/machinelearning-helloworld-with-iris-full-analysis
https://wr.informatik.uni-hamburg.de/_media/teaching/wintersemester_2016_2017/bd-uebung-02.pdf
https://www2.le.ac.uk/offices/ld/resources/numerical-data/averages

[10] Wikipedia. Histograms. 
https://en.wikipedia.org/wiki/Histogram

plotting Histograms
https://pythonspot.com/matplotlib-histogram/

plotting scatter charts 
https://pythonspot.com/matplotlib-scatterplot/

Writing functions.
https://nbviewer.jupyter.org/github/ianmcloughlin/python-fundamentals-notes/blob/master/functions-modules.ipynb#

