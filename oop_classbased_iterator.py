class Evenodd_numbers:
    
    def __init__(self,max):
        self.max = max
        self.number = 0
        
    def __iter__(self):
        return self
    
    def __next__(self):
        
        self.number += 1
        
        if self.number > self.max :
            print("Max number of iteration reached :", self.max)
        else:
            if self.number%2 != 0:
                print(str(self.number),"is an odd number")
            else:
                print(str(self.number),"is an even number")
            
obj = Evenodd_numbers(5)

obj.__next__()
obj.__next__()
obj.__next__()
obj.__next__()
obj.__next__()
obj.__next__()



            