width = int(input('Enter the width of the tire in mm (ex 205): '))
aspect = int(input('Enter the aspect ratio of the tire (ex 60): '))
diameter = int(input('Enter the diameter of the wheel in inches (ex 15): '))
print()
volume = 3.14 * width * width * aspect * (width * aspect + 2540 * diameter) / 10000000000
print(f'The approximate volume is {volume} liters')
