sair = 0
pares = 0
contador = 0

while sair != 1000:
    print("Digite um numero: ")
    num = int(input())
    if num % 2 == 0:
        print("Este numero é par ")
        pares += 1
        contador +=1
    else:
        print("Este numero não é par ")
        contador += 1
    print("Deseja sair? se sim, digite 1000, caso contrario digite qualquer outro numero.")
    sair = int(input())

print(pares)
print(contador)

