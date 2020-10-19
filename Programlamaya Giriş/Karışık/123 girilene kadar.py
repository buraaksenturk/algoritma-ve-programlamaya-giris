########################################################
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
#               Klavyeden 123 girilene kadar           #
#               girilen sayılardan kaç tane            #
#        tahmin yapıldığını bulan programı yazınız.    #
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
########################################################

t=0
s=int(input("Sifreyi giriniz:"))
while s!=123:
    t=t+1
    s=int(input("Sifreyi giriniz:"))
print(t)
   
