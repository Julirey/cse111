# File: receipt.py
# Author: Julio Reyes

# Summary: This program prints a receipt for a customer’s grocery order.  

# -Full  version-

import csv
from datetime import datetime

def main():
    try:
        current_date_and_time = datetime.now()
        weekday = current_date_and_time.weekday()

        store_name = "Inkom Emporium"
        request_file = "request.csv"
        products_file = "products.csv"
        products_dict = read_dictionary(products_file, 0)
        
        items_number = 0
        subtotal = 0
        sales_tax_rate = 0.06
        total = 0
            
        print (store_name)
        print()

        with open(request_file, "rt") as infile:
            
            reader = csv.reader(infile)
            next(reader)


            for line in reader:
                number = line[0]
                quantity = int(line[1])

                name = products_dict[number][1]
                price = products_dict[number][2]
                print(f"{name}: {quantity} @ {price}")

                items_number += quantity

                # Discount the product prices by 10% if today is Tuesday or Wednesday
                if weekday == 1 or weekday == 2:
                  price -= price * 0.1   
                  subtotal += quantity * price 
                else:
                    subtotal += quantity * price 
        print()

        sales_tax = subtotal * sales_tax_rate
        total = subtotal + sales_tax

        print (f"Number of items: {items_number}")
        print (f"Subtotal: {subtotal:.2f}")
        print (f"Sales Tax: {sales_tax:.2f}")
        print (f"Total: {total:.2f}")
        print()

        print (f"Thank you for shopping at the {store_name}")
        print(f"{current_date_and_time:%a %b %d %H:%M:%S %Y }")

    except FileNotFoundError as not_found_err:
        print("Error: missing file")
        print(not_found_err)

    except PermissionError as perm_err:
        print(type(perm_err).__name__, perm_err, sep=": ")
        
    except (csv.Error, KeyError) as key_err:
        print(f"Error: unkown product ID in the {infile.name} file")
        print(key_err)


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

if __name__ == "__main__":
    main()