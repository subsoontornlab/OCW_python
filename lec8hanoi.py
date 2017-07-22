# size = total number of disc
# fromStack, toStack, spareStack --> stack name
# function print out the instruction on how to solve this problem

def Towers(size, fromStack, toStack, spareStack):
    if size == 1:
        print('Move disc from ' + fromStack + ' to ' + toStack)
    else:
        Towers(size-1, fromStack, spareStack, toStack)
        Towers(1, fromStack, toStack, spareStack)
        Towers(size-1, spareStack, toStack, fromStack)
              
