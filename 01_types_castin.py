# to są metry
a = 1337
# operuje na a
a_km = int(a / 1000)
a_miles = float(a / 1608)
a_nmiles = float(a / 1852)

# Wojtek: zrobil funkcje czyli def -> return; sprytniej, mozna uzyc w dalszym kodzie


print(f'Meters: {a}')  # int
print(f'Kilometers: {a_km}')  # int
print(f'Miles: {a_miles}')  # float
print(f'Nautical Miles: {a_nmiles}')  # float
print(f'All: {a}, {a_km}, {a_miles}, {a_nmiles}')  # int, int, float, float


