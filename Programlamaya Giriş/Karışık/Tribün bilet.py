class tribün():
    def __init__(self,ad,soyad,rütbe,takım):
        self.ad=ad
        self.soyad=soyad
        self.rütbe=rütbe
        self.takım=takım
        self.bilfiy=0
    def bilet(self):
        self.bilfiy+=200
        print("Bileti Aldınız.")
    def göster(self):
        print("Adınız:",self.ad)
        print("Soyadınız:",self.soyad)
        print("Rütbeniz:",self.rütbe)
        print("Takımınız:",self.takım)
        print("Bilet fiyatı:",self.bilfiy)

x=tribün("Burak","Şentürk","Normal vatandaş","FB")
x.bilet()
x.göster()
        
