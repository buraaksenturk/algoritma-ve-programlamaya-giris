########################################################
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
#                  200'ü geçinceye kadar               #
#                girilen sayıların toplamı             #
#             ve kaç sayı girildiğini bulunuz.         #
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
########################################################

a=int(input("bir sayı giriniz:"))
toplam=0
sayac=0
while toplam<=200:
    toplam=toplam+a
    sayac=sayac+1
    
    print(toplam)
    a=int(input("bir sayı giriniz:"))
print("son toplam:", toplam)

print("girilen değer sayısı:",sayac)
