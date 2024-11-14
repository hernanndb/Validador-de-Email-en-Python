email=input("introduce tu email:")
contador_de_puntos=0
contador_de_arrobas=0
numero_de_letras=0

for i in email:
	if (i=="@"):
		contador_de_arrobas=contador_de_arrobas+1
	elif (i=="."):
		contador_de_puntos=contador_de_puntos+1
	else:
		numero_de_letras=numero_de_letras+1

if (contador_de_arrobas==1 and contador_de_puntos>=1):
	print("el email es correcto")
else:
	print("el email es incorrecto")