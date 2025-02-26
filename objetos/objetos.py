from typing import Any


class Memoria():

    def __init__(self):
        self.memoria = []

    def recordar(self, obj: Any) -> None:
        """
        Recuerda el objeto dado.
        """
        self.memoria.append(obj)
    
    def nombrar_objeto(self, posicion: int) -> None:
        """
        Imprime en pantalla el objeto recordado de la posicion dada.
        Si no hay un objeto en la posicion dada, imprime None.
        """
        try:
            print(self.memoria[posicion])
        except:
            print(None)
    
    def devolver_objeto(self, posicion: int) -> Any:
        """
        Devuelve el objeto en la posición dada o None.
        """
        try:
            return self.memoria[posicion]
        except:
            return None

MEMORIZADOR = Memoria()