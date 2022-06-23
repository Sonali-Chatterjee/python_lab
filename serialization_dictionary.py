import pickle

#Serialization/deserialization of a dictionary

#create a dictionary
Dict_serl = {"Apple":"Fruit","Potato":"Vegetable",20 :"Numbers"}

    
#Serialize an object
with open ("C:\\development\\OOPS_Concept_06_20\\serialization.py", "wb") as f:
    pickle.dump(Dict_serl,f)
    
#Deserialize an object
with open ("C:\\development\\OOPS_Concept_06_20\\serialization.py", "rb") as f:
    Dict_serl = pickle.load(f)

print (Dict_serl)
