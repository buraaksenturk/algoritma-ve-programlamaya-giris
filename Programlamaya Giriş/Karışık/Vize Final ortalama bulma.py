vize=int(input("Vize notunuzu giriniz:"))
final=int(input("Final notunuzu giriniz:"))
ort=((vize*40/100)+(final*60/100))/2
if ort>=50:
    print("Geçtiniz. Ortalamanız:",ort )
else:
    print("Dersten kaldınız. Ortalamanız:",ort)
