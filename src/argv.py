import sys

#print("Todos los argumentos pasados en la linea de comandos:", sys.argv)

#print ("El nombre del script python que se esta ejecutando actualmente es", sys.argv[0])

#print("\n\n****Programa para multiplicar dos numeros****\n\n")

numero1 = sys.argv[1]
numero2 = sys.argv[2]

try:
    numero1 = float(numero1)
    numero2 = float(numero2)
    total = numero1 * numero2
    print("El total de la multiplicación de",numero1, "por", numero2, "es igual a",total)
except ValueError:
    print("Error los argumentos para multiplicar han de ser numericos")

#porcentaje = sys.argv[1]
#agrupa = sys.argv[2]
#tarea = sys.argv[3]
#try:
 #   porcentaje=float(porcentaje)
  #  agrupa=int(agrupa)
   # tarea=int(tarea)
   # print("Los datos ingresados para los escenarios son:",porcentaje,agrupa,tarea)
#except ValueError:
 #   print("Ingrese de esta manera: PORCENTAJE, MIN, HORA")

import sys

total = len(sys.argv)
cmdargs = str(sys.argv)
print("The total numbers of args passed to the script: %d " % total)
print("Args list: %s " % cmdargs)
# Pharsing args one by one
print("Script name: %s" % str(sys.argv[0]))
print("First argument: %s" % str(sys.argv[1]))
print("Second argument: %s" % str(sys.argv[2]))