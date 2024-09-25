from abc import ABC, abstractmethod


class Publicacion(ABC):

    @abstractmethod
    def informacion(self):
        pass

    @abstractmethod
    def resumen(self):
        pass

    def __init__(self, informacion, resumen):
        self._informacion = informacion
        self._resumen = resumen

    def __str__(self):
        return f"{self.informacion()}, {self.resumen()}"


class Libro(Publicacion):
    def __init__(self, informacion, resumen):
        super().__init__(informacion, resumen)

    def informacion(self):
        return f"Este es un libro: {self._informacion}"

    def resumen(self):
        return f"Resumen del libro: {self._resumen}"


class libro(Publicacion):
    def __init__(self, informacion, resumen):
        super().__init__(informacion, resumen)

    def informacion(self):
        return f"Esta es un libro: {self._informacion}"

    def resumen(self):
        return f"Resumen del libro: {self._resumen}"


# Crear instancias de libro y Libro con los parámetros correctos
libro1 = libro("libro de caballos", "Lo último en tendencias de moda")
libro1 = Libro("El amor eterno por tu caballo", "como querer tu caballo")

# Imprimir información y resumen de las instancias
print(libro1)
print(libro1)