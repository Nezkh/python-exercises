def escribir(fichero, datos):
    f = open(fichero,'w')
    
    for linea in datos:
        if not linea.endswith('\n'):
            linea += '\n'
            
        f.write(linea)
        
    f.close()
    
list = [
    'primera linea',
    'segunda linea',
    'tercera linea',
    'cuarta linea',
    'quinta linea',
    'sexta linea',
    'octaba linea',
    'novena linea',
]

escribir('ejercicio8.txt', list)
