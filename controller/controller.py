class Controlador:
    def __init__(self, modelo, visao):
        self.modelo = modelo
        self.visao = visao

    def executar(self):
        while True:
            self.visao.exibir_contador(self.modelo.obter_contador())
            opcao = self.visao.exibir_menu()

            if opcao == "1":
                self.modelo.incrementar()
            elif opcao == "2":
                self.modelo.resetar()
            elif opcao == "3":
                print("Saindo do programa...")
                break
            else:
                print("Opção inválida. Tente novamente.")
