n1 = int(input("Digite N1: "))
n2 = int(input("Digite N2: "))
n3 = int(input("Digite N3: "))

if(n1>n2 and n1<n3) or (n1>n3 and n1<n2):
    print("N1 é o valor do meio")
elif (n2> n1 and n2<n3) or (n2>n3 and n2<n1):
    print("N2 é o valor do meio")
elif (n3>n1 and n3<n2) or (n3>n2 and n3<n1):
    print("N3 é o valor do meio")
else:
    print("Outra situação")
