
import requests
from classes.Endereco import Endereco
import pytest





def test_quantidade_de_numeros_errada ():

    cep = 123456789456456

    assert Endereco.consultar_cep(cep) == False

def test_cep_como_string ():
    
    cep = '23555063'
    consulta = Endereco.consultar_cep(cep) 

    assert consulta['logradouro'] == 'Rua Fomento'


def test_endereco_sem_numero ():

    
    cep = '23555063'

    with pytest.raises(TypeError) as excinfo:

        end = Endereco(cep)
    assert "missing 1 required positional argument" in str(excinfo.value)

def test_endereco_sem_cep ():


    with pytest.raises(TypeError) as excinfo:

        end = Endereco(numero=37)
    assert "missing 1 required positional argument" in str(excinfo.value)



def test_cep_como_int ():
    
    cep = 23555063
    endereco = Endereco(cep,37)
    
    assert endereco.rua == 'Rua Fomento'

def test_cep_como_int_comecando_com_zero ():
    
    cep = 4552040
    endereco = Endereco(cep,37)

    assert endereco.rua == "Rua Elvira Ferraz"
    
    
    

def test_cep_inexistente ():

    cep = 99999999
    
    assert Endereco.consultar_cep(cep) == False
        
@pytest.mark.net
def test_sem_conexao ():
    

    with pytest.raises(requests.exceptions.ConnectionError) as exinfo:

        Endereco(23555063, 37)
    assert "Failed to establish a new connection" in str(exinfo.value)

