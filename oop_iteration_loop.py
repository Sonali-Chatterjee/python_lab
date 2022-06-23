#create a list of data
data_set = [1,2,3,4]

#loop or iterate over this data list using loop
for value1 in data_set:
    print (value1)

#create an iterator using "iter" function    
itr = iter(data_set)

#call the print to display nest value
print(itr.__next__())
print(itr.__next__())
print(itr.__next__())
print(itr.__next__())