op = 1
soma = 0
quantidade = 0
media = 0
pares = 0
np = 0
media_par = 0


while(op != 0):
    op = int(input("Digite um numero: "))
    if(quantidade == 0):
        maior = op
        menor = op
    else:
        if(op > maior):
            maior = op
        elif(op < menor):
            menor = op

    if(op % 2 == 0):
        pares += 1
        np += op
        media_par = np / pares

    soma += op
    quantidade += 1
    media = soma / quantidade

    print("O maior numero é {} ".format(maior))
    print("O menor numero é {} ".format(menor))
    print("A média é {:.2f} ".format(media))
    print("A média de numeros pares é {:.2f} ".format(media_par))
    print("A quantidade de numeros digitados foi {} ".format(quantidade))
    print("A soma dos digitados é {} ".format(soma))

