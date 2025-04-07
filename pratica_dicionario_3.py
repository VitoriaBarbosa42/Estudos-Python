while True:    
    nome = input ('Digite o seu nome: ')
    if len(nome) > 0:
        print (f'{nome} registrado')
        break
    else:
        print ('O campo não pode ficar vazio. Tente novamente!')

while True: 
    idade = input ('Digite a sua idade: ')
    if len(idade) > 0 :
        if idade.isdigit():
            print (f'{idade} registrado')
            break
        else:
            print ('Digite um valor valido')
    else:
        print ('O campo não pode ficar vazio. Tente novamente!')

while True:
    salario = input("Digite o salário: ")
    if len(salario) > 0:
        try:
            salario = float(salario)
            print("Salário registrado:", salario)
            break
        except ValueError:
            print("Digite um valor numérico válido.")

while True:
    cargo = input ('Digite o seu cargo: ')
    if len(cargo) > 0:
        print (f'{cargo} registrado')
        break
    else:
        print ('O campo não pode ficar vazio. Tente novamente!')

while True:
    endereco = input ('Digite o seu endereço: ')
    if len(endereco) > 0:
        print (f'{endereco} registrado')
        break
    else:
        print ('O campo não pode ficar vazio. Tente novamente!')

validacao = input ('Você tem dependentes? Digite [1] para sim e [2] para não: ')
  

registros_funcionario = {
    'nome' : nome,
    'idade' : idade,
    'salario' : salario,
    'cargo' : cargo,
    'endereço' : endereco
}

if validacao == '1':
    while True:
        quantidade_dependentes = int (input ('Informe a quantidade de dependentes: '))
        if quantidade_dependentes == 1:
            parentesco = input ('Digite o nome do seu dependente: ')
            nome_dependente = input ('Digite o grau de parentesco: ')
            registros_funcionario.update({'dependentes' : {quantidade_dependentes : nome_dependente}})
            print (f'Dependente {nome_dependente} adicionado')
            break
        elif quantidade_dependentes > 1:
            nome_dependente = input ('Digite o nome do seu dependente: ')
            registros_funcionario.update({'dependentes':{quantidade_dependentes : nome_dependente}})
            quantidade_dependentes -=1
            print (f'Dependente {nome_dependente} adicionado. Faltam {quantidade_dependentes}')

            while True:  
                nome_dependente = input ('Digite o nome do seu dependente: ')  
                registros_funcionario.setdefault('dependentes', {})[quantidade_dependentes] = nome_dependente
                quantidade_dependentes -=1
                print (f'Dependente {nome_dependente} adicionado. Faltam {quantidade_dependentes}')
                
                if quantidade_dependentes == 0:
                    break
            if quantidade_dependentes == 0:
                break
        else:
            print ('Quantidade invalida.')
            validacao = input ('Gostaria de tentar novamente? Digite [1] para sim e [2] para não: ')
            if validacao == '2':
                break

for chave, valor in registros_funcionario.items():
    if isinstance(valor, dict):
        print(f'{chave}:')
        for sub_chave, sub_valor in valor.items():
            print(f'  {sub_chave}: {sub_valor}')
    else:
        print(f'{chave}: {valor}')





