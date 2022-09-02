#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#----------------------------------------------------------------------------
# Created By  : Tiago Sanches da Silva e Fabio Miranda - https://github.com/Tiagoeem | https://github.com/mirwox
# Created Date: 15/08/2022
# version ='1.0'
# ---------------------------------------------------------------------------


class Produto:
    lista = []

    def __init__(self, id_produto, nome_produto=''):
        self.__id = id_produto
        self.__nome = nome_produto
        Produto.lista.append(self)

    def __eq__(self, outro):
        if isinstance(outro, Produto):
            if outro.get_id() == self.__id :
                return True
        pass

    def set_id (self, novo_id):
        self.__id = novo_id

    def get_id (self):
        return self.__id


    # def set_nome (self, novo_nome):
    #     self.__nome = novo_nome

    # def get_nome (self):
    #     return self.__nome

    def __str__ (self) :
        return f'''{self.__nome} | {self.__id}'''  # Optei por printar o id do produto ao invés do nome dele em si.

    @property
    def nome(self):
        return self.__nome
    
    @nome.setter
    def nome (self, novo_nome) :

        if novo_nome[0] != 'T' :
            self.__nome = novo_nome
    
    # @nome.getter
    # def nome (self) :
    #     return self.__nome
    def busca_nome (busca) :

        resultados = []
        for produto in Produto.lista :
            if busca.upper() in produto.__nome.upper():
                resultados.append(produto)
        return resultados
    