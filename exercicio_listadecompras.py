comandos = ('i', 'a', 'l', 't', 's')
n1, n2, n3, n4, n5 = comandos
print (n1)
botao = 'n'
lista_de_compras = []
i = 0
item_apagar = True

while True:

    print ('Escolha uma opção')
    botao = input ('[i]nsetir [a]pagar [l]istar [t]rocar: ')
    botao.lower().startswith('ialt')
    item_apagar = True

    if botao in n1:

        while item_apagar:
            item = input(f'Qual item gostaria de adicionar? Digite [{n5}] se deseja voltar ao menu ')
            item.lower
            sair = item == n5
            if sair == False:
                print (f'Item {item} adicionado com sucesso')
                lista_de_compras.append(item)
                
            if sair:
                item_apagar = False
    elif botao in n2:
            
        while item_apagar:
            try:
                i = int (input('Qual item gostaria de apagar? '))
                ultimo_valor = lista_de_compras.pop(i)
                print (f'O item {ultimo_valor} foi apagado da sua lista')
                item_apagar = False
            except:
                print ('Indice invalido. Tente novamente')    
        
    elif botao in n4:
            while item_apagar:

                try:
                    alterar = int (input ('Qual item da lista deseja alterar: '))
                    alteracao = input ('qual item deseja acrescentar no lugar: ')
                    lista_de_compras [alterar] = alteracao
                    item_apagar = False
                    print ('Seu item foi ALTERADO com SUCESSO!')

                except:
                    print ('Item INVALIDO, tente novamente.')

    elif botao in n3:
        for indice, nome in enumerate(lista_de_compras):
            print (indice, nome)
        
    else:
        print('Digite um valor valido')