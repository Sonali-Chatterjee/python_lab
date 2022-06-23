import pickle

#serialization of an object

#create a class
class PickleTest():
    
    a=0
    b=0
    
    def __init__(self,i_a,i_b):
        self.a = i_a
        self.b = i_b
    
#create an object
obj1 = PickleTest(1,2)

#Serialize an object

with open ("C:\\development\\OOPS_Concept_06_20\\serialization.py", 'wb') as f:
    pickle.dump(obj1,f)
    
#Deserialize an object
with open ("C:\\development\\OOPS_Concept_06_20\\serialization.py", 'rb') as f:
    objfile = pickle.load(f)

print (objfile.a)
print (objfile.b)



