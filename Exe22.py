
op = 10
vezes = 0
notas = 0

while(op >= 10 and op <= 20):
    op = float(input("Digite sua nota: "))
    vezes +=1
    notas += op
    media = notas / vezes
    print("A média é de: {} ".format(media))
