botao = None
lista_de_compras = []
ind = 0
item_apagar = True

while True:

    print ('Escolha uma opção ')
    botao = input ('[i]nsetir [a]pagar [l]istar [t]rocar: ').lower()
    item_apagar = True

    if botao == 'i':

        while item_apagar:
            item = input(f'Qual item gostaria de adicionar? Digite [s] se deseja voltar ao menu ')
            item.lower
            sair = item == 's'
            if sair == False and len(item) >= 1:
                print (f'Item {item} adicionado com sucesso')
                lista_de_compras.append(item)
                
            if sair:
                item_apagar = False
    elif botao == 'a':
            
        while item_apagar:
            try:
                for i, item in enumerate(lista_de_compras):
                        print(i, item)
                        
                i = int (input('Qual item gostaria de apagar? '))
                ultimo_valor = lista_de_compras.pop(i)
                print (f'O item {ultimo_valor} foi apagado da sua lista')
                item_apagar = False
            except:
                print ('Indice invalido. Tente novamente')    
        
    elif botao == 't':
            while item_apagar:

                try:
                    for i, item in enumerate(lista_de_compras):
                        print(i, item)

                    alterar = int (input ('Qual item da lista deseja alterar: '))
                    alteracao = input ('qual item deseja acrescentar no lugar: ')
                    lista_de_compras [alterar] = alteracao
                    item_apagar = False
                    print ('Seu item foi ALTERADO com SUCESSO!')
            

                except:
                    print ('Item INVALIDO, tente novamente.')
                    print (lista_de_compras)
                    sair1 = input ('Caso queira voltar ao menu digite "s" caso contrario digite "n": ').lower
                    if sair1 == 's':
                        item_apagar = False


    elif botao == 'l':
        for indice, nome in enumerate(lista_de_compras):
            print (indice, nome)
        if len(lista_de_compras) == 0:
            print ('Sua lista esta vazia')
        
        
    else:
        print('Digite um valor valido')