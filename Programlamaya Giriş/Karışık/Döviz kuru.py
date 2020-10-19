########################################################
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
#                                                      #
#                       DÖVİZ KURU                     #
#                                                      #
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
########################################################

dolar=int(input("Dolar Kuru Ne Kadar?"))
euro=int(input("Euro Kuru Ne Kadar?"))
altin=int(input("1 Gram Altın Ne Kadar?"))
para=int(input("Kaç Türk Liran Var?"))
def hesap(dolar,euro,altin,lira):
    print(para/dolar,"Kadar Dolar Alabiliyorsun.")
    print(para/euro,"Kadar Euro Alabiliyorsun.")
    print(para/altin,"Kadar Altın Alabiliyorsun.")
hesap(dolar,euro,altin,para) 
