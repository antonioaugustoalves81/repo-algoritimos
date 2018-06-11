txt = input("Digite um texto: ")
quant = len(txt)
print("Numero de caracteres: %d"%quant)
copia = txt[quant-3:quant]
print("Cópia é igual a:%s"%copia.upper())

p = txt.index('@')
print("Posição: %d"%p)
