class product:
    def inputdata(self):
        pname = input("Enter the product name: ")
        price = int(input("Enter Price: "))
        qty = int(input("Enter quantity: "))
    def calculation(self):
        self.dis = (self.price*self.qty)*10/100
        self.bill = (self.price*self.qty)-self.dis
        print("Discount",self.dis)
        print("Bill Amount=", self.bill)
prod1 = product()
prod2 = product()
prod1.inputdata()
prod1.calculation()
prod2.inputdata()
prod2.calculation()



