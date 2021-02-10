base = float(input("Digite a base: "))
altura = float(input("Digite a altura: "))

if(base <= 0 or altura <= 0):
    print("Erro.")
else:
    area = (base * altura) / 2
    print("A Area do triangulo é de {} ".format(area))