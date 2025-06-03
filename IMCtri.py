try:

    NOME = input ("Coloque seu nome:")
    PESO = float (input("coloque o seu peso: "))
    ALTURA = float (input("coloque sua altura: "))
    RESULTADO = PESO/(ALTURA*ALTURA)

    if RESULTADO <= 18.5:
        print(f"{NOME} está Abaixo do peso,seu peso é de {PESO}Kg sua altura é de {ALTURA}M")
    elif  18.5<= RESULTADO <=24.9: 
        print(f"{NOME} está com o Peso normal,seu peso é de {PESO}Kg sua altura é de {ALTURA}M")
    elif 25.0<= RESULTADO <=29.9:
        print(f"{NOME} está com Sobrepeso,seu peso é de {PESO}Kg sua altura é de {ALTURA}M")
    elif 30.0<= RESULTADO <= 34.9:
        print(f"{NOME} está com Obesidade Grau I,seu peso é de {PESO}Kg sua altura é de {ALTURA}M")
    elif 35.0<= RESULTADO <= 39.9:
        print(f"{NOME} está com Obesidade Grau II,seu peso é de {PESO}Kg sua altura é de {ALTURA}M")
    elif 40.0<= RESULTADO:
        print (f"{NOME} está com Obesidade Grau III (mórbida),seu peso é de {PESO}Kg sua altura é de {ALTURA}M")
except:
    print ("O peso não pode ser colocado por extenso")
