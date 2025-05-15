km_pecorrido = float(input("Quantos KM você pecorreu: "))
dias_alugado = int(input("Quantos dias você alugou o carro: "))

soma_total = (dias_alugado * 90) + (km_pecorrido * 0.20)

print("========== NOTA FISCAL ==========")
print(" ")
print(f"[1] - KM = R$ {(km_pecorrido * 0.20)}")
print(f"[2] - DIAS = R$ {(dias_alugado * 90)}")
print(" ")
print("=================================")
print(f"TOTAL = R$ {soma_total}")
print("=================================")

