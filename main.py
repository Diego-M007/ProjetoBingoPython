# A classe agora é o nosso "cérebro", guardando os números e as operações.
class BingoGame:
    def __init__(self):
        """Este método é executado quando o jogo é criado.
        Ele cria a lista de números que pertence a ESTE jogo."""
        self.numeros = []

    def adicionar_numero(self):
        """Adiciona um número à lista do jogo."""
        try:
            # try...except para evitar que o programa quebre se o usuário digitar texto
            numero_novo = int(input("Digite um número: "))
            if numero_novo in self.numeros:
                print(f"O número {numero_novo} já foi sorteado. Tente outro.")
            else:
                self.numeros.append(numero_novo)
                print(f"Número {numero_novo} adicionado!")
        except ValueError:
            print("Erro: Por favor, digite um número válido.")

    def remover_numero(self):
        """Remove um número da lista do jogo."""
        if not self.numeros: # Verifica se a lista não está vazia
            print("A lista de números está vazia. Não há o que remover.")
            return

        try:
            numero_remover = int(input("Digite o número a ser removido: "))
            if numero_remover in self.numeros:
                self.numeros.remove(numero_remover)
                print(f"Número {numero_remover} removido com sucesso.")
            else:
                print("Esse número não está na lista.")
        except ValueError:
            print("Erro: Por favor, digite um número válido.")

    def limpar_lista(self):
        """Limpa a lista de números para um novo jogo."""
        # Usando um loop para garantir que o usuário digite 's' ou 'n'
        while True:
            confirmacao = input("Deseja realmente limpar a lista? (s/n): ").lower()
            if confirmacao == "s":
                self.numeros.clear()
                print("A lista de números foi reiniciada.")
                break # Sai do loop
            elif confirmacao == "n":
                print("Operação cancelada.")
                break # Sai do loop
            else:
                print("Opção inválida. Digite 's' para sim ou 'n' para não.")

    def ver_ultimos_5_numeros(self):
        """Mostra os últimos 5 números sorteados."""
        if not self.numeros: # Verifica se a lista não está vazia
            print("Nenhum número foi sorteado ainda.")
            return
        
        # O fatiamento [-5:] funciona de forma segura mesmo com menos de 5 números
        print(f"Últimos 5 números sorteados: {self.numeros[-5:]}")

    def ver_ultimo_numero(self):
        """Mostra o último número sorteado."""
        if not self.numeros: # Verifica se a lista não está vazia
            print("Nenhum número foi sorteado ainda.")
            return

        print(f"Último número sorteado: {self.numeros[-1]}")

    def ver_todos_os_numeros(self):
        """Mostra todos os números sorteados em ordem crescente."""
        if not self.numeros:
            print("A lista de números está vazia.")
        else:
            # Usar sorted() para mostrar em ordem sem alterar a lista original
            print(f"Todos os números sorteados: {sorted(self.numeros)}")

# --- FUNÇÕES DO MENU E LOOP PRINCIPAL ---

def exibir_menu():
    """Apenas exibe as opções para o usuário."""
    print("\n" + "-"*30)
    print("Opções do Bingo")
    print("1 - Adicionar número")
    print("2 - Remover número")
    print("3 - Reiniciar jogo (limpar lista)")
    print("4 - Ver últimos 5 números")
    print("5 - Ver último número")
    print("6 - Ver todos os números")
    print("7 - Sair do Sistema")
    print("-"*30)

# --- PROGRAMA PRINCIPAL ---

# 1. Criamos uma instância do nosso jogo.
# Agora todas as informações ficam guardadas dentro do objeto 'jogo'.
jogo = BingoGame()

while True:
    exibir_menu()
    
    # 2. Tratamento de erro para a escolha da opção
    try:
        opcao = int(input("Escolha uma opção: "))
    except ValueError:
        print("\nOpção inválida! Por favor, digite um número de 1 a 7.")
        continue # Volta para o início do loop

    # 3. As chamadas agora são "métodos" do nosso objeto 'jogo'
    if opcao == 1:
        jogo.adicionar_numero()
    elif opcao == 2:
        jogo.remover_numero()
    elif opcao == 3:
        jogo.limpar_lista()
    elif opcao == 4:
        jogo.ver_ultimos_5_numeros()
    elif opcao == 5:
        jogo.ver_ultimo_numero()
    elif opcao == 6:
        jogo.ver_todos_os_numeros()
    elif opcao == 7:
        print("\nObrigado por usar o sistema de Bingo! Até a próxima!")
        break
    else:
        print("\nOpção inválida! Por favor, digite um número de 1 a 7.")