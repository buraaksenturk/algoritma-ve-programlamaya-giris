class Personel():
    sirket="YBS"
    def __init__(self,isim,maas,yetenek,rutbe):
        self.isim=isim
        self.maas=maas
        self.yetenek=yetenek
        self.rutbe=rutbe
        self.gunsayisi=0
    def calis(self):
        print(self.isim,"çalışıyor")
        self.gunsayisi+=1
    def terfi(self):
        print("Tebrikler",self.isim,"Terfi ettin")
        self.maas+=200
    def bilgileriGoster(self):
        print("*_"*20)
        print("Personelin adı:",self.isim)
        print("Personelin Maaşı:",self.maas)
        print("Personelin yetenekleri:",self.yetenek)
        print("Personelin Rütbesi:",self.rutbe)
        print("personelin çalıştığı gün:",self.gunsayisi)
        print("*_"*20)
class yonetici(Personel):
    def yukselme(self):
        self.maas+=523
    def __init__(self,isim,maas,yetenek,rutbe,yonbec):
        super().__init__(isim,maas,yetenek,rutbe)
        self.yonbec=yonbec
    def beceriart(self):
        self.yonbec+=10
    def gosterme(self):
        super().bilgileriGoster()
        print("Yönetim Becerisi:",self.yonbec)
        print("*_"*20)

class hizmetli(Personel):
    def __init__(self,isim,maas,yetenek,rutbe,yas,calyil):
        super().__init__(isim,maas,yetenek,rutbe)
        self.yas=yas
        self.calyil=calyil
    def maasart(self):
        self.maas+=150
    def bilggos(self):
        super().bilgileriGoster()
        print("Hizmetlinin Yaşı:",self.yas)
        print("Hizmetlinin Çalışma Yılı:",self.calyil)


class grafiker(Personel):
    def __init__(self,isim,maas,yetenek,rutbe,mesai):
        super().__init__(isim,maas,yetenek,rutbe)
        self.mesai=mesai
        self.hakedis=0
    def toplam(self):
        self.hakedis=self.maas+(self.mesai*150)
    def bilggoster(self):
        super().bilgileriGoster()
        print("Bu ay yaptığınız mesai:",self.mesai)
        print("Toplam Hakedişiniz:",self.hakedis)

Hasan=grafiker("Hasaz ÖZ",3460,"php web","ön tasarımcı",23)

Hasan.toplam()

Hasan.bilggoster()














