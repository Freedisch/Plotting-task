import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import matplotlib
# Use the TkAgg backend (or any other backend that suits your system)
matplotlib.use('Agg')

# Load the dataset
data = pd.read_csv('fuel_econ.csv')

# Print the column names to verify
print(data.columns)

# Create a scatter plot: Fuel Efficiency vs Vehicle Type
plt.figure(figsize=(10, 6))
# 'comb' for combined fuel efficiency, 'VClass' for vehicle class
sns.scatterplot(x='comb', y='VClass', data=data)
plt.title('Fuel Efficiency vs Vehicle Type')
plt.xlabel('Fuel Efficiency (combined)')
plt.ylabel('Vehicle Class')
plt.savefig('fuel_efficiency_vs_vehicle_type.png')
plt.show()
