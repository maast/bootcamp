#
#     Stwórz tuple z cyframi od 0-9
#     Przekonwertuj ją do list
#     Na pierwsze miejsce w liście dodaj całą oryginalną tuple
#     Przekonwertuj wszystko na płaski set unikalnych wartości wykorzystując slice


a=0,1,2,3,4,5,6,7,8,9 # tupla
b=list(a) # lista
b.insert(0, a)
print(b)

c=set(b[0])
c.update(b[1:])
print(c)

