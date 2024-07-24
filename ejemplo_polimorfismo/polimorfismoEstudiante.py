from abc import ABC, abstractmethod

class Estudiante(ABC):
    def __init__(self, nombres_estudiante, apellidos_estudiante, identificacion_estudiante, edad_estudiante):
        self._nombres_estudiante = nombres_estudiante
        self._apellidos_estudiante = apellidos_estudiante
        self._identificacion_estudiante = identificacion_estudiante
        self._edad_estudiante = edad_estudiante
        self._matricula = 0.0

    def establecer_nombres_estudiante(self, nom):
        self._nombres_estudiante = nom

    def establecer_apellidos_estudiante(self, ape):
        self._apellidos_estudiante = ape

    def establecer_identificacion_estudiante(self, iden):
        self._identificacion_estudiante = iden

    def establecer_edad_estudiante(self, ed):
        self._edad_estudiante = ed

    @abstractmethod
    def calcular_matricula(self):
        pass

    def obtener_nombres_estudiante(self):
        return self._nombres_estudiante

    def obtener_apellidos_estudiante(self):
        return self._apellidos_estudiante

    def obtener_identificacion_estudiante(self):
        return self._identificacion_estudiante

    def obtener_edad_estudiante(self):
        return self._edad_estudiante

    def obtener_matricula(self):
        return self._matricula


class EstudianteDistancia(Estudiante):
    def __init__(self, nombres_estudiante, apellidos_estudiante, identificacion_estudiante, edad_estudiante):
        super().__init__(nombres_estudiante, apellidos_estudiante, identificacion_estudiante, edad_estudiante)
        self._numero_asignaturas = 0
        self._costo_asignatura = 0.0

    def establecer_numero_asignaturas(self, numero):
        self._numero_asignaturas = numero

    def establecer_costo_asignatura(self, valor):
        self._costo_asignatura = valor

    def calcular_matricula(self):
        self._matricula = self._numero_asignaturas * self._costo_asignatura

    def obtener_numero_asignaturas(self):
        return self._numero_asignaturas

    def obtener_costo_asignatura(self):
        return self._costo_asignatura


class EstudiantePresencial(Estudiante):
    def __init__(self, nombres_estudiante, apellidos_estudiante, identificacion_estudiante, edad_estudiante):
        super().__init__(nombres_estudiante, apellidos_estudiante, identificacion_estudiante, edad_estudiante)
        self._numero_creditos = 0
        self._costo_credito = 0.0

    def establecer_numero_creditos(self, numero):
        self._numero_creditos = numero

    def establecer_costo_credito(self, valor):
        self._costo_credito = valor

    def calcular_matricula(self):
        self._matricula = self._numero_creditos * self._costo_credito

    def obtener_numero_creditos(self):
        return self._numero_creditos

    def obtener_costo_credito(self):
        return self._costo_credito


def main():
    estudiante_distancia = EstudianteDistancia("Juan", "Perez", "1234567890", 20)
    estudiante_distancia.establecer_numero_asignaturas(5)
    estudiante_distancia.establecer_costo_asignatura(50.0)
    estudiante_distancia.calcular_matricula()
    print(f"Nombre: {estudiante_distancia.obtener_nombres_estudiante()}")
    print(f"Apellido: {estudiante_distancia.obtener_apellidos_estudiante()}")
    print(f"Identificación: {estudiante_distancia.obtener_identificacion_estudiante()}")
    print(f"Edad: {estudiante_distancia.obtener_edad_estudiante()}")
    print(f"Matricula a Distancia: {estudiante_distancia.obtener_matricula():.2f}\n")

    estudiante_presencial = EstudiantePresencial("Maria", "Gomez", "0987654321", 22)
    estudiante_presencial.establecer_numero_creditos(4)
    estudiante_presencial.establecer_costo_credito(100.0)
    estudiante_presencial.calcular_matricula()
    print(f"Nombre: {estudiante_presencial.obtener_nombres_estudiante()}")
    print(f"Apellido: {estudiante_presencial.obtener_apellidos_estudiante()}")
    print(f"Identificación: {estudiante_presencial.obtener_identificacion_estudiante()}")
    print(f"Edad: {estudiante_presencial.obtener_edad_estudiante()}")
    print(f"Matricula Presencial: {estudiante_presencial.obtener_matricula():.2f}")


if __name__ == "__main__":
    main()
