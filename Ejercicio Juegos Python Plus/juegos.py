import hangman
import reversegam
import tictactoeModificado
import json

'''
###estructura del contenido del archivo###
jugador = {
	'nombre': str,
	'hangman': {'attempts': int, 'wins': int, 'loses': int},
    'tictactoe': {'attempts': int, 'tie': int, 'wins':int, 'loses':int},
    'reversegam': {'attempts': int, 'tie': int, 'wins':int, 'loses':int}
          }'''

"""
Probar si anda con un usuario ya registrado
"""

def actualizarPuntajes(jugador):
	jugadores = []
	with open('datos.json','r') as f:
		jugadores = json.load(f) #cargo mi archivo de jugadores
	x = 0
	while (jugadores[x]['nombre'] != jugador['nombre']): #Busco la posicion de mi jugador
		x = x + 1
	jugadores[x] = jugador #sobre-escribo el jugador antiguo por el actualizado 
	with open('datos.json','w') as f:
		json.dump(jugadores,f, indent=4) #Re-escribo todo el archivo con el jugador actualizado
	print('Puntajes guardados exitosamente')

def dialogo(usuario):
	print('El Usuario ',usuario['nombre'])
	print('En el ahoracado jugó',usuario['hangman']['attempts'],' veces, de las cuales gaste',usuario['hangman']['wins'],' y perdiste ',usuario['hangman']['loses'])
	print('En el tateti jugó',usuario['tictactoe']['attempts'],' veces, de las cuales ',usuario['tictactoe']['tie'],' fueron empate, ganaste ',usuario['tictactoe']['wins'],' y perdiste ',usuario['tictactoe']['loses'])
	print('en el otello jugó',usuario['reversegam']['attempts'],' veces, de las cuales ',usuario['reversegam']['tie'],' fueron empate, ganaste ',usuario['reversegam']['wins'],' y perdiste ',usuario['reversegam']['loses'])
	return()

def MostrarPuntajes():
	jugadores = []
	with open('datos.json') as f:
		jugadores = json.load(f)
		for(key) in jugadores:
			dialogo(key)
	return()


def existejugador(nombre):
	existe= False
	jugadores = []
	try:
		with open('datos.json') as f: #Si el archivo existe
			jugadores = json.load(f)
			for key in jugadores:
				if key['nombre'] == nombre:  #Busco el jugador
					existe= True	
					print('Que felicidad, regresaste!')	
					break			
	except FileNotFoundError: #Si no existe
		with open('datos.json','w') as f: #Creo el archivo
			jugador = {}
			jugador['nombre'] = nombre
			jugador['hangman'] = {'attempts': 0, 'wins': 0, 'loses': 0}
			jugador['tictactoe'] = {'attempts': 0, 'tie': 0, 'wins':0, 'loses':0}
			jugador['reversegam'] = {'attempts': 0, 'tie': 0, 'wins':0, 'loses':0}
			jugadores.append(jugador)
			json.dump(jugadores,f, indent=4)  #Cargo el usuario
			print('Bienvenido ',nombre)
			existe = True
	return(existe) #Retorno True o False si el usuario está o no en el archivo de 
	
def agregarJugador(nombre):
	jugadores = []
	jugador = {}
	jugador['nombre'] = nombre
	jugador['hangman'] = {'attempts': 0, 'wins': 0, 'loses': 0}
	jugador['tictactoe'] = {'attempts': 0, 'tie': 0, 'wins':0, 'loses':0}
	jugador['reversegam'] = {'attempts': 0, 'tie': 0, 'wins':0, 'loses':0}
	with open('datos.json','r') as f:
		jugadores = json.load(f) #cargo mi archivo de jugadores
	jugadores.append(jugador)
	with open('datos.json','w') as f:
		json.dump(jugadores,f, indent=4) #Re-escribo todo el archivo con el jugador actualizado
	print('Bienvenido ',nombre)
	return()

def quieroMiJugador(nombre): 
	jugador = {}
	with open('datos.json') as f: 
		jugadores = json.load(f)
		for key in jugadores:
			if key['nombre'] == nombre: #Busco el jugador
				jugador = key
	return(jugador) #Retorno el jugador

def mostrarMisPuntajes(usuario):
	print('En el ahoracado jugaste',usuario['hangman']['attempts'],' veces, de las cuales gaste',usuario['hangman']['wins'],' y perdiste ',usuario['hangman']['loses'])
	print('En el tateti jugaste ',usuario['tictactoe']['attempts'],' veces, de las cuales ',usuario['tictactoe']['tie'],' fueron empate, ganaste ',usuario['tictactoe']['wins'],' y perdiste ',usuario['tictactoe']['loses'])
	print('en el otello jugaste',usuario['reversegam']['attempts'],' veces, de las cuales ',usuario['reversegam']['tie'],' fueron empate, ganaste ',usuario['reversegam']['wins'],' y perdiste ',usuario['reversegam']['loses'])
	return()


def main():
	jugador = {}
	nombre = input('Ingrese su nombre ')
	if existejugador(nombre):
		jugador= quieroMiJugador(nombre)
	else:
		agregarJugador(nombre)
		jugador= quieroMiJugador(nombre)

	sigo_jugando = True
	while sigo_jugando:
		
		print('''
		¿Qué deseas hacer?
		1.- Ahorcado
		2.- Ta-TE-TI
		3.- Otello
		4.- Mostrar tu puntaje
		5.- Mostrar todos los puntajes
		0.- Guardar y salir''')

		opcion = input()
		if opcion == '1':
			jugador['hangman'] = hangman.main(jugador['hangman'])
		if opcion == '2':
			jugador['tictactoe'] = tictactoeModificado.main(jugador['tictactoe'])
		elif opcion == '3':
			jugador['reversegam'] = reversegam.main(jugador['reversegam'])
		elif opcion == '4':
			mostrarMisPuntajes(jugador)
		elif opcion == '5':
			MostrarPuntajes()
		elif opcion == '0':
			actualizarPuntajes(jugador)
			sigo_jugando = False

if __name__ == '__main__':
	main()
