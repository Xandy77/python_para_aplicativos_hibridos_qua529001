# declaração de dicionario
usuario =  {
    'nome': "Valdomiro Pereira",
    'nascimento': "15/01/1984",
    'email': "xandnho2017@gmail.com",
    'telefone': "(61)985865761",
    'endereço': "Campo da Esperança"
}

for chave in usuario:
    print(f"\n{chave.capitalize()}: {usuario[chave]}\n")