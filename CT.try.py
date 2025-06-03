try:
    Temperatura = float (input("Digite a temperatura em celsius: "))

    if Temperatura >= 30:
        print("☀️ Está quente☀️")
    elif Temperatura >= 20: 
        print("🌄Está agradável🌄")    
    elif Temperatura >= 10:
        print ("❄️Está frio!❄️")    
    else:
        print("🥶 Está muito frio!!!🥶")   
except:
    print ("A temperatura não pode ser escrita por extenso")










 