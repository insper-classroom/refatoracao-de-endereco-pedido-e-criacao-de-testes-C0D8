import pytest
from classes.PessoaFisica import PessoaFisica
from classes.Endereco import Endereco



def test_adicionar_endereco () :
    end = Endereco(23555063, 37)
    p = PessoaFisica('00000000000', 'teste@gmail.com')
    p.adicionar_endereco('casa', end)
    assert end == p.get_endereco('casa')


def test_remover_endereco () :
    end = Endereco(23555063, 37)
    p = PessoaFisica('00000000000', 'teste@gmail.com')
    p.adicionar_endereco('casa', end)
    p.remover_endereco('casa')
    assert len(p.listar_enderecos()) == 0 


def test_listar_enderecos ():

    end = Endereco(23555063, 37)
    p = PessoaFisica('00000000000', 'teste@gmail.com')
    p.adicionar_endereco('casa', end)
    assert ['casa'] == p.listar_enderecos()


def test_buscar_pessoa_capslok () :
    p = PessoaFisica('00000000000', 'teste@gmail.com', 'Matheus')
    r = PessoaFisica.busca_nome('MATHEUS')
    assert r[0] == p 

def test_buscar_pessoa_lowercase () :
    p = PessoaFisica('00000000000', 'teste@gmail.com', 'Matheus')
    r = PessoaFisica.busca_nome('matheus')
    assert r[0] == p 

def test_buscar_pessoa_busca_com_nome_incompleto () :
    
    p = PessoaFisica('00000000000', 'teste@gmail.com', 'Matheus')
    r = PessoaFisica.busca_nome('math')
    assert r[0] == p 


def test_buscar_pessoa_misto_completo () :
    
    p = PessoaFisica('00000000000', 'teste@gmail.com', 'Matheus')
    r = PessoaFisica.busca_nome('MaThEUs')
    assert r[0] == p 


def test_buscar_pessoa_misto_incompleto () :
    
    p = PessoaFisica('00000000000', 'teste@gmail.com', 'Matheus')
    r = PessoaFisica.busca_nome('MaThE')
    assert r[0] == p 




