print("Digite 10 numeros. ")
numeros = range(1, 11)
soma = 0

for numero in numeros:
        print("Digite um numero: ")
        digitado = int(input())
        if digitado > 0:
            soma += digitado


print("A soma é de: ")
print(soma)
