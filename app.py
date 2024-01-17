import os


restaurantes = []
# Para mais tarde
# try:
#     restaurantes_ativos = {
#         restaurantes[0]: {
#             'ativo': 1
#         }
#     }
# except IndexError:
#     pass

def nome_do_programa():
    """
    Imprime o nome do sistema.
    """
    print('SmallCON')

def opcoes():
    """
    Mostra para o usuário as opções do menu.
    """
    print("""
    1. Cadastrar o restaurante
    2. Listar restaurantes
    3. Ativar novamente
    4. Fechar
    """)

def finalizar_app():
    """
    Finaliza o funcionamento do sistema;
    Limpa o console;
    Retorna:
    none: o sistema encerra e retorna uma mensagem de final.
    """
    os.system('cls')
    print('Fechando o app\n')
    print()

def opcao_invalida():
    """
    Envia a mensagem de opção enviada ao console

    """
    exibi_subtitulo('Erro! Opção Ínvalida')
    input('Digite alguma tecla para retornar: ')
    main()

def decisao():
    """
    Aplica a escolha do usuário com base no que foi inserido
    Retorna:
    function: retorna as funções cadastro_novo_restaurante, listar_restaurante, finalizar_app e main
    """
    try:
        opcao_do_usuario = int(input('Digite a sua escolha: '))
        match opcao_do_usuario:
            case 1:
                cadastrar_novo_restaurante()
            case 2:
                listar_restaurante()
            case 3:
                ativa_restaurante()
            case 4:
                finalizar_app()
            case _:
                opcao_invalida()
    except ValueError:
        opcao_invalida()
        main()

def exibi_subtitulo(txt):
    """
    Imprime o subtítulo da opção
    Limpa o terminal
    Args:
        txt (_type_): _description_
    """
    os.system('cls')
    print(txt)
    print()

def main():
    """
    Função base para iterar o sistema. Não sendo necessário rodar o programa todas as vezes
    """
    os.system('cls')
    nome_do_programa()
    opcoes()
    decisao()

def cadastrar_novo_restaurante():
    """
    Incluí um novo restaurante para a variável <restaurante>
    Retorna:
    str: mensagem de sucesso dizendo que o restaurante foi cadastrado.
    """
    exibi_subtitulo('Cadastro de restaurante')
    nome_restaurante = input("Digite o nome do seu restaunte: ")
    restaurantes.append(nome_restaurante)
    print(f'O restaurante {nome_restaurante} foi criado')
    volta_menu()

def listar_restaurante():
    """
    Lista os restaurantes cadastrados;
    Organiza numéricamente os restaurantes;
    Retorna:
    str e int: o nome listado dos restaurantes.
    """
    exibi_subtitulo('Listando os restaurantes')
    numero = 0
    for restaurante in restaurantes:
        numero = numero + 1
        print(f'{numero}. {restaurante}')
    volta_menu()

def ativa_restaurante():
    """
    Ativa um restaunte escolhido pelo usuário
    Verifica se existem restaurantes
    Retorno:
    array: coloca em restaurantes_ativos { restaurante[] }
    """
    if existe_restaurantes():
        exibi_subtitulo('Ativando o restaurante')
        nome_do_restaurante = verifica_restaurante()
        index_restaurante = acha_index_restaurante(nome_do_restaurante)
    else:
        print('Ainda não foi cadastrado nenhum restaurante.')
        volta_menu()

def verifica_restaurante():
    """
    Verifica se existe o restaurante mencionado
    """
    nome_restaurante = input('Digite o nome do restaunte: ')
    if nome_restaurante in restaurantes:
        return nome_restaurante
    else:
        print('Restaurante não encontrado')
        volta_menu()

def acha_index_restaurante(arg):
    """
    Acha o index do restaurante

    Args:
        arg (_str_): _nome do restaurante_

    Returns:
        _int_: _index do restaurante dentro da variável_
    """
    info = restaurantes.index(arg)
    return info

def existe_restaurantes():
    """
    Verifica se existem restaurantes na variável restaurante

    Returns:
        True: se o número de restaurantes for maior que um
        False: se o número de restaurantes for menor que um
    """
    existe = len(restaurantes) >= 1
    return existe

def volta_menu():
    """
    Volta ao menu de opções do usuário
    Retorna:
    function: executa a função main() que retorna ao menu e executa outras funções como opcoes()
    """
    input('Digite algo para voltar ao menu: ')
    main()

if __name__ == '__main__':
    main()
