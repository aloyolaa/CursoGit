from Persona import Persona

persona = Persona("Alan", "Loyola")

nombre1 = input("Ingrese su nombre: ")
apellido1 = input("Ingrese su apellido: ")
persona1 = Persona(nombre1, apellido1)

print("Detalle de Personas:")
print(persona.verDetalle())
print(persona1.verDetalle())