class personel():
    sirket="ybs"
    def __init__(self,isim,maas,yetenek,rutbe):
        self.isim=isim
        self.maas=maas
        self.yetenek=yetenek
        self.rutbe=rutbe
        self.gunsayisi=0
    def calis(self):
        print("sayın", self.isim," çalışıyorsunuz")
        self.gunsayisi=self.gunsayisi+1
    def terfi(self):
        self.maas=self.maas+200
        print("tebrikler terfi ettiniz yeni mmaş:",self.maas)
    def goster(self):
        print("*_"*20)
        print("personel maaşı:",self.maas)
        print("personel yetenekleri:",self.yetenek)
        print("personelin konumu.",self.rutbe)
        print("personelin çalıştığı gün sayısı:",self.gunsayisi)
        print("*_"*20)

class yonetici(personel):
    def terfi(self):
        self.maas=self.maas+523
    def __init__(self,isim,maas,yetenek,rutbe,yonbecerisi):
        super().__init__(isim,maas,yetenek,rutbe)
        self.yonbecerisi=yonbecerisi
    def bilggoster(self):
        super().goster()
        print("yönetim becerisi=",self.yonbecerisi)
    def calis(self):
        super().calis()
        self.yonbecerisi=self.yonbecerisi+5
        print("yönetim beceriniz arttırılfı")
eda=yonetici("eda öz",6000,"php,yönetim,iletişim","proje müdürü",67)
eda.terfi()
eda.calis()
eda.bilggoster()
