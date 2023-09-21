import math

num = int(input('Enter the number of items: '))
per_box = int(input('Enter the number of items per box: '))
boxes = math.ceil(num / per_box)

print(f'For {num} items,  packing {per_box} items in each box, you will need {boxes} boxes.')