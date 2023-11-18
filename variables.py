
'''
Define una variable de cada tipo de primitivo
'''
entero = 10
cadenas = 'Hola esto es python'
decimal = 12.2
boleana = True


'''
Concatena a la cadena las otras variables aplicandola conversión
correcta para funcionar, guarda el resultado en una variable
'''
 
concatenacion = 'El ntero es: '+str(entero)+', La cadena es: '+cadenas+', El flotante es: '+str(decimal)+', La variable booleana es: '+str(boleana)
print(concatenacion)

print('\n')
'''
Investiga sobre el límite de los enteros y los flotantes en python
y anotar sus descubrimientos como comentarios en el archivo
'''

#En Python, el tamaño de los enteros y flotantes no está limitado por la cantidad de bits 
#como en algunos otros lenguajes de programación. La cantidad de memoria asignada a un entero
#o un flotante en Python puede crecer dinámicamente para acomodar números grandes.


#Enteros (int): En versiones anteriores de Python (Python 2), el tamaño de los enteros
#  estaba limitado por la memoria del sistema, lo que significa que había un límite práctico.
#  Sin embargo, en Python 3, los enteros pueden crecer hasta el límite de la memoria disponible.

#Flotantes (float): Los números de punto flotante en Python siguen el estándar IEEE 754, 
#  por lo que el límite de precisión y rango está determinado por las especificaciones de este
#  estándar. Los flotantes de Python tienen una precisión de aproximadamente 15-16 dígitos
#  decimales significativos.

'''
Aplica la fórmula de la suma de los primeros n números pares (investigar),
 tomando como n la variable de tipo entero y almacenar el resultado en una variable
'''

n = int(input('dijite el numero limite para la suma de los pares: '))
suma = n * (n + 1)

print(f'La suma de los primeros {n} números es: {suma}')

print('\n')