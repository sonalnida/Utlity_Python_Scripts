import collections
from collections import OrderedDict

# Initialize dictionaries to store data
d = {}  # This dictionary will hold gene expression values grouped by keys
same_key_dic = {}  # Placeholder for future use, currently unused

# Open the input file containing gene expression data
with open('yng_res_edit.txt', 'r') as f1:
    for line1 in f1:
        line1 = line1.rstrip()  # Remove trailing whitespace
        exp = line1.split("\t")  # Split each line into key-value pairs based on tab delimiter
        f_key = exp[1]  # Extract the key (e.g., gene identifier)
        f_value = exp[0]  # Extract the value (e.g., expression level)
        
        # Check if the key already exists in the dictionary
        if f_key in d.keys():
            geneExprVal = float(exp[0])  # Convert the expression value to a float
            d[f_key][geneExprVal] = 0  # Add the expression value as a nested key
        else:
            vals = {}  # Initialize a new dictionary to store expression values
            geneExprVal = float(exp[0])  # Convert the expression value to a float
            vals[geneExprVal] = 0  # Add the expression value to the nested dictionary
            d[f_key] = vals  # Assign the nested dictionary to the main dictionary under the key

# Initialize a dictionary to store ranked data
rankedDict = {}

# Rank gene expression values for each key
for keyIdentity in d:
    rankDict = sorted(d[keyIdentity].items(), reverse=True)  # Sort expression values in descending order
    rankedDict[keyIdentity] = rankDict  # Store the sorted values in the ranked dictionary

# Assign ranks and print the ranked data
for rankedKey in rankedDict:
    rank = 1000  # Start rank at 1000
    # Calculate step size based on the number of values for the key
    stepSize = int(1000 / len(rankedDict[rankedKey])) if len(rankedDict[rankedKey]) > 0 else 0
    for rankValue in rankedDict[rankedKey]:
        # Print the key, expression value, and assigned rank
        print(f"{rankedKey} {rankValue[0]} {rank}")
        rank -= stepSize  # Decrease the rank by the step size for the next value
