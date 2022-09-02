import pytest 
from classes.Pedido import Pedido 




def test_criar_pedido_sem_parametros_obrigatorios () :
    with pytest.raises(TypeError) as excinfo :

        p = Pedido()
    assert "missing 2 required positional argument" in str(excinfo.value)


