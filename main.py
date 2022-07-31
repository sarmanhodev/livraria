from fastapi import FastAPI, HTTPException, Request, status
from fastapi.exceptions import RequestValidationError
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse
from classes import *
from database import SessionLocal
import tabelas
from typing import List
from sqlalchemy.orm import joinedload


app = FastAPI()

db = SessionLocal()

@app.get("/", status_code=status.HTTP_200_OK)
async def hello():
    """
    **Boas vindas**
    """

    ola=str("Seja bem-vindo, usuário!")
    print("\n"+str(ola)+"\n")
    return ola


#POST EDITORA
@app.post("/editora", response_model=Editora, status_code=status.HTTP_201_CREATED)
async def add_editora(editora: Editora):
    """
    Cria um novo registro na tabela **Editora**
    
    - **id: int**
    - **nome:str**
    
    """ 

    nova_editora = tabelas.Editora(nome = editora.nome)
    db.add(nova_editora)
    db.commit()
       
    print("\nEditora cadastrada com sucesso\n")

    return nova_editora

 
#GET RETORNA TODOS OS REGISTROS
@app.get("/editoras",response_model= List[Editora_Out], status_code=status.HTTP_200_OK)
async def get_editoras():
    """
      - Retorna os valores registrados na tabela **Editora**
    
    """
 
    editora = db.query(tabelas.Editora).order_by(tabelas.Editora.id).options(joinedload(tabelas.Editora.livros)).all()

    if editora == None:
        print("\nNenhum registro encontrado")
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Nenhum registro encontrado")
    
    return editora

#GET EDITORA NOME
@app.get("/editora/{nome}", response_model = Editora_Out, status_code=status.HTTP_200_OK)
async def get_editora_nome(nome:str):
    """
    - Realiza a busca por uma editora através de seu **nome**
    
    """
    editora_nome = db.query(tabelas.Editora).filter(tabelas.Editora.nome==nome).first()
    
    return editora_nome



#DELETA UM REGISTRO DA TABELA EDITORA
@app.delete("/editora/delete/{nome}", response_model=Editora, status_code=status.HTTP_200_OK)
async def deleta_editora(nome:str):
    """
    Após efetuar a busca de uma determinada editora através de seu **nome**, esta função apaga registro existente no banco
    """

    editora_delete = db.query(tabelas.Editora).filter(tabelas.Editora.nome==nome).first()

    if editora_delete is None:
        print("\nRegistro não encontrado\n")
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail='Registro não encontrado')
    
    db.delete(editora_delete)
    db.commit()

    print("REGISTRO EXCLUIDO")
    return editora_delete


#ATUALIZANDO REGISTRO DA TABELA EDITORA
@app.put("/editora/update/{id}",response_model=Editora_Out,status_code=status.HTTP_200_OK)
async def atualiza_editora(id:int,editora:Editora_Out):
    """
    Após efetuar a busca de uma determinada editora através de seu **Id**, seu registro poderá ser atualizado
    """
    editora_update = db.query(tabelas.Editora).filter(tabelas.Editora.id==id).options(joinedload(tabelas.Editora.livraria), joinedload(tabelas.Editora.livro)).first()

    if editora_update == None:
        print("\nRegistro não encontrado\n")
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail='Registro não encontrado')

    editora_update.name=editora.nome
    db.commit()

    print("\nDados atualizados com sucesso!")
    return editora_update


#POST LIVRO
@app.post("/livro", response_model=Livro, status_code=status.HTTP_201_CREATED)
async def add_livro(livro: Livro):
    """
    - Cria um novo registro na tabela **Livro**
    
    - **id:int**
    - **titulo:str**
    - **ano:int**
    - **nome_autor:str**
    - **isbn:str**
    - **editora_id:int**
    - **assunto:str**
          
    """

    novo_livro =tabelas.Livro(titulo = livro.titulo, ano = livro. ano, nome_autor=livro.nome_autor, isbn = livro.isbn, editora_id=livro.editora_id,
    assunto= livro.assunto)
    db.add(novo_livro)
    db.commit()
    
    print("\nLivro cadastrado com sucesso\n")

    return novo_livro


