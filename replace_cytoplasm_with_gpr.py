# Initialize empty lists for storing data (though these are unused in the code below)
gpr = list()
loc = list()

# Open the input file in read mode using a context manager for better resource management
with open('C:\\Users\\sd01165\\Desktop\\metabolic_model\\python_scripts\\young_model.txt', 'r') as f:
    for line in f:
        # Split the line into a list using tab as the delimiter
        splited_line = line.split('\t')
        
        # Extract the 4th column (index 3) as the GPR value
        gpr = splited_line[3]
        
        # Split the GPR value on underscores and take the first part
        org = gpr.split('_')
        exact = org[0]
        
        # Replace 'Cytoplasm' in the line with the extracted value
        replaced_line = line.replace('Cytoplasm', exact)
        
        # Print the modified line
        print(replaced_line)
