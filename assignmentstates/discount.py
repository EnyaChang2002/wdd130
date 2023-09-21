from datetime import datetime
subtotal = float(input('Please enter the subtotal: '))

daytime = datetime.now()
time = daytime.weekday()
time = 2
total = 0
tax = subtotal * 0.06
if subtotal >= 50:
    if time == 1 or time == 2:
        discount = subtotal * 0.1
        tax = subtotal * 0.06
        total = subtotal - discount + tax
        print(f'Discount amount: {discount}')
    else:
        total = subtotal + tax
else:
    total = subtotal + tax

print(f'Sales tax amount: {tax}')
print(f'Total: {total}')