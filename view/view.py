class Visao:
    def exibir_contador(self, contador):
        print(f"Contador atual: {contador}")

    def exibir_menu(self):
        print("\nSelecione uma ação:")
        print("1 - Clique")
        print("2 - Resetar")
        print("3 - Sair")
        return input("Opção: ")
