import os


restaurantes = []
restaurantes_ativos = {}

print(restaurantes_ativos)

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
    3. Ativar restaurante
    4. Mais
    """)

def opcoes2():
    """
    Mostra o restante das opções
    """
    print("""
    5. Excluir restaurante
    6. Desativar restaurante
    7. Listar restaurantes ativados e número de ativos
    8. Fechar
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

def mensagem_de_erro(erro):
    """
    Envia a mensagem de opção enviada ao console

    """
    erros = ['Opção Inválida.', 'Nome de restaurante inválido.', 'Nome do restaurante já existe.', 'Esse restaurante não existe.', 'Ainda não existem restaurantes','Nenhum restaurante foi ativado.']
    exibi_msg_erro(f'Erro! {erros[erro]}')
    volta_menu()

def decisao():
    """
    Aplica a escolha do usuário com base no que foi inserido
    Retorna:
    function: retorna as funções cadastro_novo_restaurante, listar_restaurante, opcoes2, mensagem_de_erro e main
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
                decisao2()
            case _:
                mensagem_de_erro(0)
    except ValueError:
        mensagem_de_erro(0)
        volta_menu()

def decisao2():
    """
    Aplica a escolha do usuário da página dois das opções
    Retorna: 
    function: executa as funções exclui_restaurante, desativa_restaurante() e finalizar_app()
    """
    try:
        exibi_subtitulo2('SmallCON  Segunda página de opções')
        opcoes2()
        opcao_do_usuario = int(input('Digite a opção: '))
        match opcao_do_usuario:
            case 5:
                exclui_restaurante()
            case 6:
                desativa_restaurante()
            case 7:
                lista_ativos()
                # imprime_dict()
            case 8:
                finalizar_app()
            case _:
                mensagem_de_erro(0)
    except ValueError:
        mensagem_de_erro(0)

def exibi_subtitulo(txt):
    """
    Imprime o subtítulo da opção
    Limpa o terminal
    Aplica um espaço depois     da mensagem
    Args:
        txt (_type_): _mensagem do subtítulo_
    """
    os.system('cls')
    print(f'SmallCON - {txt}')
    print()

def exibi_msg_erro(txt):
    """
    Template de mensagem de erro aonde não aparece não aparece o nome do sistema

    Args:
        txt (_str_): _mensagem do erro_
    """
    os.system('cls')
    print(txt)
    print()


def exibi_subtitulo2(txt):
    """
    Imprime o subtítulo da opção
    Limpa o terminal
    Args:
        txt (_type_): _mensagem do subtítulo_
    """
    os.system('cls')
    print(f'SmallCON - {txt}')

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
    if nome_restaurante != '':
        if nome_restaurante not in restaurantes:
            restaurantes.append(nome_restaurante)
            # Adiciona o restaurante para o dicionário dos ativos mas com valor de 0 (não)
            adiciona_ativo_0(nome_restaurante)
            # ----------------------------------
            print(f'O restaurante {nome_restaurante} foi criado')
            volta_menu()
        else:
            mensagem_de_erro(2)
    else:
        print(nome_restaurante)
        mensagem_de_erro(1)

def adiciona_ativo_0(nome):
    """
    Adiciona o restaurante cadastrado com valor de 0
    Args:
        nome (_str_): _nome do restaurante para ser pegado o index dele_
    """
    restaurantes_ativos.update({restaurantes[acha_index_restaurante(nome)]: {'ativo': 0}})

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
    exibi_subtitulo('Ativando restaurante')
    if existe_restaurantes():
        exibi_subtitulo('Ativando o restaurante')
        nome_do_restaurante = verifica_restaurante()
        index_restaurante = acha_index_restaurante(nome_do_restaurante)
        restaurantes_ativos.update({restaurantes[index_restaurante]: {'ativo': 1}})
        print('Restaurante ativado!')
        volta_menu()
    else:
        mensagem_de_erro(4)
        volta_menu()

# Opcões 2 -------------------------------------------

def exclui_restaurante():
    """
    Exclui um restaurante existente
    Retorna:
    list: a lista atualizada com os restaurantes existentes
    """
    if existe_restaurantes():
        exibi_subtitulo('Excluindo restaurante')
        nome_restaurante = input('Digite o nome do restaurante: ')
        if esse_restaurante_existe(nome_restaurante):
            index = acha_index_restaurante(nome_restaurante)
            restaurantes_ativos.pop(restaurantes[index])
            restaurantes.pop(index)
            print(f'O restaurante {nome_restaurante} foi excluído!')
            volta_menu()
    else:
        mensagem_de_erro(4)

def desativa_restaurante():
    """
    Desativa um restaurante ativo
    Retorna:
    dict: dicionário com os restaurantes ativos atualizados
    """
    if existe_restaurantes():
        exibi_subtitulo('Desativa restaurante')
        nome_restaurante = input('Digite o nome do restaurante que vai ser desativado: ')
        if esse_restaurante_existe(nome_restaurante):
            index = acha_index_restaurante(nome_restaurante)
            restaurantes_ativos.update({restaurantes[index]: {'ativo': 0}})
            print(f'O {nome_restaurante} foi desativado!')
            volta_menu()
    else:
        mensagem_de_erro(4)

def lista_ativos():
    """
    Função que lista os restaurantes ativados
    Soma o número de restaurantes ativados
    Retorna:
    str: mensagem com os restaurantes ativos junto do número de restaurantes
    """
    if existe_restaurantes():
        exibi_subtitulo2('Lista/Número de ativo')
        conta = 0
        conta1 = 0
        for index, chave in restaurantes_ativos.items():
            if chave.get('ativo') == 1:
                print('Ativos ------')
                conta += 1
                print(f'{conta}. {index}')
            if chave.get('ativo') == 0:
                print('Inativos ------')
                conta1 += 1
                print(f'{conta1}. {index}')
        print(f'Número de restaurantes ativos: {conta}')
        print(f'Número de restaurantes inativos: {conta1}')
        volta_menu()
    else:
        mensagem_de_erro(4)

def imprime_dict():
    """
    Imprime o dicionário se for preciso. Normalmente usado para debug
    """
    print(restaurantes_ativos.items())

def verifica_restaurante():
    """
    Verifica se existe o restaurante mencionado
    """
    nome_restaurante = input('Digite o nome do restaunte: ')
    if nome_restaurante in restaurantes:
        return nome_restaurante
    else:
        mensagem_de_erro(5)
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
    print()
    input('Digite algo para voltar ao menu: ')
    main()

def esse_restaurante_existe(nome):
    """
    Verifica se o restaurante realmente existe
    Retorna o erro se não existir
    Args:
        nome (_str_): _nome do restaurante_
    """
    def cancela_mensagem_de_erro(arg):
        if arg is True:
            pass
        else:
            mensagem_de_erro(3)

    aqui = nome in restaurantes
    cancela_mensagem_de_erro(aqui)
    return aqui

if __name__ == '__main__':
    main()
