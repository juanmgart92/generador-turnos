# todos los generadores
# decorador

def numeros_perfumeria():
    for i in range(1, 10000):
        yield f"\nP - {i}"
        
def numeros_farmacia():
    for i in range(1, 10000):
        yield f"\nF - {i}"
        
def numeros_cosmetica():
    for i in range(1, 10000):
        yield f"\nC - {i}"
        
p = numeros_perfumeria()
f = numeros_farmacia()
c = numeros_cosmetica()


def decorar_turno(generator):
    return f"\nTurno: {next(generator)} espera en la fila 😊"
