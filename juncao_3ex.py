horas = input ("Qual horas são desse modo xx:xx : ")
horas_c = float (horas.replace(":","."))
nome = input ("Digite seu primeiro nome: ")


bom_dia = (horas_c >=00.00) and (horas_c <= 11.59)
boa_tarde = (horas_c >= 12.00) and (horas_c <= 18.59)
boa_noite = (horas_c >= 19.00) and (horas_c <= 23.59)


if bom_dia:
    print (f'Bom dia ', nome)
elif boa_tarde:
    print (f'Boa tarde ',nome)
elif boa_noite:
    print (f'Boa noite ', nome)
else:
    print ("Você não digitou o horario ")


if  nome.isalpha():
    quantidade_letras = len(nome)

    if quantidade_letras <= 4:
        print ("Seu nome é pequeno")
    elif quantidade_letras == 5 or quantidade_letras == 6:
        print ("Seu nome é normal")
    else:
        print ("Seu nome é muito grande")
else:
    print ("Você nao digitou um nome")

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