#GET TODOS OS LIVROS
@app.get("/livros/catalogo", response_model= List[Livro_Out], status_code=status.HTTP_200_OK)
async def CatalogoLivros():
    """
    - Retorna todos os registros da tabela **Livro**
    """

    livro = db.query(tabelas.Livro).order_by(tabelas.Livro.id).options(joinedload(tabelas.Livro.editora), joinedload(tabelas.Livro.detalhes)).all()

    return livro


#GET LIVRO TÍTULO
@app.get("/livro/titulo={titulo}", response_model = Livro_Out, status_code=status.HTTP_200_OK)
async def BuscarLivros(titulo:str):
    """
    - Realiza a busca por um livro através de seu **nome**
    
    """
    livro_nome = db.query(tabelas.Livro).filter(tabelas.Livro.titulo==titulo).first()
    
    return livro_nome



#DELETA UM REGISTRO DA TABELA LIVRO
@app.delete("/livro/delete/{titulo}", response_model=Livro, status_code=status.HTTP_200_OK)
async def deleta_livro(titulo:str):
    """
    Após efetuar a busca de um determinado livro através de seu **nome**, esta função apaga registro existente no banco
    """

    livro_delete = db.query(tabelas.Livro).filter(tabelas.Livro.titulo==titulo).first()

    if livro_delete is None:
        print("\nRegistro não encontrado\n")
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail='Registro não encontrado')
    
    db.delete(livro_delete)
    db.commit()

    print("REGISTRO EXCLUIDO")
    return livro_delete


#ATUALIZANDO REGISTRO DA TABELA LIVRO
@app.put("/livro/update/{id}",response_model=Livro_Out,status_code=status.HTTP_200_OK)
async def atualiza_livro(id:int,livro:Livro_Out):
    """
    Após efetuar a busca de um determinado **livro** através de seu **Id**, seu registro poderá ser atualizado
    """
    livro_update = db.query(tabelas.Livro).filter(tabelas.Livro.id==id)\
        .options(joinedload(tabelas.Livro.livraria), joinedload(tabelas.Livro.editora), joinedload(tabelas.Livro.detalhes)).first()

    if livro_update == None:
        print("\nRegistro não encontrado\n")
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail='Registro não encontrado')

    livro_update.titulo=livro.titulo
    livro_update.ano=livro.ano
    livro_update.nome_autor=livro.nome_autor
    livro_update.isbn=livro.isbn
    livro_update.editora_id=livro.editora_id
    livro_update.assunto=livro.assunto
    db.commit()

    print("\nDados atualizados com sucesso!")
    return livro_update



#POST LIVRARIA
@app.post("/livraria", response_model=Livrarias, status_code=status.HTTP_201_CREATED)
async def add_livraria(livraria: Livrarias):
    """
    - Cria um novo registro na tabela **Livrarias**
    
    - **id:int**
    - **nome:str**
    
    """

    nova_livraria =tabelas.Livrarias(nome = livraria.nome)
    db.add(nova_livraria)
    db.commit()
    
    print("\nLivraria cadastrado com sucesso\n")

    return nova_livraria


#GET TODAS AS LIVRARIAS
@app.get("/livrarias/livros/vendas", response_model=List[Livrarias_Out],status_code=status.HTTP_200_OK)
async def LivrosVendidosPorLivrarias():
    """
    - Retorna todos os registros da tabela **Livraria**
    
    """

    livrarias = db.query(tabelas.Livrarias).order_by(tabelas.Livrarias.id).options(joinedload(tabelas.Livrarias.detalhes)).all()

    return livrarias



#GET LIVRARIA NOME
@app.get("/livraria/{nome}", response_model = Livrarias_Out, status_code=status.HTTP_200_OK)
async def get_livraria_nome(nome:str):
    """
    - Realiza a busca por uma livraria através de seu **nome**
    
    """
    livraria_nome = db.query(tabelas.Livrarias).filter(tabelas.Livrarias.nome==nome).first()
    
    return livraria_nome



#DELETA UM REGISTRO DA TABELA LIVRARIA
@app.delete("/livraria/delete/{nome}", response_model=Livrarias, status_code=status.HTTP_200_OK)
async def deleta_livraria(nome:str):
    """
    Após efetuar a busca de uma determinada **livraria** através de seu **nome**, esta função apaga registro existente no banco
    """

    livraria_delete = db.query(tabelas.Livro).filter(tabelas.Livro.titulo==titulo).first()

    if livraria_delete is None:
        print("\nRegistro não encontrado\n")
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail='Registro não encontrado')
    
    db.delete(livraria_delete)
    db.commit()

    print("REGISTRO EXCLUIDO")
    return livraria_delete


