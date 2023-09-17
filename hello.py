#!/nix/store/zdba9frlxj2ba8ca095win3nphsiiqhb-python3-3.10.8/bin/python3
"""Hello World Multi Línguas

Dependendo da linguagem configurada no ambiente, o programa exibe a mensagem correspondente

Como usar:

Tenha a variável LANG devidamente configurada ex:

  export LANG=pt_BR

Execução:
  python3 hello.py
  ou
  ./hello.py
"""
__version__ = "0.0.1"
__author__ = "Cláudio"
__license__ ="Unlicense"

import os

current_language = os.getenv("LANG", "en_US")[:5]

message = "Hello, World!"

if current_language == "pt_BR":
  message = "Olá, Mundo!"
elif current_language == "it_IT":
  message = "Ciao, Mondo!"
elif current_language == "es_SP":
  message = "Hola, Mundo!"
elif current_language == "fr_FR":
  message = "Bonjour, Mondo!"

print(message)