even = 2
# zapytaj uzytkownika ile ma lat, wrzuc do floata
liczba = float(input("Wpisz liczbe: "))

if int(liczba) % even == 0:
    print('Parzysta, brawo')
else:
    print('nieparzysta')
