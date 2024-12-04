#def solicitacao_de_emprestismo(conbd,data_emprestimo,data_devolucao,id_livro)
def buscar_livro_por_nome(conbd, nome_livro):
    mycursor = conbd.cursor()
    sql = "SELECT id_livro, nome_l, status FROM livro WHERE nome_l LIKE %s"
    mycursor.execute(sql, ('%' + nome_livro + '%',))
    livro = mycursor.fetchone()
    mycursor.close()
    return livro


def buscar_pessoa_por_nome(conbd, nome_pessoa):
    mycursor = conbd.cursor()
    sql = "SELECT matricula, nome_p FROM detalhepessoa WHERE nome_p LIKE %s"
    mycursor.execute(sql, ('%' + nome_pessoa + '%',))
    pessoa = mycursor.fetchone()
    mycursor.close()
    return pessoa



def solicitar_reserva(conbd, nome_livro, nome_pessoa):
    # Buscar o livro pelo nome
    livro = buscar_livro_por_nome(conbd, nome_livro)
    
    if livro:
        id_livro = livro[0]
        status = livro[2]
        
        if status == 'disponível':
            # Buscar a pessoa pelo nome
            pessoa = buscar_pessoa_por_nome(conbd, nome_pessoa)
            
            if pessoa:
                id_pessoa = pessoa[0]
                
                # Atualiza o status do livro para 'reservado'
                mycursor = conbd.cursor()
                sql_reserva = "UPDATE livro SET status = 'reservado' WHERE id_livro = %s"
                mycursor.execute(sql_reserva, (id_livro,))
                
                # Registrar a reserva na tabela de reservas
                sql_reserva_pessoa = "INSERT INTO reservas(id_livro, id_pessoa, data_reserva) VALUES (%s, %s, NOW())"
                mycursor.execute(sql_reserva_pessoa, (id_livro, id_pessoa))
                
                conbd.commit()
                mycursor.close()
                print(f"Reserva do livro '{nome_livro}' feita com sucesso para {nome_pessoa}.")
            else:
                print(f"A pessoa '{nome_pessoa}' não foi encontrada.")
        else:
            print(f"O livro '{nome_livro}' não está disponível para reserva. Status: {status}")
    else:
        print(f"O livro '{nome_livro}' não foi encontrado.")
        
        
        
def solicitar_emprestimo(conbd, nome_livro, nome_pessoa):
    # Buscar o livro pelo nome
    livro = buscar_livro_por_nome(conbd, nome_livro)
    
    if livro:
        id_livro = livro[0]
        status = livro[2]
        
        if status == 'disponível':
            # Buscar a pessoa pelo nome
            pessoa = buscar_pessoa_por_nome(conbd, nome_pessoa)
            
            if pessoa:
                id_pessoa = pessoa[0]
                
                # Atualiza o status do livro para 'emprestado'
                mycursor = conbd.cursor()
                sql_emprestimo = "UPDATE livro SET status = 'emprestado' WHERE id_livro = %s"
                mycursor.execute(sql_emprestimo, (id_livro,))
                
                # Registrar o empréstimo na tabela de empréstimos
                sql_emprestimo_pessoa = "INSERT INTO emprestimos(id_livro, id_pessoa, data_emprestimo) VALUES (%s, %s, NOW())"
                mycursor.execute(sql_emprestimo_pessoa, (id_livro, id_pessoa))
                
                conbd.commit()
                mycursor.close()
                print(f"Empréstimo do livro '{nome_livro}' solicitado com sucesso para {nome_pessoa}.")
            else:
                print(f"A pessoa '{nome_pessoa}' não foi encontrada.")
        else:
            print(f"O livro '{nome_livro}' não está disponível para empréstimo. Status: {status}")
    else:
        print(f"O livro '{nome_livro}' não foi encontrado.")

# Função para devolver o livro
def devolver_livro(conbd, nome_livro, nome_pessoa):
    # Buscar o livro pelo nome
    livro = buscar_livro_por_nome(conbd, nome_livro)
    
    if livro:
        id_livro = livro[0]
        status = livro[2]
        
        if status == 'emprestado':
            # Buscar a pessoa pelo nome
            pessoa = buscar_pessoa_por_nome(conbd, nome_pessoa)
            
            if pessoa:
                id_pessoa = pessoa[0]
                
                # Atualiza o status do livro para 'disponível'
                mycursor = conbd.cursor()
                sql_devolucao = "UPDATE livro SET status = 'disponível' WHERE id_livro = %s"
                mycursor.execute(sql_devolucao, (id_livro,))
                
                # Registrar a devolução na tabela de devoluções
                sql_devolucao_pessoa = "INSERT INTO devolucoes(id_livro, id_pessoa, data_devolucao) VALUES (%s, %s, NOW())"
                mycursor.execute(sql_devolucao_pessoa, (id_livro, id_pessoa))
                
                conbd.commit()
                mycursor.close()
                print(f"Livro '{nome_livro}' devolvido com sucesso por {nome_pessoa}.")
            else:
                print(f"A pessoa '{nome_pessoa}' não foi encontrada.")
        else:
            print(f"O livro '{nome_livro}' não está emprestado. Status: {status}")
    else:
        print(f"O livro '{nome_livro}' não foi encontrado.")
        
        
#elif escolha == 3:
#            nome_livro = input("Digite o nome do livro que deseja emprestar: ")
 #           nome_pessoa = input("Digite o nome da pessoa que deseja emprestar o livro: ")
  #          solicitar_emprestimo(conbd, nome_livro, nome_pessoa)    
   # elif escolha == 4:
    #        nome_livro = input("Digite o nome do livro que deseja devolver: ")
     #       nome_pessoa = input("Digite o nome da pessoa que está devolvendo o livro: ")
      #      devolver_livro(conbd, nome_livro, nome_pessoa)
    #elif escolha == 5:
     #       nome_livro = input("Digite o nome do livro que deseja reservar: ")
      #      nome_pessoa = input("Digite o nome da pessoa que deseja reservar o livro: ")
       #     solicitar_reserva(conbd, nome_livro, nome_pessoa)       