class ucgen:
    def __init__(self,aci1,aci2,aci3):
        self.aci1=aci1
        self.aci2=aci2
        self.aci3=aci3
    def kontrol(self):
        self.toplam=self.aci1+self.aci2+self.aci3
        if self.toplam==180:
            print("Bu bir üçgendir.")
        else:
            print("Bu bir üçgen değildir.")

u1=ucgen(60,80,40)

u1.kontrol()
