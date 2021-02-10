import random
n1 = 0
rand = random.randint(1,1000)

while(n1 != rand):  
    n1 = int(input("Digite um numero: "))

    if(n1 < rand):
        print("O numero que você digitou é menor.")
    elif(n1 > rand):
        print("O numero que você digitou é maior.")
    else:
        print("Parabens, acertou.")