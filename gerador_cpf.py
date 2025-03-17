import random

while True:

    print ('Bem vindo ao GERADOR DE CPF :)')
    print ('----------------------------------------------------------')
    sair = input ('Aperte [1] para gerar um novo CPF [2] para sair: ')


    if sair == '1':
        base_cpf = random.choices(range(10), k=9)
        digito_mul1 = 10
        soma_digito1 = 0

        for i in base_cpf:
            soma_digito1 += i * digito_mul1
            digito_mul1 -= 1
        digito1 = (soma_digito1*10) % 11

        if digito1 > 9: digito1 = 0

        base_cpf.append(digito1)
        digito_mul2 = 11
        soma_digito2 = 0

        for i in base_cpf:
            soma_digito2 += i * digito_mul2
            digito_mul2 -= 1

        digito2 = (soma_digito2*10) % 11
        if digito2 > 9: digito2 = 0

        base_cpf.append(digito2)

        cpf_str = [str(digito) for digito in base_cpf]

        cpf_formatado = (
            ''.join(cpf_str[0:3]) + '.' +
            ''.join(cpf_str[3:6]) + '.' +
            ''.join(cpf_str[6:9]) + '-' +
            ''.join(cpf_str[9:])
        )
        print("Novo CPF: ", cpf_formatado)
        print()
    elif sair == '2':
        print ('Até a próxima :)')
        break

    else:
        print ('Não identifiquei o que gostaria. Por favor, tente novamente')
