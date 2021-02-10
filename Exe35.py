n1 = int(input("Digite o primeiro numero: "))
n2 = int(input("Digite o segundo numero: "))
diferença  = 0
if(n1 > n2):
    print("Digite uma diferença inválida.")
else:
    if(n1 % 2 == 0):
        n1 = n1 + 1

    while (n1 <= n2):
        diferença = diferença + n1
        n1 += 2

print("A soma da diferença é de: {}".format(diferença))