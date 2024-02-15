# File: receipt.py
# Author: Julio Reyes

# Summary: This program prints a receipt for a customer’s grocery order.  

# -Milestone  version-

import csv

def main():
    products_dict = read_dictionary("products.csv", 0)
    
    print()
    print ("All Products")
    print_dictionary(products_dict)
    print()
    
    with open("request.csv", "rt") as infile:
        
        reader = csv.reader(infile)
        next(reader)

        print ("Requested Items:")
        for line in reader:
            number = line[0]
            quantity = line[1]

            name = products_dict[number][1]
            price = products_dict[number][2]
            print(f"{name}: {quantity} @ {price}")
            



def read_dictionary(filename, key_column_index):
    """Read the contents of a CSV file into a compound
    dictionary and return the dictionary.

    Parameters
        filename: the name of the CSV file to read.
        key_column_index: the index of the column
            to use as the keys in the dictionary.
    Return: a compound dictionary that contains
        the contents of the CSV file.
    """
    dictionary = {}

    with open(filename, "rt") as infile:
        reader = csv.reader(infile)

        next(reader)

        for line in reader:
            number = line[key_column_index]
            name = line[1]
            price = float(line[2])

            dictionary[number] = [number, name, price]
    
    return dictionary

def print_dictionary(dictionary):
    for key, items in dictionary.items():
        print(f"{key} : {items[1]}")

if __name__ == "__main__":
    main()