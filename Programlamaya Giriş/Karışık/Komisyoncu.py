########################################################
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
#           Bir komisyoncu sattığı mallardan           #
#            50 liraya kadar olanlardan %3             #
#     50 liradan fazla olanlardan %2 komisyon alıyor.  #
#    Klavyeden girilen 5 malın komisyonlarını bularak  #
#             toplam komisyonu hesaplayınız.           #
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
########################################################

k=0
for i in range(5):
    a=int(input("Malın fiyatını giriniz:"))
    if a<=50:
        k=k+(a*3/100)
    elif a>50:
        k=k+(a*2/100)
    print(k)
        
