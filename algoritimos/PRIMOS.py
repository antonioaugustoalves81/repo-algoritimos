#Numeros primos
num = int(input("Digite um numero maior que 1: "))
total = 0
for c in range(1, num+1):

    if num%c == 0:
        total = total+1
print('O número {} foi divisivel {} vezes'.format(num, total))
if total == 2:
    print("Por isso ele é primo")
else:
    print("Por isso ele não é primo")
        
            

          
