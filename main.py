from conexaobd import conexao 
from funcoesbd import *

conbd = conexao()



def menu():
    print("-- SISTEMA BIBLIOTECARIO --") #OK
    print("1 - CADASTRAR LIVRO/AUTOR") #OK
    print("2 - CADASTRAR DETALHE PESSOA") #OK
    print("3 - SOLICITAR EMPRESTIMO")
    print("4 - CADASTRAR PESSOA")
    print("5 - SOLICITAR RESERVA")
    print("6 - ATUALIZAR/LISTAR/EXCLUIR LIVROS CADASTRADO")#ok,ok,..
    print("7 - ENCERRAR O SISTEMA!!! ")
while True:
    menu()
    
    escolha  = int(input("Digite uma das opções acima: "))
    
    if escolha == 1:
        nome_livro = str(input("Digite o nome do livro para cadastro: "))
        sinopse = str(input("Digite a sinopse do livro: "))
        ano_publicado = int(input("Digite o ano do livro: "))
        codigo_isbn = str(input("Digite o isbn do livro: "))
        nome_autor = str(input("Digite o nome do autor do livro: ")) 
        cadastrar_livro_autor(conbd,nome_livro,sinopse,ano_publicado,codigo_isbn,nome_autor)
    elif escolha == 2:
        nome_pessoa = str(input("Digite o seu nome: "))
        endereco = str(input("informe seu endenreço: "))
        cep = int(input("Informe seu CEP: "))
        matricula = int(input("Informe a sua matricula: "))
        tipo = str(input("Informe se é Funcionário/Estudante? "))
        detalhe_pessoa(conbd,nome_pessoa,endereco,cep,matricula,tipo)
    elif escolha == 6:
        print("1 - Atualizar Livro/Autor")
        print("2 - Listar Livros/Autores")
        print("3 - Excluir Livro/Autor")
        opcao = int(input("Escolha a operação: "))
        
        if opcao == 1:
            id_livro = int(input("Digite o ID do livro para atualizar: "))
            novo_nome = input("Novo nome (ou deixe vazio): ")
            nova_sinopse = input("Nova sinopse (ou deixe vazio): ")
            novo_ano = input("Novo ano (ou deixe vazio): ")
            novo_ano = int(novo_ano) if novo_ano else None
            novo_isbn = input("Novo ISBN (ou deixe vazio): ")
            novo_autor = input("Novo nome do autor (ou deixe vazio): ")
            atualizar_livro_autor(conbd, id_livro, novo_nome, nova_sinopse, novo_ano, novo_isbn, novo_autor)
        
        elif opcao == 2:
            listar_livros_autores(conbd)
        
        elif opcao == 3:
            nome_l = str(input("Digite o ID do livro para excluir: "))
            excluir_livro_autor(conbd, nome_l)
        
        else:
            print("Opção inválida.")
        
        
    elif escolha == 7:
        break   
        
  

