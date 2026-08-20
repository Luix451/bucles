import math


class Estudiante:

    def _init_(self, nombre):
        self.nombre = nombre
        self.calificaciones = []

    def agregar_calificacion(self, nota):
        if 0 <= nota <= 100:
            self.calificaciones.append(nota)
            print("Calificación agregada correctamente.")
        else:
            print("Error: la nota debe estar entre 0 y 100.")

    def calcular_promedio(self):
        if not self.calificaciones:
            return 0

        promedio = sum(self.calificaciones) / len(self.calificaciones)
        return math.ceil(promedio)

    def estado_final(self):
        promedio = self.calcular_promedio()

        if promedio >= 60:
            return "Aprobado"
        else:
            return "Reprobado"


def main():

    print(" SISTEMA DE GESTIÓN DE CALIFICACIONES")
   

    # Pedir nombre del estudiante
    nombre = input("Ingrese el nombre del estudiante: ")

    # Crear el estudiante
    estudiante = Estudiante(nombre)

    # Agregar calificaciones
    while True:

        entrada = input(
            "Ingrese una calificación (0-100) "
            "o escriba 'fin' para terminar: "
        )

        if entrada.lower() == "fin":
            break

        try:
            nota = float(entrada)
            estudiante.agregar_calificacion(nota)

        except ValueError:
            print("Error: debe ingresar un número válido.")

  
    print("RESULTADO FINAL")
   

    print("Nombre:", estudiante.nombre)
    print("Calificaciones:", estudiante.calificaciones)
    print("Promedio:", estudiante.calcular_promedio())
    print("Estado:", estudiante.estado_final())




if __name__ == "__main__":
    main()