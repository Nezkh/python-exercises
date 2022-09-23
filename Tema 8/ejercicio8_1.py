f = open('ejercicio8-1.txt', 'w')
f.write('He creado la primera linea de mi archivo \n')
f.close()

f = open('ejercicio8-1.txt', 'a')
f.write("he agregado la segunda linea de texto")
f.close()

print(f.read)