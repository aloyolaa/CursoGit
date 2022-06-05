from Persona import Persona

persona = Persona("Alan", "Loyola")

nombre1 = input("Ingrese su nombre: ")
apellido1 = input("Ingrese su apellido: ")
persona1 = Persona(nombre1, apellido1)

personas = [persona, persona1]

print("Detalle de Personas ciclo for:")
for p in personas:
    print(p.verDetalle())
