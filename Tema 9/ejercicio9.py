ipais = input("Ingrese una cantidad de paises: ")

paises = []
paises.append(ipais)

cadena = ",".join(paises)
print(sorted(list(set(cadena.split(",")))))