#Cacular Fatorial
print("Calcular o fatorial de um numero:")
print("-"*400)
num = int(input("Digite um numero para calcular o seu fatorial: "))
cont = num
f = 1
while cont >0:
    print("%d"%cont, end = ' ')
    print('X ' if cont>1 else '=', end = '')
    f = f*cont
    cont = cont-1
print("%d"%f)
          
