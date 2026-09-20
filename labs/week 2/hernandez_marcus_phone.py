# Marcus Hernandez
# COMSC-078, Section 202
# Assignment 2 - Functions (third program: Phone Plan Cost Comparison)
# asks the user for a number of units used, then uses a calculate_cost()
# function to price two different phone plans and report which one is cheaper


def get_units():
    """Ask the user for the number of units used and return it as an integer."""
    return int(input("Please enter the number of units used: "))

def calculate_cost(units, base_cost, base_limit, cost_per_extra_unit):
   """Return the total cost of a plan for the given number of units.
   Units at or below the base limit cost ONLY the base cost, and using max() 
   keeps the overage from going negative if the units are below the base limit."""
   return base_cost + (max(0, units - base_limit) * cost_per_extra_unit)

units_used = get_units()

if units_used < 0:
    print("Error: The number of units used cannot be negative!")
else:
    plan_a_cost = calculate_cost(units_used, 9.38, 65, 0.045)
    plan_b_cost = calculate_cost(units_used, 8.57, 50, 0.052)

    print (f"Plan A costs: ${plan_a_cost:.2f}")
    print (f"Plan B costs: ${plan_b_cost:.2f}")

    if plan_a_cost < plan_b_cost:
        print("Plan A is cheaper!")
    elif plan_b_cost < plan_a_cost:
        print("Plan B is cheaper!")