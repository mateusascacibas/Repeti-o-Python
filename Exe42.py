import math

op = 1

while(op > 0):
    op = int(input("Digite um numero: "))
    print("O quadrado é: {} ".format(op*op))
    print("O cubo é: {} ".format(op*op*op))
    print("A raiz quadrada é: {} ".format(math.sqrt(op)))
