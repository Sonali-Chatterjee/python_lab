
#function converted to a generator using keyword "yield"
def Generator_Demo():
    yield 22
    yield 33
    yield 44
    yield 55

#call the function as iterator    
myitr = Generator_Demo()

#print the state of the function as an iterator
print(myitr.__next__())
print(myitr.__next__())
print(myitr.__next__())
print(myitr.__next__())

 
    