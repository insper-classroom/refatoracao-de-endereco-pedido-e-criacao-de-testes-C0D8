from queue import PriorityQueue
import pytest
from classes.Endereco import Endereco 
from classes.Pedido import Pedido
from classes.PessoaFisica import PessoaFisica 
from classes.Carrinho import Carrinho
from classes.Produto import Produto



def test_criar_pedido_sem_parametros_obrigatorios () :
    with pytest.raises(TypeError) as excinfo :

        p = Pedido()
    assert "missing 2 required positional argument" in str(excinfo.value)


def test_criar_pedido_corretamente () :
    pessoa = PessoaFisica('00000000000', 'teste@gmail.com')
    end = Endereco(23555063, 37)
    produto = Produto(123)
    carrinho = Carrinho()

  
    pessoa.adicionar_endereco('Casa', end) 

    


    carrinho.adicionar_item(produto,23)
    

    pedido = Pedido(pessoa, carrinho, endereco_entrega=pessoa.listar_enderecos()[0])

    pass


