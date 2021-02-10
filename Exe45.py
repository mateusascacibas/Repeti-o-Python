op = int(input("Digite 1 para converter KM/H para M/S, 2 se for converter M/S para KM/H e 0 para sair"))

while(op != 0):
    vel = int(input("Digite a velocidade: "))
    if(op == 1):
        cont = vel / 3.6
        print(cont)
    elif(op == 2):
        cont = vel * 3.6
        print(cont)
    else:
        print("Opção invalida")
