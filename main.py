#!/usr/bin/python3

"""
WORDPY

Versión de consola del juego WORDLE escrito en Python3

Planes:
    * Posibilidad de no colorear una letra si no está repetida y ya se maró
      una en su posición correcta.
    * ¿Agregar verbos conjugados al diccionario?
    * ¿Agregar la posibilidad de iniciar el juego con argumentos desde consola?
"""


from random import choice

class colors:
    """
    Clase utilizada para colorear 
    """

    reset = '\033[0m'
    bold = '\033[01m'
    disable = '\033[02m'
    underline = '\033[04m'
    reverse = '\033[07m'
    strikethrough = '\033[09m'
    invisible = '\033[08m'

    class fg:
        black = '\033[30m'
        red = '\033[31m'
        green = '\033[32m'
        orange = '\033[33m'
        blue = '\033[34m'
        purple = '\033[35m'
        cyan = '\033[36m'
        lightgrey = '\033[37m'
        darkgrey = '\033[90m'
        lightred = '\033[91m'
        lightgreen = '\033[92m'
        yellow = '\033[93m'
        lightblue = '\033[94m'
        pink = '\033[95m'
        lightcyan = '\033[96m'

    class bg:
        black = '\033[40m'
        red = '\033[41m'
        green = '\033[42m'
        orange = '\033[43m'
        blue = '\033[44m'
        purple = '\033[45m'
        cyan = '\033[46m'
        lightgrey = '\033[47m'


class JUEGO:
    def __init__(self, tam_palabra=5, intentos=6, archivo_palabras="spanish.lst", validar_palabras=True):
        self.tam_palabras = tam_palabra
        self.lista_palabras = self.cargar_palabras(archivo_palabras)
        self.intentos = intentos
        self.palabra = choice(self.lista_palabras)
        self.tablero = []
        self.validar_palabras = validar_palabras


    def cargar_palabras(self, archivo_palabras):
        # Leer archivo con lista de palabras para el juego
        with open(archivo_palabras) as archivo:
            lista_completa = archivo.readlines()

        # Armar lista con solo las palabras que tengan la longitud especificada
        # y quitar el caracter del salto de linea al final de cada palabra con ([0:-1])
        lista_palabras = []
        for i in lista_completa:
            if len(i) == (self.tam_palabras + 1):
                lista_palabras.append(i[0:-1])

        return lista_palabras


def in_word(juego):
    """
    Rutina para el ingreso y validación de las palabras
    """
    palabra = ""
    while True:
        palabra = input(f"Palabra de {juego.tam_palabras} caracteres: ").lower()

        # La palabra tiene una longitud incorrecta
        if (len(palabra) != juego.tam_palabras):
            print("\nPalabra de longitud incorrecta.")
            continue

        # Si no hace falta validar las palabras en el diccionario : salir del bucle
        if not juego.validar_palabras:
            break

        # Si la palabra no se encuentra en el diccionario
        if palabra not in juego.lista_palabras:
            print("\nPalabra desconocida!")
            continue

        # La palabra sorteo los filtros y es correcta : salir del bucle
        break

    return palabra


def game_loop(juego):
    while True:
        # Mostrar mensaje con el estado del juego
        print(f"Intentos: {juego.intentos - len(juego.tablero)}")

        # Ingresar una palabra
        palabra = in_word(juego)
        juego.tablero.append(palabra)

        # Mostrar el tablero con las palabras 'intentadas'
        print() # espacio antes del tablero
        for i in juego.tablero:
            print(colorear_palabra(i, juego.palabra))

        # Verificar si la palabra es la correcta y salir del juego
        if palabra == juego.palabra:
            print(colors.bg.green + "\nGanaste!" + colors.reset)
            return()

        # Exediste el número de intentos
        if len(juego.tablero) >= juego.intentos:
            print(colors.bg.orange + "\nPerdiste!" + colors.reset)
            print(f"la palabra era: {juego.palabra}")
            return()


def colorear_palabra(intento, original):
    """
    Colorear palabra del intento según las reglas de wordle teniendo en cuenta
    la palabra original
    """
    palabra_coloreada = ""
    for i in range(len(original)):
        li = intento[i]
        lo = original[i]
        if li in original:
            if li == lo:
                colorletra = colors.bg.green + colors.fg.black
            else:
                colorletra = colors.bg.orange + colors.fg.black
        else:
            colorletra = colors.bg.lightgrey + colors.fg.black
        palabra_coloreada += colors.bold + colorletra + " " + li + " " + colors.reset

    return palabra_coloreada


def wordpy():
    # Tamaño de las palabras
    size_word = 5
    # Utilizando QPython3 en android es necesario especificar la ruta del archivo
    archivo = "/storage/emulated/0/qpython/projects3/pydle/spanish.lst"

    juego = JUEGO(
        tam_palabra=5,
        intentos=6,
        archivo_palabras="spanish.lst",
        validar_palabras=True
    )

    # Iniciar el juego
    print("\nnota: Los verbos están en infinitivo\n")
    game_loop(juego)
    print("Fin del juego")
    quit()


wordpy()