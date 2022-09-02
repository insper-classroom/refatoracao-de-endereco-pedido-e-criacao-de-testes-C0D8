import pytest 
from classes.Carrinho import Carrinho
from classes.Produto import Produto



def test_adicionar_item () :

    produto = Produto(123, 'papel')
    carrinho = Carrinho() 
    carrinho.adicionar_item(produto, 12)
    assert carrinho.itens == {'123' : 12}


@pytest.mark.remover
def test_remover_item () :

    produto = Produto(123, 'papel')
    carrinho = Carrinho() 
    carrinho.adicionar_item(produto, 12)
    carrinho.remover_item(produto.get_id())
    assert carrinho.itens == {}
