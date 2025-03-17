while True:
    cpf = input ('Digite o CPF que gostaria de validar: ')
    print (f'O CPF "{cpf}" esta correto?')
    confirmacao = input ('[s]im - [n]ão --- [sair] se quiser encerrar o programa ').lower()
    cpf = cpf.replace('.', '').replace('-', '').replace(',', '')
    soma_cpf1 = 0
    soma_cpf2 = 0
    n_multiplicador1 = 10
    n_multiplicador2 = 11
    digitos_int_cpf = []


    if confirmacao == 's':

        cpf_numero_repetido = cpf == cpf [0] * len(cpf)
        if len(cpf) == 11 and cpf.isdigit() and cpf_numero_repetido == False:
            for i in cpf[:9]:
                digitos_int_cpf.append (int(i))

            for i in digitos_int_cpf:
                soma_cpf1 += i * n_multiplicador1 
                n_multiplicador1 -= 1
            
            validacao1 = (soma_cpf1 * 10) % 11
            if validacao1 > 9:
                validacao1 = 0
                
            digitos_int_cpf.append(validacao1)

            for i in digitos_int_cpf:
                soma_cpf2 += i * n_multiplicador2
                n_multiplicador2 -= 1
                
            validacao2 = (soma_cpf2 * 10) % 11
            if validacao2 > 9:
                validacao2 = 0
            
            digito1 = int (cpf[9])
            digito2 = int (cpf[10])

            if validacao1 == digito1 and validacao2 == digito2:
                print ('o cpf é valido')
            else:
                print ('o cpf é invalido')

        else:
            print ('Digite um valor valido')

    elif confirmacao == 'sair':
        print ('Volte sempre :)')
        break
    else:
        print ('Tente novamente')
