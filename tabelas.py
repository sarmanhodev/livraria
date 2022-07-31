from database import Base, engine
from sqlalchemy import BigInteger, String,Integer, Column, ForeignKey, Float
from sqlalchemy.orm import relationship


class Livraria_Livro(Base):
    __tablename__="livraria_livro"
    id=Column(Integer, primary_key=True)
    livraria_id= Column(Integer,ForeignKey('livrarias.id'))
    livro_id = Column(Integer,ForeignKey('livro.id'))
    quantidade_estoque = Column(Integer,nullable= False, unique = False)
    valor = Column(Float, nullable = False)
    prazo_entrega = Column(String(256),nullable= False, unique = False)

    #RELATIONSHIPS
    livraria = relationship("Livrarias", back_populates = "detalhes")
    livro = relationship("Livro", back_populates = "detalhes")


class Livro_Cliente(Base):
    __tablename__ = "livro_cliente"
    id=Column(Integer, primary_key=True)
    cliente_id= Column(Integer,ForeignKey('cliente.id'))
    livro_id = Column(Integer,ForeignKey('livro.id'))

    #RELATIONSHIPS
    cliente = relationship("Cliente", back_populates = "livro")
    livros = relationship("Livro", back_populates = "livros")


class Livrarias(Base):
    __tablename__="livrarias"
    id=Column(Integer, primary_key=True)
    nome = Column(String(256),nullable= False, unique = False)
    
    #RELATIONSHIPS
    #livro = relationship("Livro", back_populates = "livraria")
    detalhes = relationship("Livraria_Livro", back_populates = "livraria")



class Livro(Base):
    __tablename__="livro"
    id=Column(Integer, primary_key=True)
    titulo = Column(String(256),nullable= False, unique = False)
    ano= Column(Integer,nullable= False, unique = False)
    nome_autor= Column(String(256),nullable= False, unique = False)
    isbn = Column(String(256),nullable= False, unique = False)
    editora_id=Column(Integer,ForeignKey('editora.id'))
    assunto = Column(String(256),nullable= False, unique = False)

    #RELATIONSHIPS
    #livraria = relationship("Livrarias", back_populates = "livro")
    editora = relationship("Editora", back_populates = "livros")
    detalhes = relationship("Livraria_Livro", back_populates = "livro")
    livros = relationship("Livro_Cliente", back_populates = "livros")


class Editora(Base):
    __tablename__ = "editora"
    id=Column(Integer, primary_key=True)
    nome = Column(String(256),nullable= False, unique = False)

    #RELATIONSHIPS
    
    livros = relationship("Livro", back_populates = "editora")



class Cliente(Base):
    __tablename__ = "cliente"
    id=Column(Integer, primary_key=True)
    cpf = Column(String(256),nullable= False, unique = True)
    nome = Column(String(256), nullable= False, unique = False)
    data_nascimento = Column(String(256),nullable= False, unique = False)
    endereco_id = Column(Integer,ForeignKey('endereco.id'))

    #RELATIONSHIPS
    endereco = relationship("Endereco", back_populates = "cliente")
    livro = relationship("Livro_Cliente", back_populates = "cliente")


class Endereco(Base):
    __tablename__ = "endereco"
    id=Column(Integer, primary_key=True)
    cep = Column(String(256),nullable= False, unique = False)
    logradouro = Column(String(256),nullable= False, unique = False)
    numero = Column(Integer, nullable = False , unique = False)
    complemento = Column(String(256),nullable= False, unique = False)
    cidade_id = Column(Integer,ForeignKey('cidade.id'))
    estado_id = Column(Integer,ForeignKey('estado.id'))
    pais_id = Column(Integer,ForeignKey('pais.id'))

    #RELATIONSHIPS
    cliente = relationship("Cliente", back_populates = "endereco")
    cidade = relationship("Cidade", back_populates = "endereco")
    estado = relationship("Estado", back_populates = "endereco")
    pais = relationship("Pais", back_populates = "endereco")


class Cidade(Base):
    __tablename__="cidade"
    id=Column(Integer, primary_key=True)
    sigla= Column(String(256), nullable= False, unique = False)
    nome = Column(String(256), nullable= False, unique = False)
    
    
    #RELATIONSHIPS
    endereco = relationship("Endereco", back_populates = "cidade")
    

class Estado(Base):
    __tablename__="estado"
    id=Column(Integer, primary_key=True)
    sigla= Column(String(256), nullable= False, unique = False)
    nome = Column(String(256), nullable= False, unique = False)
    
    
    #RELATIONSHIPS
    endereco = relationship("Endereco", back_populates = "estado")
 
class Pais(Base):
    __tablename__="pais"
    id=Column(Integer, primary_key=True)
    sigla= Column(String(256), nullable= False, unique = False)
    nome = Column(String(256), nullable= False, unique = False)
    
   
    #RELATIONSHIPS
    endereco = relationship("Endereco", back_populates = "pais")

