soma_pares = 0
soma_impares = 0

for i in range(10):
    numero = int(input(f"Digite o {i+1}° número: "))

    if(numero % 2 == 0):
        soma_pares +=numero

    else:
        soma_impares +=numero

print(f"A soma dos números pares digitados é: {soma_pares}")
print(f"A soma dos números ímpares digitados é: {soma_impares}")