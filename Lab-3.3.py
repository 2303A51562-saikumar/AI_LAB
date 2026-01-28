
#Task:-01

# Read Previous Units (PU) with input validation
while True:
	pu_input = input("Enter Previous Units (PU): ")
	pu_input = pu_input.strip()
	try:
		previous_units = float(pu_input)
		break
	except ValueError:
		print("Invalid input. Please enter a numeric value for Previous Units.")

# Read Current Units (CU) with input validation
while True:
	cu_input = input("Enter Current Units (CU): ")
	cu_input = cu_input.strip()
	try:
		current_units = float(cu_input)
		break
	except ValueError:
		print("Invalid input. Please enter a numeric value for Current Units.")

# Read Type of Customer (free-text; examples: Domestic, Commercial)
customer_type = input("Enter Type of Customer (e.g., Domestic / Commercial): ").strip()

# Calculate units consumed (CU - PU). This program does not implement
# billing rates; it only computes consumption as requested.
units_consumed = current_units - previous_units

# Basic sanity check: consumption should not be negative
if units_consumed < 0:
	print("\nWarning: Current Units is less than Previous Units. Please verify inputs.")

# Output the captured inputs and computed value with clear labels
print("\n--- Consumer Details ---")
print(f"Previous Units: {previous_units}")
print(f"Current Units:  {current_units}")
print(f"Type of Customer: {customer_type}")
print(f"Units Consumed: {units_consumed}")


#Task:-02
# Energy charges depend on the number of units consumed and customer type.
#from task 1 and extend it to.
#calculate the energy charges.
#Use conditional statements based on:
#o Domestic
#o Commercial
#o Industrial consumer.
def 