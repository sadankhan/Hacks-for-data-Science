"""
General problems with the data:

1. Header on the data (Unnamed: 0 epoch mb bh bl nh)
2. Needs to be in numpy.ndarray format in order to use it in the machine learning model
3. Non-numeric data within the dataset
4. row numbers associated with each row that affect the model

To resolve these problems,use -> removeColumns(pandasArray, column)
"""
# Remove the column containing the target name since it doesn't contain numeric values.
# Also remove the column that contains the row number
# axis=1 means we are removing columns instead of rows.
# Function takes in a pandas array and column numbers and returns a numpy array without the stated columns


def removeColumns(pandasArray, *column):
    return pandasArray.drop(pandasArray.columns[[column]], axis=1).values
