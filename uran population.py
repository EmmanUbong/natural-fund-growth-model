# -*- coding: utf-8 -*-
"""
Created on Tue Nov  7 16:47:34 2023

@author: EMMANUEL
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Load the data from the CSV file
file_path = 'pop1.csv'
data = pd.read_csv(file_path)

# Display the first few rows of the data to understand its structure
print(data.head())

# Function to calculate exponential growth
def exponential_growth(initial_population, growth_rate, time):
    return initial_population * np.exp(growth_rate * time)

# Iterate over rows and plot population growth for each state
for index, row in data.iterrows():
    state = row['STATE']
    initial_population = float(row['POPULATION (2006)'])

    # Convert 'ANNUAL % GR' to numeric if it's not already
    try:
        growth_rate_str = str(row['ANNUAL % GR']).replace('%', '')
        growth_rate = float(growth_rate_str) / 100
    except (ValueError, AttributeError):
        print(f"Skipping {state} due to invalid growth rate")
        continue

    time_values =pd.to_numeric( np.arange(0, 10, 1))  # Assuming a 10-year projection

    # Calculate population values over time
    population_values = exponential_growth(initial_population, growth_rate, time_values)

    # Plot the population growth for each state
    # plt.plot(time_values, population_values, label=state)
    
    
#     plt.figure(figsize=(10, 5))

#    # Line Chart
#     plt.subplot(1, 3, 1)
#     plt.plot(time_values, population_values)
#     plt.title(f"Population Growth Over Time - {state}")
#     plt.xlabel("Years")
#     plt.ylabel("Population")

#    # Bar Chart
#     plt.subplot(1, 3, 2)
#     plt.bar(['Initial Population', 'Final Population'], [initial_population, population_values[-1]])
#     plt.title(f"Initial and Final Population - {state}")

#    # Pie Chart
#     plt.subplot(1, 3, 3)
#     plt.pie([initial_population, population_values[-1]], labels=['Initial Population', 'Final Population'], autopct='%1.1f%%')
#     plt.title(f"Population Distribution - {state}")

#     plt.tight_layout()
#     plt.show()


# # Plot settings
# plt.xlabel("Years")
# plt.ylabel("Population")
# plt.title("Population Growth Over Time for States")
# plt.legend()
# plt.grid(True)
# plt.show()



def edA():
    # Basic Statistics
    print("\nBasic Statistics:")
    print(data.describe())
    
    # Data types and missing values
    print("\nData Types and Missing Values:")
    print(data.info())
    
    # Correlation Matrix
    print("\nCorrelation Matrix:")
    correlation_matrix = data.corr()
    sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', linewidths=0.5)
    plt.show()
    
    # Pairplot for selected columns
    print("\nPairplot:")
    sns.pairplot(data[['POPULATION (2006)', 'ANNUAL % GR']])
    plt.show()
    
    # Histograms
    print("\nHistograms:")
    data.hist(bins=20, figsize=(12, 8))
    plt.show()
    
    # Boxplots
    print("\nBoxplots:")
    sns.boxplot(x='ANNUAL % GR', data=data)
    plt.show()


edA()     
# # Plot settings
# plt.xlabel("Years")
# plt.ylabel("Population")
# plt.title("Population Growth Over Time for Nigerian States")
# plt.legend()
# plt.grid(True)
# plt.show()


# def exponential_growth(initial_population, growth_rate, time):
#     return initial_population * np.exp(growth_rate * time)

# # Define parameters
# initial_population = 1000
# growth_rate = 0.02  # 2% growth rate per unit of time

# # Create an array of time values
# time_values = np.arange(0, 20, 1)

# # Calculate population values over time
# population_values = exponential_growth(initial_population, growth_rate, time_values)

# # Plot the population growth
# plt.plot(time_values, population_values)
# plt.xlabel("Time")
# plt.ylabel("Population")
# plt.title("Population Growth Model")
# plt.grid(True)
# plt.show()

