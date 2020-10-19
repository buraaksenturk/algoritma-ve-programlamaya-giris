########################################################
#~~~~~~~~~~~~~~~~~~~~~~~~~~-~~~~~~~~~~~~~~~~~~~~~~~~~~~#
#                  Bir otopark sistemi                 #
#                  1 saat üzerinde ise                 #
#             aşağadaki artışları uyguluyor.           #
#~~~~~~~~~~~~~~~~~~~~~~~~~~-~~~~~~~~~~~~~~~~~~~~~~~~~~~#
########################################################

tu=5 #Taksi Ücreti
mu=6 #Minibüs Ücreti
tau=6.5 #Ticari Araç Ücreti
borc=0
a=input("Aracınız Nedir? Taksi:t, Minibüs:m, Ticari:ta")
saat=int(input("Kaç saat durdunuz?"))

if a=="t" and saat<=1:
    borc=tu
    print(borc)
if a=="t" and saat>1:
    borc=(tu+(tu*20/100))*saat

    
if a=="m" and saat<=1:
    borc=mu
    print(borc)
if a=="m" and saat>1:
    borc=(mu+(mu*21.5/100))*saat

if a=="ta" and saat<=1:
    borc=tau
    print(borc)
if a=="ta" and saat>1:
    borc=(tau+(tau*25/100))*saat
