x = 1
soma = 0
while(x < 1000):
    if(x % 3 == 0):
        soma += x
        x += 1
    elif(x % 5 == 0):
        soma += x
        x += 1
    else:
        x += 1

print(soma)