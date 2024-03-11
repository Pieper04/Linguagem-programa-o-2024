continua = True

while (continua):
    print("Trabalhando com adições!")
    s1 = float(input("Insira o primeiro número: "))
    s2 = float(input("Insira o segundo número: "))
    
    print(f"A soma de {s1} + {s2} é: {s1+s2}")
    
    continua = int(input("Quer continuar somando? 1 pra sim 0 para não: 5"))

print("Fim do if")