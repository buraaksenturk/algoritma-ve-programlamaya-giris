class kisi:
    yas=0
    def __init__(self,isim,dt,my):
        self.isim=isim
        self.dt=dt
        self.my=my
    def yazdir(self):
        self.yas=self.my-self.dt
        print("sayın",self.isim,"yaşınız",self.yas,"dır")

isim=input("Adınızı Giriniz:")
dogtar=int(input("Doğduğunuz Yılı Giriniz"))
mevcutyıl=int(input("Mevcut Yılınızı Giriniz"))

karakter1=kisi(isim,dogtar,mevcutyıl)
karakter1.yazdir()
