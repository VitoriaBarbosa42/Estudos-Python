botao = None
lista_de_compras = []
ind = 0

while True:

    print ('Escolha uma opção ')
    botao = input ('[i]nsetir [a]pagar [l]istar [t]rocar: ').lower()

    if botao == 'i':

        while True:
            adicionar_item = input(f'Qual item gostaria de adicionar? Digite [s] se deseja voltar ao menu ').lower().strip()
            if adicionar_item == 's':
                break
            if len(adicionar_item) >= 1:
                lista_de_compras.append(adicionar_item)
                print (f'Item {adicionar_item} adicionado com sucesso')
            else:
                print('Digite um item válido')
    elif botao == 'a':
            
        while True:
            try:
                for i, item in enumerate(lista_de_compras):
                        print(i, item)
                        
                ind = int (input('Qual item gostaria de apagar? '))
                ultimo_valor = lista_de_compras.pop(ind)
                print (f'O item {ultimo_valor} foi apagado da sua lista')
                break
            except:
                print ('Indice invalido. Tente novamente')    
        
    elif botao == 't':
        while True:

            if not lista_de_compras:
                print ('a lista esta vazia')
                break

            try:
                for i, item in enumerate(lista_de_compras):
                    print(i, item)

                alterar = int (input ('Qual item da lista deseja alterar: '))
                alteracao = input ('qual item deseja acrescentar no lugar: ')
                lista_de_compras [alterar] = alteracao
                print ('Seu item foi ALTERADO com SUCESSO!')
                break
        

            except:
                sair1 = input('Item INVÁLIDO. Deseja voltar ao menu? [s/n]: ').lower()
                if sair1 == 's':
                    break
                else:
                    print('Vamos tentar novamente...')


    elif botao == 'l':
        for indice, nome in enumerate(lista_de_compras):
            print (indice, nome)
        if len(lista_de_compras) == 0:
            print ('Sua lista esta vazia')
        
        
    else:
        print('Digite um valor valido')