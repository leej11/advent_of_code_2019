import math
import pandas as pd

# Create the fuel counter function
def Fuel_Counter_Upper(x):
    return math.floor(x / 3) - 2

# Read in the inputs provided
inputs = pd.read_csv('day1/input.txt', sep=" ", header=None)

# Apply the fuel counting to each input
fuel_requirements = inputs.apply(Fuel_Counter_Upper, axis=1)

# Sum the fuel requirements for all moduels
total_fuel_required = fuel_requirements.sum()

# Print the answer
print(total_fuel_requirged)