#ATUALIZANDO REGISTRO DA TABELA LIVRARIA
@app.put("/livraria/update/{id}",response_model=Livrarias_Out,status_code=status.HTTP_200_OK)
async def atualiza_livraria(id:int,livraria:Livrarias_Out):
    """
    Após efetuar a busca de uma determinada **livraria** através de seu **Id**, seu registro poderá ser atualizado
    """
    livraria_update = db.query(tabelas.Livrarias).filter(tabelas.Livrarias.id==id)\
        .options(joinedload(tabelas.Livrarias.livro), joinedload(tabelas.Livrarias.detalhes)).first()

    if livraria_update == None:
        print("\nRegistro não encontrado\n")
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail='Registro não encontrado')

    livraria_update.nome=livraria.nome
    livraria_update.livro=livraria.livro
    livraria_update.detalhes=livraria.detalhes
    
    db.commit()

    print("\nDados atualizados com sucesso!")
    return livraria_update



#POST LIVRARIA_LIVRO
@app.post("/livraria_livro", response_model=Livraria_Livro, status_code=status.HTTP_201_CREATED)
async def add_livraria_livro(livraria_livro: Livraria_Livro):
    """
    - Cria um novo registro na tabela **Livraria_Livro**
    
    - **livraria_id:int**
    - **livro_id:int**
    - **quantidade_estoque: int**
    - **valor: float**
    - **prazo_entrega: str**
    
    """

    novo_registro =tabelas.Livraria_Livro(livraria_id=livraria_livro.livraria_id, livro_id = livraria_livro.livro_id, quantidade_estoque=livraria_livro.quantidade_estoque,
    valor = livraria_livro.valor, prazo_entrega = livraria_livro.prazo_entrega)
    db.add(novo_registro)
    db.commit()
    
    print("\nCadastrado com sucesso\n")

    return novo_registro


#GET LIVRARIA_LIVRO
@app.get("/livraria_livro/{nome_livro}", response_model = Livraria_Livro, status_code=status.HTTP_200_OK)
async def get_livraria_livro_nome(nome_livro:str):
    """
    - Realiza a busca por um livro através de seu **nome**
    
    """
    nome = db.query(tabelas.Livraria_Livro).filter(tabelas.Livraria_Livro.livro==nome_livro).first()
    
    return nome



#DELETA UM REGISTRO DA TABELA LIVRARIA_LIVRO
@app.delete("/livraria_livro/delete/{id}", response_model=Livraria_Livro, status_code=status.HTTP_200_OK)
async def deleta_livraria_livro(id:int):
    """
    Após efetuar a busca de um determinado **livro** através de seu **nome**, esta função apaga registro existente no banco
    """

    delete = db.query(tabelas.Livraria_Livro).filter(tabelas.Livraria_Livro.id==id).first()

    if delete is None:
        print("\nRegistro não encontrado\n")
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail='Registro não encontrado')
    
    db.delete(delete)
    db.commit()

    print("REGISTRO EXCLUIDO")
    return delete


""""#ATUALIZANDO REGISTRO DA TABELA LIVRARIA_LIVRO
@app.put("/livraria_livro/update/{nome}",response_model=Livraria_Livro_Out,status_code=status.HTTP_200_OK)
async def atualiza_livraria_livro(nome:str,livraria_livro:Livraria_Livro_Out):
   
    livraria_livro_update = db.query(tabelas.Livraria_Livro).filter(tabelas.Livraria_Livro.livraria==nome or tabelas.Livraria_Livro.livro==nome)\
        .options(joinedload(tabelas.Livraria_Livro.livraria), joinedload(tabelas.Livraria_Livro.livro)).first()

    if livraria_livro_update == None:
        print("\nRegistro não encontrado\n")
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail='Registro não encontrado')

    livraria_livro_update.nome=livraria.nome
    livraria_update.livro=livraria.livro
    livraria_update.detalhes=livraria.detalhes
    
    db.commit()

    print("\nDados atualizados com sucesso!")
    return livraria_livro_update"""


