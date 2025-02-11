
print ("Bem vindo(a) ao game")
print ("Digite uma letra para adivinhar qual palavra estamos escondendo:")
print ("Você tem 7 tentativas")
print ("-----------------------------------------------------------------")
senha = "caverna"
adivinha = ""
repeticao = 0

for adivinha in senha:
    
    adivinha = input ("Digite uma letra: ")
    adivinha = str.lower(adivinha)
    repeticao += 1

    if adivinha in senha:
        print (f"A letra {adivinha} esta na palavra secreta. Tentativa num {repeticao}")
    else:
        print (f'Letra {adivinha} não esta na palavra. Tentativa {repeticao}')
    
    if repeticao >= 7:
        print ("numero de tentativas acabou")
        adivinha = input ("Digite a palavra correta: ")
        if adivinha == senha:
            print ("PARABENS!!! VOCÊ GANHOU!!!")
        else:
            print ("Não foi dessa vez")
