## nome do usuario 
nome = input("Digite o seu nome: ")


##  Qual o seu salario mensal.
salario = input("Digite o seu salario mensal :")
salario_num = float(salario)


## Qual o valor do seu bonus ?
bonus = input("Digite o valor do seu bonus: ")
bonus_num = float(bonus)


## adicional recebido
adicional = input("Qual o valor do seu bonus recebido: ")
adicional_num = float(adicional)


salario_final = salario_num * bonus_num + adicional_num
print(f"O usuario {nome} possui o salario total de R$ {salario_final}")