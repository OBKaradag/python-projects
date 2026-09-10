def selamlama(isim):
    if cinsiyet=="erkek":
        print("Sayın",isim,"bey","restorantımıza hoşgeldiniz...")
    elif cinsiyet=="kadın":
        print("Sayın",isim,"hanım","restorantımıza hoşgeldiniz...")
    else:
        print("Sayın",isim,"restorantımıza hoşgeldiniz...")
while True:
    ad=input("isminiz:")
    if ad=="0":
        break
    cinsiyet=input("cinsiyet:")
    selamlama(ad)