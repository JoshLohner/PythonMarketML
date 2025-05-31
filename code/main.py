# %% Imports and Data Loading
import pandas
import matplotlib.pyplot as plt


    
file_path = "data/avocado.csv"  # Replace with your CSV file path
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

data['Date'] = pandas.to_datetime(data['Date'])
data = data.sort_values(by='Date')

data_2015 = data[data['Date'].dt.year == 2015]

# Plot the average price over time
plt.figure(figsize=(10, 6))
plt.plot(data_2015['Date'], data_2015['AveragePrice'], label='Average Price (2015)', color='green')
plt.title('Average Price Over Time (2015)')
plt.xlabel('Date')
plt.ylabel('Average Price')
plt.legend()
plt.grid()
plt.show()

# %%
