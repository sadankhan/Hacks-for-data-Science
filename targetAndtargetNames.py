"""
Since we cannot use .target and .target_names, I have created a function that will do this for us.

targetAndtargetNames(numpyArray, targetColumnIndex)

This function produces two outputs, and requires two inputs.

1st Input: A numpy array. The numpy array you will use is my_data.values (or my_data.as_matrix())
Note: DO NOT USE new_data here. We need the original .csv data file without the headers
2nd Input: An integer value that represents the target column . 
(Look at the data again and find which column contains the non-numeric values. This is the target column)
Note: Remember that Python is zero-indexed, therefore the first column would be 0.
1st Output: The response vector (target)
2nd Output: The target names (target_names)
"""
def targetAndtargetNames(numpyArray, targetColumnIndex):
    target_dict = dict()
    target = list()
    target_names = list()
    count = -1
    for i in range(len(my_data.values)):
        if my_data.values[i][targetColumnIndex] not in target_dict:
            count += 1
            target_dict[my_data.values[i][targetColumnIndex]] = count
        target.append(target_dict[my_data.values[i][targetColumnIndex]])
    # Since a dictionary is not ordered, we need to order it and output it to a list so the
    # target names will match the target.
    for targetName in sorted(target_dict, key=target_dict.get):
        target_names.append(targetName)
    return np.asarray(target), target_names
