# -*- coding: utf-8 -*-

# --Trabalhando com Strings-- Fatiamento de strings

nome = input("Digite o seu primeiro nome.:")
print(nome.capitalize())#primeira letra maiuscula
print(nome.center(40))#centraliza com espaços a direita e a esquerda
print(nome.count('e'))#quantas letras o existem
print("Termina com io? ",nome.endswith("io"))#termina com io?
print("Parte da String.: ", nome[0:4])#fatiamento
print("Comando find.: ", nome.find("e"))#busca uma substring dentro do texto
print("Comando find.: ", nome.find("n",1))#busca uma substring dentro do texto
print("Comando find.: ", nome.find("n",4,6))#busca uma substring dentro do texto
print("Index.:", nome.index("f"))#Busca a posição da primeira ocorrencia - Geera uma exceção