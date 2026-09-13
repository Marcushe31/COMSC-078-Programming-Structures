# Marcus Hernandez
# COMSC-078, Section 202
# Assignment 2 - Functions (second program: Degree Conversions)
# asks the user for an angle in degrees-minutes-seconds form and 
# converts that to decimal degrees using the to_decimal() function

import math

def to_decimal(degrees, minutes, seconds):
    """Convert degrees, minutes, and seconds to decimal degrees."""
    degrees = int(degrees)
    minutes = abs(int(minutes))
    seconds = abs(seconds)
    magnitude = abs(degrees) + (minutes / 60) + (seconds / 3600)

    return math.copysign(magnitude, degrees)

entered_degrees = float(input("Please enter degrees: "))
entered_minutes = float(input("Please enter minutes: "))
entered_seconds = float(input("Please enter seconds: "))

decimal_degrees = to_decimal(entered_degrees, entered_minutes, entered_seconds)
print(f"The decimal degrees is: {decimal_degrees}")