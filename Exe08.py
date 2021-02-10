print("Digite 10 numeros. ")
numeros = range(1, 11)
soma = 0
contador = 0

for numero in numeros:

    print("Digite um numero: ")
    digitado = int(input())
    contador += 1
    if contador == 1:
        menor = digitado
        maior = digitado
    else:
        if digitado > maior:
            maior = digitado
        elif digitado < menor:
            menor = digitado
print(maior)
print(menor)

