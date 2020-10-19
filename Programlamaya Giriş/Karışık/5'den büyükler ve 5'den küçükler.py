########################################################
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
#              Klavyede girilen 10 sayıdan             #
#        5'ten büyük olanların yarısının toplamını     #
# 5'e eşit ve küçük olan sayıların 2 katının toplamını #
#                 bulan programı yazınız.              #
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
########################################################

toplamk=0
toplamb=0
for i in range(10):
    a=int(input("Sayı giriniz:"))
    if a>5:
        toplamb=toplamb+(a/2)
    if a<=5:
        toplamk=toplamk+(a*2)
print("5e eşit ve 5den küçük olan",toplamk)
print("5 den büyük olanlar",toplamb)