#POST PAÍS
@app.post("/paises", response_model=Pais, status_code=status.HTTP_201_CREATED)
async def add_pais(pais: Pais):
    """
    - Cria um novo registro na tabela **País**
    
    - **id: int**
    - **sigla: str**
    - **nome: str** 
    
    
    """

    novo_pais=tabelas.Pais(sigla= pais.sigla ,nome= pais.nome)
    db.add(novo_pais)
    db.commit()
    
    print("\nid: "+str(novo_pais.id))
    print("sigla: "+str(novo_pais.sigla))
    print("nome: "+str(novo_pais.nome))
   
    print("\nPaís cadastrado com sucesso\n")

    return novo_pais


#DELETA UM REGISTRO DA TABELA PAÍS
@app.delete("/pais/delete/{id}", response_model=Pais, status_code=status.HTTP_200_OK)
async def deleta_estado(id:int):
    """
    Após efetuar a busca de um determinado país através de seu **Id**, esta função apaga registro existente no banco
    """

    pais_delete = db.query(tabelas.Pais).filter(tabelas.Pais.id==id).first()

    if pais_delete is None:
        print("\nRegistro não encontrado\n")
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail='Registro não encontrado')
    
    db.delete(pais_delete)
    db.commit()

    print("REGISTRO EXCLUIDO")
    return pais_delete


#ATUALIZANDO REGISTRO DA TABELA PAÍS
@app.put("/pais/update/{id}",response_model=Pais,status_code=status.HTTP_200_OK)
async def atualiza_pais(id:int,pais:Pais):
    """
    Após efetuar a busca de um determinado país através de seu **Id**, seu registro poderá ser atualizado
    """
    pais_update = db.query(tabelas.Pais).filter(tabelas.Pais.id==id).first()

    if pais_update == None:
        print("\nRegistro não encontrado\n")
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail='Registro não encontrado')

    pais_update.name=pais.sigla
    pais_update.email=pais.nome
    
    db.commit()

    
    print("\nDados atualizados com sucesso!")
    return pais_update


#GET PAÍSES
@app.get("/paises",response_model= List[Pais], status_code=status.HTTP_200_OK)
async def get_paises():
    """
    - Retorna todos os registros da tabela **País**
    """
 
    pais = db.query(tabelas.Pais).all()

    if pais == None:
        print("\nNenhum registro encontrado")
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Nenhum registro encontrado")
    
   
    return pais

#POST ESTADO
@app.post("/estado", response_model=Estado, status_code=status.HTTP_201_CREATED)
async def add_estado(estado: Estado):
    """
    Cria um novo registro na tabela **Estado**
    
    - **id: int**
    - **sigla: str**
    - **nome: str** 
    
    
    """

    novo_estado=tabelas.Estado(sigla= estado.sigla ,nome= estado.nome)
    db.add(novo_estado)
    db.commit()
    
    print("\nid: "+str(novo_estado.id))
    print("sigla: "+str(novo_estado.sigla))
    print("nome: "+str(novo_estado.nome))
   
    print("\nEstado cadastrado com sucesso\n")

    return novo_estado


#DELETA UM REGISTRO DA TABELA ESTADO
@app.delete("/estado/delete/{id}", response_model=Estado, status_code=status.HTTP_200_OK)
async def deleta_estado(id:int):
    """
    Após efetuar a busca de um determinado estado através de seu **Id**, esta função apaga registro existente no banco
    """

    estado_delete = db.query(tabelas.Estado).filter(tabelas.Estado.id==id).first()

    if estado_delete is None:
        print("\nRegistro não encontrado\n")
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail='Registro não encontrado')
    
    db.delete(estado_delete)
    db.commit()

    print("REGISTRO EXCLUIDO")
    return estado_delete



#ATUALIZANDO REGISTRO DA TABELA ESTADO
@app.put("/estado/update/{id}",response_model=Estado,status_code=status.HTTP_200_OK)
async def atualiza_estado(id:int,estado:Estado):
    """
    Após efetuar a busca de um determinado estado através de seu **Id**, seu registro poderá ser atualizado
    """
    estado_update = db.query(tabelas.Estado).filter(tabelas.Estado.id==id).first()

    if estado_update == None:
        print("\nRegistro não encontrado\n")
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail='Registro não encontrado')

    estado_update.name=estado.sigla
    estado_update.email=estado.nome
    
    db.commit()

    
    print("\nDados atualizados com sucesso!")
    return estado_update


