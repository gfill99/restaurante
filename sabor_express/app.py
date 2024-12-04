import os

restaurantes = [{'nome':'Praça', 'categoria':'Japonesa', 'ativo':False},{'nome':'Pizza Suprema', 'categoria':'Pizza', 'ativo':True},{'nome':'Cantina', 'categoria':'Italiana', 'ativo':False}]

def exibir_nome_do_programa():
    print("""
░██████╗░█████╗░██████╗░░█████╗░██████╗░  ███████╗██╗░░██╗██████╗░██████╗░███████╗░██████╗░██████╗
██╔════╝██╔══██╗██╔══██╗██╔══██╗██╔══██╗  ██╔════╝╚██╗██╔╝██╔══██╗██╔══██╗██╔════╝██╔════╝██╔════╝
╚█████╗░███████║██████╦╝██║░░██║██████╔╝  █████╗░░░╚███╔╝░██████╔╝██████╔╝█████╗░░╚█████╗░╚█████╗░
░╚═══██╗██╔══██║██╔══██╗██║░░██║██╔══██╗  ██╔══╝░░░██╔██╗░██╔═══╝░██╔══██╗██╔══╝░░░╚═══██╗░╚═══██╗
██████╔╝██║░░██║██████╦╝╚█████╔╝██║░░██║  ███████╗██╔╝╚██╗██║░░░░░██║░░██║███████╗██████╔╝██████╔╝
╚═════╝░╚═╝░░╚═╝╚═════╝░░╚════╝░╚═╝░░╚═╝  ╚══════╝╚═╝░░╚═╝╚═╝░░░░░╚═╝░░╚═╝╚══════╝╚═════╝░╚═════╝░
      
 """)

def exibir_opcoes():
    print('1. Cadastrar restaurante')
    print('2. Listar restaurantes')
    print('3. Alternar estado do restaurante')
    print('4. Sair\n')

def finalizando_app ():
# limpar o terminal
    # os.system('cls')
    # print('Finalizando o app\n')
    exibir_subtitulo('Finalizando o app')

def voltando_ao_menu_principal():
    input(f'\nDigite uma tecla para voltar ao menu principal: ')
    main()

def opcao_invalida():
    print('Opção invalida!\n')
    voltando_ao_menu_principal()

def exibir_subtitulo(texto):
    os.system('cls')
    linha = '*' * (len(texto)) 
    print(linha)
    print(texto)
    print(linha)
    print()

def cadastrar_novo_restaurante():
    exibir_subtitulo('Cadastro de novos restaurantes')
    nome_do_restaurante = input('Digite o nome do restaurante que deseja cadastrar: ')
    categoria = input(f'Digite a categoria do restaurante {nome_do_restaurante}: ')
    #dicionário 
    dados_do_restaurante = {'nome':nome_do_restaurante, 'categoria':categoria, 'ativo':False}
    #salvando na lista
    restaurantes.append(dados_do_restaurante)
    print(f'O restaurante {nome_do_restaurante} foi cadastrado com sucesso!\n')

    voltando_ao_menu_principal()

def listar_restaurantes():
    exibir_subtitulo('Listando novos restaurantes')    

    print(f'{'Nome do restaurante:'.ljust(22)} | {'Categoria:'.ljust(20)} | Status:')
    for restaurante in restaurantes:
        nome_restaurante = restaurante['nome']
        categoria = restaurante['categoria']
        #ternário
        ativo = 'ativo ' if restaurante['ativo'] else 'desativado'
        print(f'- {nome_restaurante.ljust(20)} | {categoria.ljust(20)} | {ativo}')

    voltando_ao_menu_principal()

def alterna_estado_restaurante():
    exibir_subtitulo('Alternando estado do restaurante')
    nome_restaurante = input('Digite o nome do restaurante que deseja alternar o estado: ')
    restaurante_encontrado = False

    for restaurante in restaurantes:
        if nome_restaurante == restaurante['nome']:
            restaurante_encontrado= True
            restaurante['ativo'] = not restaurante['ativo']
            # ternário
            mensagem = f'O restaurante {nome_restaurante} foi ativado com sucesso!' if restaurante['ativo'] else f'O restaurante {nome_restaurante} foi desativado com sucesso!'
            print(mensagem)

    if not restaurante_encontrado:
        print('O restaurante não foi encontrado!')

    voltando_ao_menu_principal()

def escolher_opcoes():
    try:
        opçao_escolhida = int(input('Escolha uma opção: '))
        # opçao_escolhida = int(opçao_escolhida)

        if opçao_escolhida == 1:
            cadastrar_novo_restaurante()
        elif opçao_escolhida == 2:
            listar_restaurantes()
        elif opçao_escolhida == 3:
            alterna_estado_restaurante()
        elif opçao_escolhida == 4:
            finalizando_app()
        else: 
            opcao_invalida()  
    except:
        opcao_invalida()

def main ():
    os.system('cls')
    exibir_nome_do_programa()
    exibir_opcoes()
    escolher_opcoes()

if __name__ == '__main__':
    main()    