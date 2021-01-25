import os
import math
from os import system
from Programming.Exercises.calculate import calculateGallonPrice, displayGallonsNeeded, caclulateWallArea

#Ask user for the length width and height
length=int(input('Please enter the length of the room: '))
width=int(input('Please enter the width of the room: '))
height=int(input('Please enter the height of the room: '))

wallArea = caclulateWallArea(length, width, height)
gallonsOfPaint = displayGallonsNeeded(wallArea)
totalPrice = calculateGallonPrice(gallonsOfPaint)

print(f'The number of gallons needed is: {gallonsOfPaint}')
print(f'For {gallonsOfPaint} gallons of paint, the cost will be ${totalPrice}')