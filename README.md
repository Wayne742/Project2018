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

In analysing the data set I have used two of the modules for the Python programmng language standard library. Python comes
with a very extensive library of modules. Many of these modules provide standardised solutions to programming problems[6].

### Anaylsis by Others.
There appears to be ample amounts of analysis using the Iris Flower data set. After carrying out a couple of Google searches
I found three sets of analysis of note.

1. This analyst uses the data set to train and test a "Classifier" [7]. This work appears to have been carried out using the 
R programming language. I thought this was interesting as it showed how a well known and old (1936) data set is being used
in the development of machine learning. Something I'm sure Fisher wouldn't have imagined when he used the data set.

2. Statistical Analysis of the Iris Flower Data Set by Patrick Hoey[8]. The goal of this analyst was to create predictors
based on the analysis of the data set. He used Java as the programming language and 


## Part 2.
My work on the data set. What I did with the data, e.g sum, mean, median, etc.
My analysis of the data set is quite rudimentary. I have chosen to apply the following mathmatical operation;

### Sum.
I have summed each column of numbers. For example the sum of the Sepal Lengths is....

### Count.
Counted the total number of lines in hte data set.

### Mean.
The mean is the most commonly used mathimatical measure of average (University of Leicester, 2018).

### Median.
The median refers to the middle value in the dataset, when the values are arranged in order of 
magnitude (University of Leicester, 2018).

### Mode.
The mode is the value that occurs with the greatest frequency in a dataest (University of Leicester, 2018)..

### Find the Highest number in each column.

### Find the lowest number in each column.

I went from this:
meanseplen = np.mean(seplen) # Mean of the Sepal Length.
meansepwid = np.mean(sepwid) # Mean of the Sepal Width.
meanpetlen = np.mean(petlen) # Mean of the Petal Length.
meanpetwid = np.mean(petwid) # Mean of the Petal Width.

print("Average Sepal Length is:", meanseplen)
print("Average Sepal Width is:", meansepwid)
print("Average Petal Length is:", meanpetlen)
print("Average Petal Width is:", meanpetwid)

To this:
def meanall(n):
  ans = np.mean(n)
  return ans

print("Average Sepal Length is:", meanall(seplen))
print("Average Sepal Width is:", meanall(sepwid))
print("Average Petal Length is:", meanall(petlen))
print("Average Petal Width is:", meanall(petwid))  

### Histograms.

![Histogram](https://github.com/Wayne742/Project2018/blob/master/Seplen_Hist.png)


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

plotting Histograms
https://pythonspot.com/matplotlib-histogram/

plotting scatter charts 
https://pythonspot.com/matplotlib-scatterplot/

https://nbviewer.jupyter.org/github/ianmcloughlin/python-fundamentals-notes/blob/master/functions-modules.ipynb#

