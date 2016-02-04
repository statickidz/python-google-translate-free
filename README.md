# python-google-translate-free
Simple Python class for talking to Google's Translate API for free.

# Usage
```python
# coding=utf-8
from lib.translator import GoogleTranslate as translator

translation = translator.translate("es", "en", "Esto es una prueba")

print translation # output: This is a test
```
