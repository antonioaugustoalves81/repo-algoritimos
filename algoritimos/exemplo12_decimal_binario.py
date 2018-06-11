#Funções Matematicas
numero = int(input("Forneça um número"))
quantasDivisões = 0
binário = "" 
while numero > 0 : 
  quantasDivisões += 1
  print(numero,"dividido por 2 dá",numero//2,"resta",numero%2)
  numero = numero // 2
  binário = str(numero%2) + binário
print("Deu",quantasDivisões,"divisões")

          
