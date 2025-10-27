
# Segundo passo: Existe a possibilidade do usuario colocar no lugar de peso uma string ao invés de float
# Tratamento de exceção

try:

# Primeira coisa a se fazer : Declaração de Variável
# entrada de dados

    nome = input("Informe o nome: ").strip().title()
    peso = float(input("Informe o peso em kg: ").strip().replace(",","."))
    altura = float(input("Informe a altura em metros: ").strip().replace(",","."))



# Terceiro passo: Cálculo do IMC
    imc = peso/(altura**2)

# Quarto passo: exibe o imc do usuário
    print(f"{nome}, seu IMC é {imc:.2f}")

# Quinto passo: 
    if imc < 18.5:
        print(f"{nome} está abaixo do peso")
    elif imc < 25:
        print(f"{nome} está no peso ideal.")
    elif imc < 30:
        print(f"{nome} está acima do peso.")
    elif imc < 35:
        print(f"{nome} está obeso.")
    elif imc < 40:
        print(f"{nome} está com obesidade nível II.")
    else:
        print(f"{nome} está com obesidade mórbida.")


# Segundo passo: Existe a possibilidade do usuario colocar no lugar de peso uma string ao invés de float
# tratamento de exceção
except Exception as e:
    print(f"Deu ruim! {e}")

# TODO: atividade
"""
Crie um programa que receba do usuário o nome, peso (em kg) e altura (em metros), calcule o IMC do usuário (arredondado para 2 casas decimais), e exiba o diagnóstico do usuário com base na tabela do IMC.
"""

''' import os
import time 

nome = input("Digite seu nome: ") 
peso = float(input("Digite seu peso em kg: ").strip().replace(",","."))
altura = float(input("Digite sua altura em metros: ").strip().replace(",","."))

os.system("cls")

# calcular IMC
imc = peso/ (altura ** 2)
imc_arredondado = round(imc, 2)

# exibir diagnóstco
print(f"Nome: {nome}")
print(f"Seu IMC é: {imc_arredondado}")

if imc < 18.5:
    print("Diagnóstico: Abaixo do peso")
elif 18.5 <= imc < 24.9:
    print("Diagnóstico: Peso normal")
elif 24.9 <= imc < 29.9:
    print("Diagnóstico: Sobrepeso")
else:
    print("Diagnóstico: Obesidade")

# mensagem de despedida
time.sleep(3)
print("\nPrograma finalizado. Volte sempre!")
'''