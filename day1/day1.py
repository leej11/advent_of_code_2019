import math
import pandas as pd

print("Attempting execution")
# Create the fuel counter function
def Fuel_Counter_Upper(x):
    return math.floor(x / 3) - 2

def Fuel_Counter_Upper_2(x):
    input = x
    fuel_required = 0
    while Fuel_Counter_Upper(input) > 0:
        fuel_required += Fuel_Counter_Upper(input)
        input = Fuel_Counter_Upper(input)

    return fuel_required


# Read in the inputs provided
inputs = pd.read_csv('input.txt', sep=" ", header=None)

# Apply the fuel counting to each input
fuel_requirements = inputs.apply(Fuel_Counter_Upper_2, axis=1)

# Sum the fuel requirements for all moduels
total_fuel_required = fuel_requirements.sum()

# Print the answer
print(total_fuel_required)