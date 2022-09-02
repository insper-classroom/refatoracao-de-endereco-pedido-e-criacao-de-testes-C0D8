import pytest
from classes.Produto import Produto 

def test_buscar_produto_capslok () :
    p = Produto(123, 'teste')
    r = Produto.busca_nome('TESTE')
    assert r[0] == p 

def test_buscar_produto_lowercase () :
    p = Produto(123, 'teste')
    r = Produto.busca_nome('teste')
    assert r[0] == p 

def test_buscar_produto_busca_com_nome_incompleto () :
    
    p = Produto(123, 'teste')
    r = Produto.busca_nome('Tes')
    assert r[0] == p 


def test_buscar_produto_misto_completo () :
    
    p = Produto(123, 'teste')
    r = Produto.busca_nome('TeStE')
    assert r[0] == p 

def test_buscar_produto_misto_incompleto () :
    
    p = Produto(123, 'teste')
    r = Produto.busca_nome('TeSt')
    assert r[0] == p 


def test_criar_produto_sem_id ():
    with pytest.raises(TypeError) as excinfo :
        p = Produto()
    assert "missing 1 required positional argument" in str(excinfo.value)
        