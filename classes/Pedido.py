#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#----------------------------------------------------------------------------
# Created By  :
# Created Date:
# version ='1.0'
# ---------------------------------------------------------------------------

from classes.Endereco import Endereco
from classes.PessoaFisica import PessoaFisica
from classes.Carrinho import Carrinho
import re




class Pedido :
    EM_ABERTO = 1
    PAGO = 2
    def __init__ (self, pessoa:PessoaFisica, carrinho:Carrinho, endereco_entrega = '', endereco_faturamento = ''):
        self.nome = pessoa.nome
        self.enderecos = pessoa.listar_enderecos()
        self.itens = carrinho
        self.endereco_entrega = endereco_entrega
        self.endereco_faturamento = endereco_faturamento

    def __str__(self):
        return f'{self.nome} - endereco de endtrega: {self.endereco_entrega} / endereco da fatura: {self.endereco_faturamento} / itens: {self.itens}'    