# %% Imports and Data Loading
import pandas
import matplotlib.pyplot as plt


    
file_path = "avocado.csv"  # Replace with your CSV file path
data = pandas.read_csv(file_path)

# %% Print Columns
print("Columns:")
print(data.columns.tolist())
print("First row of the CSV:")
print(data.iloc[0])

# %% Process Data: Drop Unwanted Columns
#columns_to_drop = ["year"]  # Replace with the columns you want to delete
#data = data.drop(columns=columns_to_drop)

# Save the modified DataFrame back to the CSV file
#data.to_csv(file_path, index=False)  # Overwrite the original file
#print("Columns permanently deleted. Remaining columns:", data.columns.tolist())



#print("Checking for null values in the CSV:")
#print(data.isnull().sum())  # Prints the count of null values for each column

#print("\nRows with any null values:")
#print(data[data.isnull().any(axis=1)])  # Displays rows with at least one null value

# %% 


