nota1 = float(input("Digite a primeira nota: "))

nota2 = float(input("Digite a segunda nota: "))

nota3 = float(input("Digite a terceira nota: "))

nota4 = float(input("Digite a quarta nota: "))

media_aritimetica = (nota1 + nota2+ nota3 +nota4)/4

print(f"A média aritimética das notas é: {media_aritimetica}")

if(media_aritimetica <5):
    print("Aluno reprovado")
elif(media_aritimetica <6):
    print("Aluno em recuperação")
else:
    print("Aluno aprovado")