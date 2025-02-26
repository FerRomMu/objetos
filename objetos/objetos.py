from typing import Any

class Calculadora():
    def sumar(self, n: int, n2: int) -> int:
        """
        Necesito 2 números. Respondo con la suma de esos dos números.
        """
        return n + n2
    
    def resta(self, n: int, n2: int) -> int:
        """
        Necesito 2 números. Respondo con la resta de esos dos números.
        """
        return n - n2
    
    def multiplicar(self, n: int, n2: int) -> int:
        """
        Necesito 2 números. Respondo con la multiplicacion de esos dos números.
        """
        return n * n2
    
    def el_mayor_entre(self, n: int, n2: int) -> int:
        """
        Necesito 2 números. Respondo con el número que es mayor.
        """
        return n if n > n2 else n2
    
    def saluda_al_alumno(self) -> None:
        print("""Hola soy la calculadora. Yo puedo hacer cuentas y decirte cual es el número mayor.
              Los mensajes que entiendo son:
              - sumar: Sumo 2 números.
              - restar: Resto 2 números.
              - multiplicar: Multiplico 2 números.
              - el_mayor_entre: Te digo cual es el número mas grande entre los dos que me des.""")
        
class Solicitador:
    def pedir_numero(self):
        """Solicito un número al usuario, validando que me de un número."""
        while True:
            entrada = input("Por favor, ingrese un número:")
            if entrada.isdigit():
                return int(entrada)
            print("Entrada inválida. Por favor, ingrese un número válido.")

    def pedir_texto(self):
        """Solicito una cadena de texto al usuario."""
        return input("Por favor, ingrese un texto:")

    def saluda_al_alumno(self) -> None:
        print("""Hola. Soy un objeto encargado de pedirle cosas al usuario del programa.
              Los mensajes que entiendo son:
              - pedir_numero: Donde le pediré un número al usuario.
              - pedir_text: Donde le pediré un texto al usuario.
        """)

class Memoria():

    def __init__(self):
        self.memoria = []

    def recordar(self, obj: Any) -> None:
        """
        Recuerdo el objeto que me das.
        """
        self.memoria.append(obj)
    
    def nombrar_objeto(self, posicion: int) -> None:
        """
        Imprimo en pantalla el objeto recordado en el orden dado.
        Si no hay un objeto en la posicion dada, imprimo None.
        """
        try:
            print(self.memoria[posicion-1])
        except:
            print(None)
    
    def devolver_objeto(self, posicion: int) -> Any:
        """
        Devuelvo el objeto en la posición dada o None.
        """
        try:
            return self.memoria[posicion-1]
        except:
            return None
    
    def saluda_al_alumno(self) -> None:
        print("Hola. Soy un objeto que sabe memorizar y mostrar cosas memorizadas. Podes hablarme diciendo: recordar(algo a recordar), nombrar_objeto(un numero de orden) o devolver_objeto(un numero de orden).")

class AnalizadorTexto:
    def contar_palabras(self, texto) -> int:
        """Cuento la cantidad de palabras en el texto. Necesito un String."""
        return len(texto.split())
    
    def palabra_mas_larga(self, texto: str) -> str:
        """Te respondo con la palabra mas larga del texto. Necesito un String con el texto."""
        palabras = texto.split()
        if not palabras:
            return ""
        return max(palabras, key=len)
    
    def cantidad_de_letras(texto: str) -> int:
        """Te respondo con la cantidad de caracteres que hay en el texto (contando incluso los espacios). Necesito un String del texto."""
        return len(texto)
    
    def saluda_al_alumno(self) -> None:
        print("""Hola! Soy el analizador de textos. Podes pedirme que cuente palabras u obtenga la palabra mas larga de un texto. Yo se responder a:
              - contar_palabras: Donde necesito que me des un texto y te digo cuantas palabras tiene.
              - palabra_mas_larga: Donde te doy la palabra mas larga del texto.
              - cantidad_de_letras: Donde te digo cuantos caracteres tiene el texto.""")

MEMORIZADOR = Memoria()
ANALIZADOR_TEXTO = AnalizadorTexto()
CALCULADORA = Calculadora()
SOLICITADOR = Solicitador()