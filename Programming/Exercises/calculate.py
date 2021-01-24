import os
import math
from math import ceil
from os import system



#caclulateWallArea
def caclulateWallArea(length, width, height):
    calculation=length*width*height
    return calculation
wallArea=caclulateWallArea()

#show the number of gallons needed
def displayGallonsNeeded(wallArea):
    gallons = round((wallArea / 350), 2)
    return gallons
     
#calculate the price per gallon
def calculateGallonPrice(gallons):
    price = gallons * 32
    return price

gallonsOfPaint = displayGallonsNeeded(wallArea)
totalPrice = calculateGallonPrice(gallonsOfPaint)
print(f'The number of gallons needed is: {gallonsOfPaint}')
print(f'For {gallonsOfPaint} gallons of paint, the cost will be ${totalPrice}')