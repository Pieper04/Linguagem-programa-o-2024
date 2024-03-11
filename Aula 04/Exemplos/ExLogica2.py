pares = 0
for cont in range(5):
    num = int(input("Digite um número: "))
    if num % 2 == 0:
        pares += 1
print(f"Quantidade de números pares digitados: {pares}")