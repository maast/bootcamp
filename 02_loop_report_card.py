# Przekonwertuj skalę ocen (2, 3, 3.5, 4, 4.5, 5) na listę float za pomocą inline for

skala = (2, 3, 3.5, 4, 4.5, 5)

skala_float = [float(x) for x in skala]
skala_float2 = [float(x) for x in (2, 3, 3.5, 4, 4.5, 5)]

print(skala)
print(skala_float)

dzienniczek=list()


while True:
    podaj_ocene = input('Podaj ocene: ')
    if not podaj_ocene:
        break

    if float(podaj_ocene) in skala_float:
        dzienniczek.append(float(podaj_ocene))
        print(f'dodaje do slownika: {podaj_ocene}')
    else:
        print("Nie ma takiej oceny")

srednia=sum(dzienniczek)/len(dzienniczek)
print(f'srednia wynosi: {srednia}')