#GET ESTADOS
@app.get("/estados",response_model= List[Estado], status_code=status.HTTP_200_OK)
async def get_estados():
    """
    - Retorna todos os registros da tabela **ESTADOS**
    """
 
    estado = db.query(tabelas.Estado).all()

    if estado == None:
        print("\nNenhum registro encontrado")
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Nenhum registro encontrado")
    
    #total="Total de alunos cadastrados: "+str(len(aluno))
   
    #print("\n"+str(total)+"\n")
    return estado


#POST CIDADE
@app.post("/cidade", response_model=Cidade, status_code=status.HTTP_201_CREATED)
async def add_cidade(cidade: Cidade):
    """
    Cria um novo registro na tabela **Cidade**
    
    - **id: int**
    - **sigla: str**
    - **nome: str** 
    
    
    """

    nova_cidade=tabelas.Cidade(sigla= cidade.sigla ,nome= cidade.nome)
    db.add(nova_cidade)
    db.commit()
    
    print("\nid: "+str(nova_cidade.id))
    print("sigla: "+str(nova_cidade.sigla))
    print("nome: "+str(nova_cidade.nome))
   
    print("\nCidade cadastrada com sucesso\n")

    return nova_cidade


#DELETA UM REGISTRO DA TABELA CIDADE
@app.delete("/cidade/delete/{id}", response_model=Cidade, status_code=status.HTTP_200_OK)
async def deleta_cidade(id:int):
    """
    Após efetuar a busca de uma determinada cidade através de seu **Id**, esta função apaga registro existente no banco
    """

    cidade_delete = db.query(tabelas.Cidade).filter(tabelas.Cidade.id==id).first()

    if cidade_delete is None:
        print("\nRegistro não encontrado\n")
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail='Registro não encontrado')
    
    db.delete(cidade_delete)
    db.commit()

    print("REGISTRO EXCLUIDO")
    return cidade_delete



#ATUALIZANDO REGISTRO DA TABELA CIDADE
@app.put("/cidade/update/{id}",response_model=Cidade,status_code=status.HTTP_200_OK)
async def atualiza_cidade(id:int,cidade:Cidade):
    """
    Após efetuar a busca de uma determinada cidade através de seu **Id**, seu registro poderá ser atualizado
    """
    cidade_update = db.query(tabelas.Cidade).filter(tabelas.Cidade.id==id).first()

    if cidade_update == None:
        print("\nRegistro não encontrado\n")
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail='Registro não encontrado')

    cidade_update.name=cidade.sigla
    cidade_update.email=cidade.nome
    
    db.commit()

    
    print("\nDados atualizados com sucesso!")
    return cidade_update



#GET CIDADES
@app.get("/cidades", response_model=List[Cidade], status_code=status.HTTP_200_OK)
async def get_cidades():
    """
   - Retorna todos os registros da tabela **CIDADE**
    """
    cidades = db.query(tabelas.Cidade).all()

    if cidades == None:
        print("\nNenhum registro encontrado")
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Nenhum registro encontrado")

    return cidades



#POST ENDEREÇO
@app.post("/endereco", response_model=Endereco, status_code=status.HTTP_201_CREATED)
async def add_endereco(endereco: Endereco):
    """
    - Cria um novo registro na tabela **Endereco**
    
    - **id:int**
    - **cep:str**
    - **logradouro:str**
    - **numero:int**
    - **complemento:str**
    - **cidade_id:int**
    - **estado_id:int**
    - **pais_id:int**
      
    """

    novo_endereco=tabelas.Endereco(cep=endereco.cep, logradouro=endereco.logradouro,complemento = endereco.complemento, numero=endereco.numero,
    cidade_id = endereco.cidade_id, estado_id=endereco.estado_id, pais_id=endereco.pais_id)
    db.add(novo_endereco)
    db.commit()
    
  
   
    print("\nEndereço cadastrado com sucesso\n")

    return novo_endereco


#DELETA UM REGISTRO DA TABELA ENDEREÇO
@app.delete("/endereco/delete/{id}", response_model=Endereco, status_code=status.HTTP_200_OK)
async def deleta_endereco(id:int):
    """
    Após efetuar a busca de um determinado endereço através de seu **Id**, esta função apaga registro existente no banco
    """

    endereco_delete = db.query(tabelas.Endereco).filter(tabelas.Endereco.id==id).first()

    if endereco_delete is None:
        print("\nRegistro não encontrado\n")
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail='Registro não encontrado')
    
    db.delete(endereco_delete)
    db.commit()

    print("REGISTRO EXCLUIDO")
    return endereco_delete


