maas = int(input("Maaş miktarınızı giriniz:"))
cocuksayisi = int(input("Çocuk sayınızı giriniz:"))

if cocuksayisi == 0:
    print("Güncel maaşınız: {} Türk Lirasıdır.".format(maas))
elif cocuksayisi == 1:
    print("Güncel maaşınız: {} Türk Lirasıdır.".format(maas + (maas * 5/100)))

elif cocuksayisi == 2:
    print("Güncel maaşınız: {} Türk Lirasıdır.".format(maas + (maas * 10/100)))

else:
    print("Güncel maaşınız: {} Türk Lirasıdır.".format(maas + (maas * 15/100)))
    
