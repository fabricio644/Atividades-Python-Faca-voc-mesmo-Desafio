nome = str(input("Qual é seu nome: "))
salario = int(input(f"{nome}, qual é seu salário: "))
vendas_totais = int(input(f"{nome}, quantas vendas você fez nesse mês: "))
bonus =  salario * 0.15
salario_total = bonus + salario

if vendas_totais >= 20:
    print(f"{nome}, você bateu a meta de 20 vendas, você recebera um bônus de R$ {bonus}, seu salario final será R$ {salario_total}")
    
else:
    print(f"{nome}, voce não bateu a meta de 20 vendas, portanto não recebera nenhum bonus, seu salario será o R$ {salario}")