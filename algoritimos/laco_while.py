idade = 0;
c1 = 0
c2 = 0
total = 0
soma = 0
while idade >=0:
    idade = int(input("Digite a Idade:"))
    if idade >=18:
        c1 +=1
    elif idade >=0 and idade < 18:
        c2+=1
    total +=1
    soma = soma+idade
print("Maiores de idade:%d"%c1)
print("Menores de idade:%d"%c2)
print("Média das Idades:%f"%(soma/(total-1)))
print("Total:%d"%(total-1))
