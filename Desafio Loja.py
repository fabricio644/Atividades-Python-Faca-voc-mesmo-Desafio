print("========== Fast Burguer ==========")
print(" ")    
print("[1] - Misto quente | R$ 7,50")
print("[2] - Pizza Frango c/ catupiry | R$ 20,00")
print("[3] - Batata frita com bacon | R$ 18,00")
print("[4] - Macarrão com queijo | R$ 15,00")
print("[5] - Finalizar pedido")
print(" ")    
print("==================================")

escolha = 0
quantidade = 0
final = 0

qtd_misto = 0
qtd_pizza = 0
qtd_batata = 0
qtd_macarrao = 0

valor_misto = 7.50
valor_pizza = 20
valor_batata = 18
valor_macarrao = 15

valor_misto_final = 0
valor_pizza_final = 0
valor_batata_final = 0
valor_macarrao_final = 0

while escolha != 5:
    
    escolha = int(input("Escolha o número do cardápio: "))
    
    if escolha == 1:
        
        quantidade = int(input("Digite a quantidade do Misto: "))
        qtd_misto = quantidade + qtd_misto
        valor_misto_final = qtd_misto * valor_misto
        print(f"[1] - Misto quente | QT: {qtd_misto} | R$ {valor_misto_final:.2f}")
        
    if escolha == 2:
        
        quantidade = int(input("Digite a quantidade da Pizza Frango c/ catupiry: "))
        qtd_pizza = quantidade + qtd_pizza
        valor_pizza_final = qtd_pizza * valor_pizza
        print(f"[2] - Pizza Frango c/ catupiry | QT: {qtd_pizza} | R$ {valor_pizza_final:.2f}")
        
    if escolha == 3:
        
        quantidade = int(input("Digite a quantidade da Batata frita com bacon: "))
        qtd_batata = quantidade + qtd_batata
        valor_batata_final = qtd_batata * valor_batata
        print(f"[3] - Batata frita com bacon | QT: {qtd_batata} | R$ {valor_batata_final:.2f}")
        
    if escolha == 4:
        
        quantidade = int(input("Digite a quantidade do Macarrão com queijo: "))
        qtd_macarrao = quantidade + qtd_macarrao
        valor_macarrao_final = qtd_macarrao * valor_macarrao
        print(f"[4] - Macarrão com queijo | QT: {qtd_macarrao} | R$ {valor_macarrao_final:.2f}")
        
    if escolha == 5:
        
        print("Obrigado por pedir no Fast Burguer :)")
        print(" ")
      
print("========== Nota Fiscal ==========")
print(" ")

final = valor_misto_final + valor_pizza_final + valor_batata_final + valor_macarrao_final

if qtd_misto > 0:
    
    print(f"[1] - Misto quente | QT: {qtd_misto} | R$ {valor_misto_final:.2f}")
    
if qtd_pizza > 0:
    
    print(f"[2] - Pizza Frango c/ catupiry | QT: {qtd_pizza} | R$ {valor_pizza_final:.2f}")
    
if qtd_batata > 0:
    
    print(f"[3] - Batata frita com bacon | QT: {qtd_batata} | R$ {valor_batata_final:.2f}")
    
if qtd_macarrao > 0:
    
    print(f"[4] - Macarrão com queijo | QT: {qtd_macarrao} | R$ {valor_macarrao_final:.2f}")
    
print(" ")    
print("=================================")
print(f"Total | R$ {final:.2f}")
print("=================================")
    
     
    