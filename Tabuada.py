contador = 1
tabuada = 2 
resultado = 0

while resultado < 100:
    resultado = tabuada * contador

    print(tabuada, "x" ,contador, "=" ,resultado)
    contador += 1
             
    if contador > 10:  
        tabuada += 1  
        contador = 1
        print("")

    
print("Final da Tabuada")




