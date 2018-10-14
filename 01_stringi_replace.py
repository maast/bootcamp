# Dane poniżej przeczyść, tak aby zmienne zawierały ciąg znaków 'Jana III Sobieskiego'
a = ' 1/2'
b = 'ul Jana III Sobieskiego 1/2'
c = 'ul. Jana III Sobieskiego 1/2'
d = 'ul.Jana III Sobieskiego 1/2'
e = 'ulicaJana III Sobieskiego 1/2'
f = 'Ul. Jana III Sobieskiego 1/2'
g = 'UL. Jana III Sobieskiego 1/2'
h = 'ulica Jana III Sobieskiego 1/2'
i = 'Ulica. Jana III Sobieskiego 1/2'
j = 'Jana 3 Sobieskiego 1/2'
k = 'Jana III Sobieskiego 1 m. 2'
l = 'Jana III Sobieskiego 1 apt 2'

# usuwanie
b1=b.upper().replace('.',' ').replace('UL ','').replace(' 1/2','').strip().title().replace('Iii','III')
print(b1)
c1=c.upper().replace('.',' ').replace('UL ','').replace(' 1/2','').strip().title().replace('Iii','III')
print(c1)
d1=d.upper().replace('.',' ').replace('UL ','').replace(' 1/2','').strip().title().replace('Iii','III')
print(d1)
e1=e.upper().replace('.',' ').replace('ULICA','').replace(' 1/2','').strip().title().replace('Iii','III')
print(e1)
f1=f.upper().replace('UL.','').replace(' 1/2','').strip().title().replace('Iii','III')
print(f1)
g1=g.upper().replace('UL.','').replace(' 1/2','').strip().title().replace('Iii','III')
print(g1)
h1=h.upper().replace('ULICA','').replace(' 1/2','').strip().title().replace('Iii','III')
print(h1)
i1=i.upper().replace('ULICA.','').replace(' 1/2','').strip().title().replace('Iii','III')
print(i1)
j1=j.upper().replace('3','III').replace(' 1/2','').strip().title().replace('Iii','III')
print(j1)
k1=k.upper().replace(' M. ','/').replace(' 1/2','').strip().title().replace('Iii','III')
print(k1)
l1=l.upper().replace(' APT ','/').replace(' 1/2','').strip().title().replace('Iii','III')
print(l1)
