#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#----------------------------------------------------------------------------
# Created By  : Tiago Sanches da Silva e Fabio Miranda - https://github.com/Tiagoeem | https://github.com/mirwox
# Created Date: 15/08/2022
# version ='1.0'
# ---------------------------------------------------------------------------

from classes.Endereco import Endereco
import re


class PessoaFisica:
    '''Esta classe implementa uma pessoa no contexto de uma compra em e-commerce.
    
    As propriedades email e cpf estão privadas para previnir o usuário da classe de 
    acessar e alterar diretamente a propriedade sem uma verificação.
    '''
    lista = []
    def __init__(self, cpf, email, nome='Visitante'):
        self.nome = nome
        self.__email = email
        self.__cpf = cpf
        self.__enderecos = {}
        PessoaFisica.lista.append(self)

    # escolher o estilo de retorno

    def __str__(self) :
        return f'{self.nome} | {self.__cpf} | {self.__email}'
    

    def adicionar_endereco(self, apelido_endereco, end:Endereco):
        self.apelido = apelido_endereco
        self.__end = end
        self.__enderecos[f'{self.apelido}'] = self.__end
        

    def remover_endereco(self, apelido_endereco):

        del self.__enderecos[f'{apelido_endereco}']
        
        

    def get_endereco(self, apelido_endereco):
        return self.__enderecos[f'{apelido_endereco}']
    

    def listar_enderecos(self):
        enderecos = [a for a in self.__enderecos]
        return enderecos

    def busca_nome (busca) :

        resultados = []
        for pessoa in PessoaFisica.lista :
            if busca.upper() in pessoa.nome.upper():
                resultados.append(pessoa)
        return resultados

    def __eq__(self, outro):
        if isinstance(outro, PessoaFisica) :
            if self.__cpf == outro.__cpf :
                return True
    


    
         
     
        
            

    