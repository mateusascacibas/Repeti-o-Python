num = int(input("Digite um numero: "))
x = 1;
while(x < num):
    if(num % x == 0):
        print(x)
        x += x
    else:
        x += x
