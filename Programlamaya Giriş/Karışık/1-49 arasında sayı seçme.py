#1,49 arasında rastgele 6 sayı seçip listeye ekleme
import random
a=[]
for i in range(6):
    b=random.randrange(1,49)
    a=a+[b]
    print(a)
dogru=0
tahminler=[]
for j in range(6):
    tahmin=int(input("tahmini giriniz:"))
    tahminler=tahminler+[tahmin]
    for z in a:
        if z==tahmin:
            dogru=dogru+1
print("bilgisayarın seçtikleri:",a)
print("tahminleriniz:",tahminler)
print("doğru sayınız:",dogru)
