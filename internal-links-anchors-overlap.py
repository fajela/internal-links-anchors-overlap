# Import necessary libraries
import pandas as pd

# Specify the name of your input file
input_file_name = 'your_input_file.csv'  # Replace with your file name

# Read the csv file
df = pd.read_csv(input_file_name)

# Convert 'Anchor' column to lowercase
df['Anchor'] = df['Anchor'].str.lower()

# Find if there are different destination urls with the same anchor
grouped = df.groupby('Anchor')

# Create a new DataFrame to store the results
result = pd.DataFrame(columns=df.columns)

# Loop through each group
for name, group in grouped:
    if len(group['Destination'].unique()) > 1:
        result = pd.concat([result, group])

# Save the result to a new csv file
result.to_csv('result.csv', index=False)

print("The analysis is complete. The result is saved as 'result.csv'.")
