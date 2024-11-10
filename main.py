from controller.controller import Controlador
from model.model import Modelo
from view.view import Visao

if __name__ == "__main__":
    modelo = Modelo()
    visao = Visao()
    controlador = Controlador(modelo, visao)
    controlador.executar()
