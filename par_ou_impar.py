numero = input ("Digite um numero inteiro ")

try:
    numero.isdigit
    numero_int = int(numero)
    if numero_int % 2 == 0:
            print ("Seu numero e par")
    else:
            print ("Seu numero e impar")
except:
    print ("O numero digitado nao e inteiro")
