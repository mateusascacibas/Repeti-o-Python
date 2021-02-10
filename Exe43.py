idade = 1
media = 0
idades = 0
op = 1
while(idade > 0):
    idade = int(input("Digite a idade: "))
    idades += idade
    op += 1
media = idades / op
print("A média de idade é de: {:.2f} anos".format(media))