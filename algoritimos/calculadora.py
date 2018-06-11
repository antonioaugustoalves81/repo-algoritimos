print("*** CALCULADORA PYTHON          ***")
print("*** digite 1 para soma          ***")
print("*** digite 2 para subtração     ***")
print("*** digite 3 para multiplicação ***")
print("*** digite 4 para divisão       ***")
print("*** digite 0 para sair          ***")

operacao = "";
v1 = 0
v2 = 0
resultado = 0
while operacao != "0":
    n1 = float(input("digite o primeiro numero: "))
    n2 = float(input("digite o segundo valor: "))
    operacao = input("Digite a operação desejada: ")

    if operacao == "1":
        resultado = v1+v2
        print("Resultado = %f"%resultado)
    elif operacao == "2":
        resultado = v1-v2
        print("Resultado = %f"%resultado)
    elif operacao == "3":
        resultado = v1*v2
        print("Resultado = %f"%resultado)
    elif operacao == "4":
        resultado = v1/v2
        print("Resultado = %f"%resultado)
    else:
        print("Opção inválida.")
        
    