#ATUALIZANDO REGISTRO DA TABELA ENDEREÇO
@app.put("/endereco/update/{id}",response_model=Endereco,status_code=status.HTTP_200_OK)
async def atualiza_endereco(id:int,endereco:Endereco):
    """
    Após efetuar a busca de um determinado endereco através de seu **Id**, seu registro poderá ser atualizado
    """
    endereco_update = db.query(tabelas.Endereco).filter(tabelas.Endereco.id==id).first()

    if endereco_update == None:
        print("\nRegistro não encontrado\n")
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail='Registro não encontrado')

    endereco_update.name=endereco.cep
    endereco_update.email=endereco.logradouro
    endereco_update.senha=endereco.numero
    endereco_update.senha=endereco.complemento

    db.commit()

    
    print("\nDados atualizados com sucesso!")
    return endereco_update


#GET ENDEREÇOS
@app.get("/enderecos", response_model = List[Endereco_Out], status_code=status.HTTP_200_OK)
async def get_endereco():
    """
    - Retorna todos os registros da tabela **Endereco**
    """
    endereco = db.query(tabelas.Endereco).options(joinedload(tabelas.Endereco.cidade), joinedload(tabelas.Endereco.estado),\
    joinedload(tabelas.Endereco.pais)).all()

    if endereco == None:
        print("\nNenhum registro encontrado")
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Nenhum registro encontrado")

    return endereco 


#POST AUTOR
@app.post("/cliente", response_model=Cliente, status_code=status.HTTP_201_CREATED)
async def add_cliente(cliente: Cliente):
    """
    Cria um novo registro na tabela **Cliente**
    
    - **id: int**
    - **cpf:str**
    - **nome:str**
    - **data_nascimento:str**
    - **endereco_id:int**
    """ 

    novo_cliente = tabelas.Cliente(cpf = cliente.cpf, data_nascimento = cliente.data_nascimento, nome = cliente.nome, endereco_id = cliente.endereco_id)
    db.add(novo_cliente)
    db.commit()
    
  
   
    print("\nAutor cadastrado com sucesso\n")

    return novo_cliente


#GET CLIENTES
@app.get("/clientes", response_model = List[Cliente_Out], status_code=status.HTTP_200_OK)
async def clientes():
    """
    Retorna todos os registros da tabela Cliente
    """
    clientes = db.query(tabelas.Cliente).order_by(tabelas.Cliente.id).options(joinedload(tabelas.Cliente.endereco)).all()

    return clientes

#DELETA UM REGISTRO DA TABELA CLIENTE
@app.delete("/cliente/delete/{id}", response_model=Cliente, status_code=status.HTTP_200_OK)
async def deleta_cliente(id:int):
    """
    Após efetuar a busca de um determinado **cliente** através de seu **Id**, esta função apaga registro existente no banco
    """

    cliente_delete = db.query(tabelas.Cliente).filter(tabelas.Cliente.id==id).first()

    if cliente_delete is None:
        print("\nRegistro não encontrado\n")
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail='Registro não encontrado')
    
    db.delete(cliente_delete)
    db.commit()

    print("REGISTRO EXCLUIDO")
    return cliente_delete


#ATUALIZANDO REGISTRO DA TABELA CLIENTE
@app.put("/cliente/update/{id}",response_model=Cliente_Out,status_code=status.HTTP_200_OK)
async def atualiza_cliente(id:int,cliente:Cliente_Out):
    """
    Após efetuar a busca de um determinado **cliente** através de seu **Id**, seu registro poderá ser atualizado
    """
    cliente_update = db.query(tabelas.Cliente).filter(tabelas.Autor.id==id).options(joinedload(tabelas.Cliente.endereco)).first()

    if cliente_update == None:
        print("\nRegistro não encontrado\n")
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail='Registro não encontrado')

    cliente_update.cpf = cliente.cpf
    cliente_update.nome=cliente.nome
    cliente_update.data_nascimento=cliente.data_nascimento

    db.commit()

    
    print("\nDados atualizados com sucesso!")
    return cliente_update