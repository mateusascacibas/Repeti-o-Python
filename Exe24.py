num = int(input("Digite um numero: "))
x = 1;
soma = 0;
while(x < num):
    if(num % x == 0):
        print(x)
        soma += x
        x += 1
    else:
        x += 1

print(soma)
