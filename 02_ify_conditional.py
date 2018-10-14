# def stalej oznaczajacej pelnoletniosc
doroslosc = 18
# zapytaj uzytkownika ile ma lat, wrzuc do floata
lat = float(input("Ile masz lat: "))

# if isinstance(lat,float):
    if int(lat) >= doroslosc:
        napisz = 'pelnoletni'
    else:
        napisz = 'malolat'
    print(napisz)
# else:
#     print('To nie jest wiek')
