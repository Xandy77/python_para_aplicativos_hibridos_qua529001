# biblioteca
import os
import math

# limpa console
def limpar():
    os.system("cls")

# funções de cálculo
def quadrado(l):
    return l**2

def retangulo(b, h):
    return b*h

def triangulo(b, h):
    return(b*h)/2

def hipotenusa(c1, c2):
    return math.sqrt((c1**2)+(c2**2))



# TODO: Atividade: Criem uma nova função para calcular a hipotenusa do triângulo retângulo.
# NOTE: para calcular raiz quadrada, importe a biblioteca "math" e use a função "marth.sqrt()".


# algoritmo principal
limpar()

# menu
while True:
    print("1 - Calcular Quadrado")
    print("2 - Calcular Retângulo")
    print("3 - Calcular Triângulo")
    print("4 - Calcular a Hipotenusa")
    print("5 - Sair do programa")
    opcao = input("Opção desejada: ").strip()
    limpar()

    match opcao:
        case "1":
            l = float(input("Informe o lado do quadrado: ").strip().replace(",","."))
            resultado = quadrado(l)
            limpar()
            print(f"Área do quadrado: {resultado}")
            continue
        case "2":
            b = float(input("Informe a base do retângulo: ").strip().replace(",","."))
            h = float(input("Informe a altura do retângulo: ").strip().replace(",","."))
            resultado = retangulo(b, h)
            limpar()
            print(f"Área do retângulo: {resultado}")
            continue
        case "3":
            b = float(input("Informe a base do triângulo: ").strip().replace(",","."))
            h = float(input("Informe a altura do triângulo: ").strip().replace(",","."))
            resultado = triangulo(b, h)
            limpar()
            print(f"Área do triângulo: {resultado}")
            continue
        case "4":
            c1 = float(input("Informe o valor do primeiro cateto: ").strip().replace(",","."))
            c2 = float(input("Informe o valor do segundo cateto: ").strip().replace(",","."))
            resultado = hipotenusa(c1**2,c2**2)
            limpar()
            print(f"A hipotenusa é: {resultado}")
            continue
        case "5":
            break
        case _:
            print("Opção inválida.")
            continue

