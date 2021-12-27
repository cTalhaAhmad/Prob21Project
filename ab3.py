import math
import statistics
import scipy.stats
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from matplotlib import colors
from matplotlib.ticker import PercentFormatter
import csv 
from collections import Counter

print("\n\n\n")

# Using All the Columns out of Read Data.

dataset1 = pd.read_csv (r'D:\Study\FAST CFD\Semester 5\MT2005-Probability and Statistics\Prob Project\dataset\Rainfall_19012016.csv')
dataset2 = pd.read_csv (r'D:\Study\FAST CFD\Semester 5\MT2005-Probability and Statistics\Prob Project\dataset\Temperature_19012016.csv')

print (dataset1)
print("\n")
print (dataset2)
print("\n")

# Using Desired Selected Columns out of Read Data.

dataset3 = pd.read_csv (r'D:\Study\FAST CFD\Semester 5\MT2005-Probability and Statistics\Prob Project\dataset\Rainfall_19012016.csv')
dataset4 = pd.read_csv (r'D:\Study\FAST CFD\Semester 5\MT2005-Probability and Statistics\Prob Project\dataset\Temperature_19012016.csv')

modifieddataset3 = pd.DataFrame(dataset3, columns= ['Rainfall (MM)','Year'])
modifieddataset4 = pd.DataFrame(dataset4, columns= ['Temperature (Celsius)','Year'])

print (modifieddataset3)
print("\n")
print (modifieddataset4)
print("\n")

# Merging both datasets into 1 with same Month and Year
dataset5 = pd.merge(dataset1, dataset2, on=["Month","Year"])
dataset5 = dataset5[["Month", "Year",'Temperature (Celsius)','Rainfall (MM)']]
print (dataset5)
print("\n")

# Taking Mean of Monthly Temprature and Rainfall from 1901-2016
tempMean=dataset5['Temperature (Celsius)'].mean()
print ("Average Monthly Temprature (Celsius) from 1901-2016 is:",tempMean, "Celsius")
print("\n")
rainMean=dataset5['Rainfall (MM)'].mean()
print ("Average Monthly Rainfall (MM) from 1901-2016 is:",rainMean, "MM")
print("\n")

# Taking Median of Monthly Temprature and Rainfall from 1901-2016
tempMedian=dataset5['Temperature (Celsius)'].median()
print ("Median Monthly Temprature (Celsius) from 1901-2016 is:",tempMedian, "Celsius")
print("\n")
rainMedian=dataset5['Rainfall (MM)'].median()
print ("Median Monthly Rainfall (MM) from 1901-2016 is:",rainMedian, "MM")
print("\n")

# Descriptive Statistics of Dataset of Temprature and Rainfall from 1901-2016
describeData=dataset5[['Temperature (Celsius)','Rainfall (MM)']].describe().round()
print(describeData)
print("\n")

# Descriptive Statistics of Dataset of Temprature and Rainfall from 1901-2016
describeData=dataset5[['Temperature (Celsius)','Rainfall (MM)']].describe().round()
print(describeData)
print("\n")

# Taking Minimum of Monthly Temprature and Rainfall from 1901-2016
tempMin=dataset5['Temperature (Celsius)'].min()
print ("Minimum Monthly Temprature (Celsius) from 1901-2016 is:",tempMin, "Celsius")
print("\n")
rainMin=dataset5['Rainfall (MM)'].min()
print ("Minimum Monthly Rainfall (MM) from 1901-2016 is:",rainMin, "MM")
print("\n")

# Taking Maximum of Monthly Temprature and Rainfall from 1901-2016
tempMax=dataset5['Temperature (Celsius)'].max()
print ("Maximum Monthly Temprature (Celsius) from 1901-2016 is:",tempMax, "Celsius")
print("\n")
rainMax=dataset5['Rainfall (MM)'].max()
print ("Maximum Monthly Rainfall (MM) from 1901-2016 is:",rainMax, "MM")
print("\n")

#dataset5.mean().plot(kind='bar');