# -*- coding: utf-8 -*-

# --Trabalhando com Strings-- Fatiamento de strings

nome = "Antonio"
sobre = "Alves"
nomeCompleto = nome+" "+sobre
idade = 36
salario = 1000
print(" Funcionário:", nomeCompleto, "\n Idade: ",idade, "\n Salario:", salario) 
print("-"*30)
print("Com composição: ")
print("-"*30)

print("Funcionário: %s \nIdade: %d \nSalario:%f"%(nome, idade,salario))
print("Funcionário: %s \nIdade: %d \nSalario:%5.2f"%(nome, idade,salario))