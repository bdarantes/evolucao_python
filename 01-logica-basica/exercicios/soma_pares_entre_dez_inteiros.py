soma =0

for i in range(10):
    numero = int(input(f"Digite o {i+1}° número: "))

    if(numero % 2 ==0):
        soma +=numero
print(f"A soma dos dez números pares é: {soma}")