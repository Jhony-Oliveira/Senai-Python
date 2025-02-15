#ENTRADA
numero1 = float(input("Digite um numero: "))
numero2 = float(input("Digite um numero: "))
print("Qual operação você deseja?, digite: ")
print ("A - adição")
print ("S - subtração")
print ("D - divisão")
print ("M - mutiplicação")
print ("E - exponenciação")
print ("P - porcentagem")
operação = input("Qual sua escolha? ")

#PROCESSAMENTO
resultado = 0
if    (operação.upper() == "A"):
    resultado = numero1 + numero2

elif (operação.upper() == "S"):
    resultado = numero1 - numero2

elif (operação.upper() == "D"):
    resultado = numero1 / numero2

elif (operação.upper() == "M"):
    resultado = numero1 * numero2

elif (operação.upper() == "E"):
    resultado = numero1 ** numero2

elif (operação.upper() == "P"):
    resultado = (numero1 * numero2) / 100

else:
    print("OPERAÇÃO INVÁLIDA! ESCOLHA UMA OPERAÇÃO VÁLIDA!")

#SAÍDA
print("O resultado é: ",resultado)    


