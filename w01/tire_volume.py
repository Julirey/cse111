# File: tire_volume.py
# Author: Julio Reyes

# Summary: This program computes the approximate volume of air inside a tire.

# -Milestone version-

import math

tire_width = float(input("Enter the width of the tire in mm (ex 205): "))
tire_ratio = float(input("Enter the aspect ratio of the tire (ex 60): "))
tire_diameter = float(input("Enter the diameter of the wheel in inches (ex 15): "))

volume = (math.pi * tire_width ** 2 * tire_ratio * (tire_width * tire_ratio + 2540 * tire_diameter)) / 10000000000

print()
print (f"The approximate volume is {volume:.2f} liters")