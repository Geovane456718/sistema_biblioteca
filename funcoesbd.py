def cadastrar_livro_autor(conbd,N_livro,D_sinopse,ano_p,c_isbn,n_autor):
    mycursor = conbd.cursor()
    sql = "INSERT INTO livro(nome_l,sinopse,ano,isbn) values(%s,%s,%s,%s);"
    valores = (N_livro,D_sinopse,ano_p,c_isbn)
    mycursor.execute(sql, valores)
    id_livro = mycursor.lastrowid
    sql2 = "INSERT INTO autor(nome_a,id_livro)values(%s,%s);"
    valores2 = (n_autor,id_livro)
    mycursor.execute(sql2,valores2)
    id_autor = mycursor.lastrowid
    sql3 = "UPDATE livro SET id_autor = %s where id_livro = %s;"
    valores3 = (id_autor,id_livro)
    mycursor.execute(sql3,valores3)
    conbd.commit()
    print("Cadastrado")
    mycursor.close()
    
 
    
def detalhe_pessoa(conbd,nome_p,endereco,cep,matricula,tipo):
    mycursor = conbd.cursor()
    sql = "INSERT INTO detalhepessoa(nome_p,endereco,cep,matricula,tipo) values(%s,%s,%s,%s,%s);"
    valores = (nome_p,endereco,cep,matricula,tipo)
    mycursor.execute(sql,valores)
    conbd.commit()
    mycursor.close()
    
#def cadastrar_pessoa(conbd,nome_p,matricula,)
# def Solicitar_emprestimo(dat_emprestimo,data_devolução)
#criar a função para atualizar, listar e excluir os livros/autor já cadastrado 
def atualizar_livro_autor(conbd, id_livro, novo_nome=None, nova_sinopse=None, novo_ano=None, novo_isbn=None, novo_autor=None):
    mycursor = conbd.cursor()
    if novo_nome or nova_sinopse or novo_ano or novo_isbn:
        sql = "UPDATE livro SET"
        valores = []
        if novo_nome:
            sql += " nome_l = %s,"
            valores.append(novo_nome)
        if nova_sinopse:
            sql += " sinopse = %s,"
            valores.append(nova_sinopse)
        if novo_ano:
            sql += " ano = %s,"
            valores.append(novo_ano)
        if novo_isbn:
            sql += " isbn = %s,"
            valores.append(novo_isbn)
        sql = sql.rstrip(',') + " WHERE id_livro = %s;"
        valores.append(id_livro)  
        mycursor.execute(sql, valores)
    if novo_autor:
        sql_autor = "UPDATE autor SET nome_a = %s WHERE id_livro = %s;"
        mycursor.execute(sql_autor, (novo_autor, id_livro))
    conbd.commit()
    print("Atualização concluída.")
    mycursor.close()


def listar_livros_autores(conbd):
    mycursor = conbd.cursor()
    sql = """
    SELECT l.id_livro, l.nome_l, l.sinopse, l.ano, l.isbn, a.nome_a
    FROM livro l
    LEFT JOIN autor a ON l.id_livro = a.id_livro;
    """
    mycursor.execute(sql)
    resultados = mycursor.fetchall()
    print("ID | Nome do Livro | Sinopse | Ano | ISBN | Nome do Autor")
    print("-" * 60)
    for linha in resultados:
        print(f"{linha[0]} | {linha[1]} | {linha[2]} | {linha[3]} | {linha[4]} | {linha[5]}")
    
    mycursor.close()
  
def excluir_livro_autor(conbd,id_livro  ):
    try:
        mycursor = conbd.cursor()
        

        sql_autor = "UPDATE autor SET id_livro = NULL WHERE id_livro = %s"
        mycursor.execute(sql_autor, (id_livro,))
        sql_livro = "DELETE FROM livro WHERE id_livro = %s"
        mycursor.execute(sql_livro, (id_livro,))
        conbd.commit()

        print("Livro e as referências no autor foram excluídos com sucesso.")
    
    except Exception as e:
        conbd.rollback()  # Em caso de erro, faz o rollback
        print(f"Ocorreu um erro: {e}")
        
        







    