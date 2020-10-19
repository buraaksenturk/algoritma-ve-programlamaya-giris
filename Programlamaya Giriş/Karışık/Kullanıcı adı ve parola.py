########################################################
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
#             Doğru kullanıcı adı ve parolayı          #
#         girene kadar tekrar deneten python kodu      #
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
########################################################

for i in range(3):
    ka=input("Kullanıcı adınızı giriniz:")
    ks=input("Şifrenizi giriniz:")
    if ka=="admin" and ks=="1234":
        print("Tebrikler Başarılı bir şekilde giriş yaptınız.")
        break
        print("3 kerede doğru girmedidğiniz için bloke oldu")
