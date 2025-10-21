nome = input("Informe o nome: ").strip().title()
idade = int(input("Informe a sua idade: ").strip())
altura = float(input("Informe a altura: ").strip().replace(",","."))

#verificação das condições
if idade >= 12 and altura >= 1.15:
    print(f"Entrada de {nome} autorizada")
else:
    print(f"Entrada de {nome} não autorizada")