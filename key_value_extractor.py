# Initialize a dictionary to store results
d = {}

# Open the input file for reading
with open('young_results.txt', 'r') as f:
    for line in f:
        # Split each line into columns by tab character
        id1 = line.strip().split('\t')
        
        # Ensure the line has at least 4 columns to avoid errors
        if len(id1) > 3:
            key = id1[0]  # First column as the key
            value = id1[3]  # Fourth column as the value
            
            # Use setdefault to add values to the dictionary
            d.setdefault(key, []).append(value)

# Print the dictionary in a clean format
for key, values in d.items():
    print(f"{key}: {values}")
