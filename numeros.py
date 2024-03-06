"""
Generadores y decorador de números para las filas de la perfumería, farmacia y cosmetica
"""

def numeros_perfumeria():
    """
    Generador de números para la fila de perfumería
    """
    for i in range(1, 10000):
        yield f"\nP - {i}"
        
def numeros_farmacia():
    """
    Generador de números para la fila de farmacia
    """
    for i in range(1, 10000):
        yield f"\nF - {i}"
        
def numeros_cosmetica():
    """
    Generador de números para la fila de cosmetica
    """
    for i in range(1, 10000):
        yield f"\nC - {i}"
        
p = numeros_perfumeria()
f = numeros_farmacia()
c = numeros_cosmetica()

def decorar_turno(generator):
    """
    Decorador para los números de turno
    """
    return f"\nTurno: {next(generator)} espera en la fila 😊"
