# Wczytaj od użytkownika imię
#
# Za pomocą f-string formatting wyświetl na ekranie:
#
#     '''My name... "José Jiménez".
#             I'm an """astronaut!"""'''
#
# Uwaga! Druga linijka zaczyna się od tabulacji
#
# Gdzie wartość w podwójnym cudzysłowiu to ciąg od użytkownika (w przykładzie użytkownik wpisał José Jiménez)


name = input("Type your name: ")
a="'''My name... \""
b="\". \n \t I'm an \"\"\"astronaut!\"\"\"'''"


print(f"{a}{name}{b}")

# Tekst wyświetlony na ekranie ma mieć zamienione wszystkie spacje na _

name = input("Type your name: ")
a="'''My name... \""
b="\". \n \t I'm an \"\"\"astronaut!\"\"\"'''"
a1=a.replace(' ','_')
b1=b.replace(' ','_')
print(f"{a1}{name}{b1}")


# Tekst wyświetlony na ekranie ma być w UPPERCASE

name = input("Type your name: ")
a="'''My name... \""
b="\". \n \t I'm an \"\"\"astronaut!\"\"\"'''"
a1=a.upper()
b1=b.upper()
print(f"{a1}{name}{b1}")