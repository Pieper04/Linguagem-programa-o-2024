valor = 10
if valor != 0 :
    print(f"{valor} é diferente de zero => verdade.")
else:
    print(f"{valor} né igual a 0.")
    
valor = 0
if not bool(valor):
    print(f"{bool(valor)} é falso, mas not inverteu o resultado.")
    
valor = 5
valor2 = 8
if valor > valor2:
    print(f"{valor} é maior que {valor2}")
else:
    print(f"{valor} é manor que {valor2}")
    
if valor >= valor2:
    print(f"{valor} é maior ou igual que {valor2}")
else:
    print(f"{valor} é menor ou igual que {valor2}")
