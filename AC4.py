#AC4 
#Exercício 1

def e_primo(num):
    primo = True
    for div in range(2, num):
        if num % div == 0:
            print(div)
            primo = False

    if primo == True:
        print("Primo")
    
    else:
        print("Não é primo")
e_primo(9)

#Exercício 2

def calculo_da_divida():

    divida = float(input("Digite o valor da dívida:"))
    parcela = 1
    juros = 0

    while True:
        juros = (5 / 3) * parcela + 5
        if parcela == 14:
            juros = 0
        valor_juros = divida * (juros / 100)
        valor_final = divida + valor_juros
        valor_parcela = valor_final / parcela

        print("Valor total:", valor_final)
        print("Valor do juros", valor_juros)
        print("Parcelas:", parcela)

        if parcela == 1:
            parcela -= 1
        parcela += 3
        if parcela > 12: 
            break
calculo_da_divida()

#Exercício 3

def numeros_entre0a100():

    a = 0
    b = 0
    c = 0
    d = 0

    programa = True

    while programa == True:
        opcao = input("Deseja continuar o programa? ")
        if opcao == "N":
            programa = False
        else: 
                num = int(input("Digite um número: "))
                if num >= 0 and num <= 25:
                    a = a + 1
                elif num >= 26 and num <= 50:
                    b += 1
                elif num >= 51 and num <= 75:
                    c =+ 1
                elif num >= 76 and num <= 100:
                    d =+ 1
        

    print("Os números entre 0 e 25 são: ", a, "Entre 26 e 50 são: ", b, "Entre 51 e 75 são: ", c, "Entre 76 e 100 são: ", d,)

numeros_entre0a100()