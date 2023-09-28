# File: tire_volume.py
# Author: Julio Reyes

# Summary: This program computes the approximate volume of air inside a tire, gets 
# the current date from the user's operating system and writes text to a file on the user's hard drive.
# If the user wants to buy the tire of the specified dimensions, the program will ask for its phoner number
# and stores it in the same file with the rest of the information.

# -Full version-

import math
from datetime import datetime

tire_width = float(input("Enter the width of the tire in mm (ex 205): "))
tire_ratio = float(input("Enter the aspect ratio of the tire (ex 60): "))
tire_diameter = float(input("Enter the diameter of the wheel in inches (ex 15): "))

tire_volume = (math.pi * tire_width ** 2 * tire_ratio * (tire_width * tire_ratio + 2540 * tire_diameter)) / 10000000000

print() 
print (f"The approximate volume is {tire_volume:.2f} liters")
print()

buy = input("Do you want to buy tires with the entered dimensions? [YES/NO] ")
if buy.lower() == "yes": 
    phone_number = input("Please enter your phone number: ")

current_date_and_time = datetime.now()

with open("volumes.txt", "at") as volumes_file:
    if buy.lower() != "yes":
        print(f"{current_date_and_time:%Y-%m-%d}, {tire_width}, {tire_ratio}, {tire_diameter}, {tire_volume:.2f}", file=volumes_file)
    else: 
        print(f"{current_date_and_time:%Y-%m-%d}, {tire_width}, {tire_ratio}, {tire_diameter}, {tire_volume:.2f} - Phone Number: {phone_number}", file=volumes_file)