asalsayac = 2
asaldizi = []
elenecekdizi = []
sayi = input("Sayi girin:")
sayi = int(sayi)

while(asalsayac < sayi):
    if(not elenecekdizi):
        asaldizi.append(asalsayac)
        asaltut = asalsayac
        asaltut += asalsayac
        while (asaltut <= sayi):
            elenecekdizi.append(asaltut)
            asaltut += asalsayac
        asalsayac +=1
    else:
        for kontrol in elenecekdizi:
            if(kontrol == asalsayac):
                if(asalsayac <= sayi):
                    asalsayac +=1
                    break
        if(asalsayac not in elenecekdizi and asalsayac < sayi):
            asaldizi.append(asalsayac)
            asaltut = asalsayac
            asaltut += asalsayac
            while (asaltut <= sayi):
                elenecekdizi.append(asaltut)
                asaltut += asalsayac
            asalsayac +=1

for yaz in asaldizi:
    print(yaz)