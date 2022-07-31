from datetime import date
from multiprocessing.managers import BaseManager
from pydantic import BaseModel, ValidationError
from typing import List 

class Livraria_Livro(BaseModel):
    livraria_id:int
    livro_id:int
    quantidade_estoque: int
    valor: float
    prazo_entrega: str

    class Config:
        orm_mode= True



class Livrarias(BaseModel):
    id:int
    nome: str

    class Config:
        orm_mode= True


class Livro(BaseModel):
    id: int
    titulo: str
    ano: int
    nome_autor: str
    isbn: str
    editora_id: int
    assunto: str

    class Config:
        orm_mode= True

class Editora(BaseModel):
    id: int
    nome: str

    class Config:
        orm_mode= True


class Cliente(BaseModel):
    id:int
    cpf: str
    nome: str
    data_nascimento: str
    endereco_id: int

    class Config:
        orm_mode= True


class Endereco(BaseModel):
    id: int
    cep: str
    logradouro: str
    numero: int
    complemento: str
    cidade_id: int
    estado_id: int
    pais_id: int

    class Config:
        orm_mode= True

class Cidade(BaseModel):
    id: int
    sigla: str
    nome: str

    class Config:
        orm_mode= True

class Estado(BaseModel):
    id: int
    sigla: str
    nome: str
    
    class Config:
        orm_mode= True


class Pais(BaseModel):
    id: int
    sigla: str
    nome: str
    
    class Config:
        orm_mode= True


#CLASSES DE SAÍDA
class Livraria_Livro_Details(BaseModel):
    quantidade_estoque: int
    valor: float
    prazo_entrega:str

    class Config:
       orm_mode= True


class Livraria_Livro_Livrarias(BaseModel):
    livraria:Livrarias
    quantidade_estoque: int
    valor: float
    prazo_entrega:str

    class Config:
       orm_mode= True

class Livro_Out(BaseModel):
    titulo: str
    ano: int
    nome_autor: str
    isbn: str
    editora: Editora
    assunto: str
    detalhes:List[Livraria_Livro_Livrarias]

    class Config:
        orm_mode= True


class Livro_Out_Details(BaseModel):
    titulo: str
    ano: int
    nome_autor: str
    isbn: str
    editora: Editora
    assunto: str
    detalhes:List[Livraria_Livro_Details]

    class Config:
        orm_mode= True

class Livraria_Livro_Out_Books(BaseModel):
    livro:Livro_Out_Details
    quantidade_estoque: int
    valor: float
    prazo_entrega:str

    class Config:
       orm_mode= True


class Editora_Out(BaseModel):
    nome: str
    livros: List[Livro_Out]

    class Config:
        orm_mode= True

class Livrarias_Out(BaseModel):
    nome:str
    detalhes:List[Livraria_Livro_Out_Books]

    class Config:
       orm_mode= True


class Endereco_Out(BaseModel):
    cep: str
    logradouro: str
    numero: int
    complemento: str
    cidade: Cidade
    estado: Estado
    pais: Pais

    class Config:
      orm_mode= True


class Cliente_Out(BaseModel):
    nome: str
    endereco: Endereco_Out

    class Config:
       orm_mode= True

