contador = 0
quantidade = 0

print("Quantos numeros quer digitar? ")
num = int(input())

while contador < num:
    print("Digite: ")
    numero = int(input())
    if contador == 0:
        maior = numero
        quantidade += 1
    else:
        if numero > maior:
            maior = numero
            quantidade = 1
        elif numero == maior:
            quantidade += 1

    contador += 1

print(maior)
print(quantidade)
