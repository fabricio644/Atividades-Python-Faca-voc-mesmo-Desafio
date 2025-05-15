print("========== Conversor ==========")

temperatura_celcius = int(input("Digite a temperatura: "))

celcius_fahrenheit = (temperatura_celcius * 9) + 32
celcius_kelvin = temperatura_celcius + 273.15

print("===============================")
print("    Escolha sua temperatura    ")
print("[1] - Fahrenheit")
print("[2] - Kelvin")
print("[3] - Finalizar")
print("===============================")

esc_temp = 0

while esc_temp != 3:
    
    esc_temp = int(input("Digite para qual deseja converter: "))
    
    if esc_temp == 1:
        
        print(f"{temperatura_celcius}° para Fahrenheit = {celcius_fahrenheit}°F")
        
    if esc_temp == 2:
        
        print(f"{temperatura_celcius}° para Kelvin = {celcius_kelvin}°")
    
