import math
#get base
inputOK = False
while not inputOK:
    base = float(input('Enter base: '))
    if type(base) == type(1.0): inputOK = True
    else: print('Error. Base must be a floating point number')
    

#get height
inputOK = False
while not inputOK:
    height = float(input('Enter height: '))
    if type(height) == type(1.0): inputOK = True
    else: print('Error. Height must be a floating point number')

hyp = math.sqrt(base*base + height*height)

print('Base: ' + str(base) + ' ,height: ' + str(height) + '  ,hyp: ' + str(hyp)) 
