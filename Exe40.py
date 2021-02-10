op = 1
cont = 1
maior = 0
menor =  0
while(op >= 0):
    op = int(input("Digite um  numero: "))
    if(cont == 1):
        maior = op
        menor = op
    elif(op > maior):
        maior = op
    elif(op < menor):
        if(op > 0):
            menor = op

    cont += 1

print("O maior numero digitado foi o {} e o menor foi o {} ".format(maior,menor))