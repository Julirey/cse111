
from datetime import datetime

DISC_RATE = 0.10
SALES_TAX_RATE = 0.06

keep_going = 1
subtotal = 0

current_date_and_time = datetime.now()
weekday = current_date_and_time.weekday()


while keep_going != 0 : 
    price = float(input("Please enter the price of the item: "))
    if price == 0 :
        keep_going = 0
    else : 
        quantity = int(input("How many items? ") )
        items_total = price * quantity
        subtotal += items_total   

print ()
print (f"Subtotal: {subtotal:.2f}")

if subtotal >= 50 and (weekday == 1 or weekday == 2):
    discount = round(subtotal * DISC_RATE, 2)
    print(f"Discount amount: {discount:.2f}")
    subtotal -= discount
elif subtotal < 50 and (weekday == 1 or weekday == 2):
    missing_amount = 50 - subtotal
    print (f"Discount amount: To receive a discount of 10% today your subtotal would need about {missing_amount}$ more")

sales_tax = round(subtotal * SALES_TAX_RATE, 2)
print(f"Sales tax amount: {sales_tax:.2f}")

total = subtotal + sales_tax
print(f"Total: {total:.2f}")