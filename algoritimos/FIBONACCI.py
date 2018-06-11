#FIBONACCI
print("Sequência Fibonacci em Python")
num = int(input("Quantos termos você quer mostrar?"))
t1 = 0
t2 = 1
print("%d"%t1)
print("%d"%t2)

contador = 3

while (contador <= num):
    t3 = t1+t2
    print("%d"%t3)
    t1 = t2
    t2 = t3
    contador = contador+1
print("FIM")


        
            

          
