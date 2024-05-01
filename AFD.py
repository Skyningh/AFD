class AutomataFinitoDeterminista:
	def __init__(self, transiciones, estado_inicial, estados_finales):
		self.transiciones = transiciones
		self.estado_inicial = estado_inicial
		self.estados_finales = estados_finales

	def transicion(self, estado, simbolo):
		return self.transiciones.get((estado, simbolo))

	def acepta_cadena(self, cadena):
		estado_actual = self.estado_inicial
		for simbolo in cadena:
			estado_actual = self.transicion(estado_actual, simbolo)
			if estado_actual is None:
				return False
		return estado_actual in self.estados_finales


def main():

	estados = {"q0", "q1", "q2"}
	alfabeto = {"0", "1"}
	transiciones = {("q0", "0"): "q1", ("q0", "1"): "q0", ("q1", "0"): "q2", ("q1", "1"): "q0", ("q2", "0"): "q2", ("q2", "1"): "q2"}
	estado_inicial = "q0"
	estados_finales = {"q1"}

	# Crear el autómata finito determinista
	afd = AutomataFinitoDeterminista(estados, alfabeto, transiciones, estado_inicial, estados_finales)

	# Ejemplo de cadena a evaluar
	cadena = "1010101"

	# Verificar si la cadena es aceptada por el autómata
	if (afd.acepta_cadena(cadena)):
		print("La cadena " + cadena + "es aceptada por el automata")
	else:
		print("La cadena " + cadena + "no es aceptada por el automata")



if (__name__ == "__main__"):
	main()
