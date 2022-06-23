class Tinitiate:
    
    t1_var=100
    # In python only one constuctor for one class
    def __init__(self,p_var1,p_var2):
        self.var1=p_var1
        self.var2=p_var2
        
    def print_member_attributes(self):
        print(self.t1_var)
        print("atrributes from constructor var1", self.var1, "var2:", self.var2)
        
t1object = Tinitiate(1,2)
t1object.print_member_attributes()
    