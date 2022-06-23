import json

bill_json = """{"BillNumber": 12345,
             "BillTotal": 125,
             "StoreLocation":"Phoenix",
             "BillDetails": [ {"Product":"Softdrinks",
                               "Quantity":10,
                               "UnitPrice":2,
                               "LineItemprice":20},
                              {"Product":"chips",
                               "Quantity":5,
                               "UnitPrice":3,
                               "LineItemprice":15},
                              {"Product":"Cookies",
                               "Quantity":12,
                               "UnitPrice":1,
                               "LineItemprice":20} ]
            }"""

print(bill_json)
#parse json using "loads" method            
y = json.loads(bill_json)

#get subset of json            
print(y["BillDetails"])

#json nested value, get the first product
print(y["BillDetails"][0]["Product"])

#json get all products
for restaurant in y["BillDetails"]:
    print(restaurant["Product"])
                             
                                                          