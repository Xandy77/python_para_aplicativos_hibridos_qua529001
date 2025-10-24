# TODO: atividade
"""
Crie um programa que receba um número inteiro do usuário, e mostre uma contagem em regressiva em segundos, e ao terminar, exiba uma mensagem qualquer.
"""

import os
import time

try:
    numero = int(input("Informe o numero: ").strip())
    os.system("cls")

    while numero >= 0: # bloco de programaação precisa de "":"" no final
        time.sleep(1)
        print(numero)
        time.sleep(1)
        numero -= 1
        os.system("cls")

    print("Contagem regressiva finalizada!")
    
except:
    print()