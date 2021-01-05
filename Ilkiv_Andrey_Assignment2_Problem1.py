#Andrey Ilkiv Assignment 2 9/30/2020 section 01

#prints heading for pokemon distance calculator and prints empty line after 2nd line
print('           Pokemon Distance Calculator' , '----------------------------------------------------' , '' , sep='\n')

#Asks user for name of first pokemon. Stored as string
FP1 = input('1. Enter name of first pokemon: ')

#Asks user for name of second pokemon. Stored as string
FP2 = input('2. Enter name of the second pokemon: ')

#Asks user to input x cooridinate of pokemon 1. Stored as float
x1 = float(input('3. Enter x coordinate of first pokemon: '))

#Asks user to input y cooridinate of pokemon 1. Stored as float
y1 = float(input('4. Enter y cooridinate of first pokemon: '))

#Asks user to input x cooridinate of pokemon 2. Stored as float
x2 = float(input('5. Enter x coordinate of second pokemon: '))

#Asks user to input y cooridinate of pokemon 2. Stored as float
y2 = float(input('6. Enter y cooridinate of second pokemon: '))

#Calculates distance between two objects using the distance formula
# Sqrt((x2 - x1)^2+(y2 - y1)^2)
#truncate is used to round to the 100th decimal position
DistanceBetween = format((((x2 - x1)**2+(y2 - y1)**2)**0.5), '.2f')

#prints the distance between pokemon 1 and pokemon 2 in inches
print('' , '      The distance between ' + FP1 + ' and ' + FP2 + ' is ' + str(DistanceBetween) + ' inches.' , sep='\n')
