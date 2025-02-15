nota = float(input("Digite uma nota:"))

# Verifica se a nota é válida (entre 0 e 10)
if nota < 0 or nota > 10:
    print("Você digitou um número inválido!")
else:
    # Verifica a situação do aluno com base na nota
    if nota >= 5:
        print("Aprovado")
    elif nota >= 3:
        print("Recuperação")
    else:
        print("Reprovado")