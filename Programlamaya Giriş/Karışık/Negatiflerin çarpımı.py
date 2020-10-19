########################################################
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
#               Klavyeden girilen 10 sayıdan           #
#            sadece negatif olanların çarpımını        #
#              ekrana yazan programı yazınız.          #
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
########################################################

carpım=1
for i in range(10):
    a=int(input("Sayı giriniz"))
    if a<0:
        carpım=carpım*a
print("Negatif sayıların çarpımı=",carpım)
