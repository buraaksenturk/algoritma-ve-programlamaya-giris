v1=int(input("Birinci Hızı Giriniz : "))
v2=int(input("İkinci Hızı Giriniz : "))
v3=int(input("Üçüncü Hızı Giriniz : "))
t1=int(input("Birinci Zamanı Giriniz : "))
t2=int(input("İkinci Zamanı Giriniz : "))
t3=int(input("Üçüncü Zamanı Giriniz : "))

vort=((v1*t1)+(v2*t2)+(v3*t3))/(t1+t2+t3)

print("Tüm yol boyunca ortalama hız : ",vort)
