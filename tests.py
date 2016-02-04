# coding=utf-8
from lib.translator import GoogleTranslate as translator

translation = translator.translate(
    "es", "fr", "Esto es una prueba con acentos de médico que tiene que funcionar. De lo contrario habrá que cambiar la clase.")

print translation