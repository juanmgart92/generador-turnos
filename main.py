"""
En una farmacia, se necesita un programa que permita a los clientes sacar turnos para ser atendidos.
"""

import numeros

def preguntar():
    """
    Pregunta al usuario de qué área quiere el turno
    """
    
    print("Bienvenido a la farmacia 🏥")
    
    while True:
        print("\n¿De qué área quieres el turno?")
        print("1. Perfumería")
        print("2. Farmacia")
        print("3. Cosmética")
        print("4. Salir")
        
        try:
            opcion = int(input("\nOpción: "))
            if opcion == 1:
                print(numeros.decorar_turno(numeros.p))
            elif opcion == 2:
                print(numeros.decorar_turno(numeros.f))
            elif opcion == 3:
                print(numeros.decorar_turno(numeros.c))
            elif opcion == 4:
                print("\nGracias por visitarnos 😊")
                break
            else:
                print("\nOpción inválida")
        except ValueError:
            print("\nOpción inválida")
            
def inicio():
    """
    Inicia el programa
    """
    while True:
        preguntar()
        try:
            otro_turno = input("\n¿Quieres otro turno? (s/n): ").upper()
            ["S", "N"].index(otro_turno)
        except ValueError:
            print("\nOpción inválida")
        else:
            if otro_turno == "N":
                print("\nGracias por visitarnos 😊")
                break
                
inicio()
