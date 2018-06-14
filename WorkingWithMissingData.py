"""
Steps for working with missing data:

1. identify missing data
2. deal with missing data
3. correct data format
"""
import numpy as np

#1. Identify and handle missing values
#-----------------------------------------#
##$Convert "?" to NaN(Not a Number), which is Python's default missing value marker

# replace "?" to NaN
df.replace("?", np.nan, inplace = True)
df.head(5)

##$Evaluating for Missing Data
"""
The missing values are converted to Python's default. We use Python's built-in functions to identify these missing values. There are two methods to detect missing data:

1. .isnull()
2. .notnull()
The output is a boolean value indicating whether the passed in argument value are in fact missing data.
"""
missing_data = df.isnull()
missing_data.head(5) #Returns True False in table

##Count missing values in each column
for column in missing_data.columns.values.tolist():
    print(column)
    print (missing_data[column].value_counts())
    print("") 

##$Deal with missing data
avg_1 = df["column"].astype("float").mean(axis = 0)
df["column"].replace(np.nan, avg_1, inplace = True)
