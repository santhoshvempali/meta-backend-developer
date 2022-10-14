

class Payment:
    def __init__(self,name,payment,ammount) -> None:
        self.name=name
        self.payment=payment
        self.ammount=ammount
    def pay(self):
        self.payment=True
    def status(self):
        if(self.payment==True):
            print(self.name+" paid "+"$"+str(self.ammount))
        else:
            print(self.name+" not paid the ammount")
santhosh=Payment("santhosh",True,4500)
Sai=Payment("sai",False,6162)
santhosh.status()
Sai.status()
Sai.pay()
Sai.status()
