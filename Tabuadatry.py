try:

    numero = int (input ("Qual o número que você deseja multiplicar?"))
    começo =int (input ("A partir de qual número deseja multiplicar?"))
    fim = int (input ("deseja multiplicar até qual número?"))

    for i in range(começo, fim + 1):
        print (f" {i} x {numero} = {i * numero}")
except:
    print("O número não pode ser escrito por extenso")        

    