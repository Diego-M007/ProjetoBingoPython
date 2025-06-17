import customtkinter
from tkinter import messagebox

# A classe BingoGame continua a mesma
class BingoGame:
    def __init__(self):
        self.numeros = []

# As funções de handler continuam as mesmas
def atualizar_telas():
    # ... (o conteúdo desta função continua idêntico)
    # Lógica para os últimos 5 números
    ultimos5 = jogo.numeros[-5:]
    ultimos_5_numeros_texto = ", ".join(map(str, ultimos5))
    if not ultimos5:
        ultimos_5_numeros_texto = "..."
    label_ultimos_numeros.configure(text=ultimos_5_numeros_texto)
    
    # Lógica para o último número sorteado
    if jogo.numeros:
        ultimo_numero_texto = str(jogo.numeros[-1])
    else:
        ultimo_numero_texto = "..."
    label_ultimo_numero.configure(text=ultimo_numero_texto)
    
    # Lógica para o Textbox de todos os números
    textbox_todos_numeros.configure(state="normal")
    textbox_todos_numeros.delete("1.0", "end")
    todos_ordenados = sorted(jogo.numeros)
    texto_todos = ", ".join(map(str, todos_ordenados))
    # Vamos quebrar a linha a cada X caracteres para melhor leitura
    texto_formatado = ""
    for i in range(0, len(texto_todos), 60): # Quebra a linha a cada 60 caracteres
        texto_formatado += texto_todos[i:i+60] + "\n"
    textbox_todos_numeros.insert("1.0", texto_formatado)
    textbox_todos_numeros.configure(state="disabled")

def adicionar_numero_funcao():
    # ... (o conteúdo desta função continua idêntico)
    numero_texto = input_numero.get()
    if numero_texto.isdigit():
        numero = int(numero_texto)
        if numero not in jogo.numeros:
            jogo.numeros.append(numero)
            atualizar_telas()
        else:
            messagebox.showwarning("Atenção", f"O número {numero} já foi sorteado!")
    else:
        messagebox.showerror("Erro", f"'{numero_texto}' não é um número válido.")
    input_numero.delete(0, "end")

def Reiniciar_Bingo():
    # ... (o conteúdo desta função continua idêntico)
    resposta = messagebox.askyesno("Confirmar Reinício", "Tem certeza que deseja apagar todos os números e começar um novo jogo?")
    if resposta:
        jogo.numeros.clear()
        atualizar_telas()

# --- CONFIGURAÇÃO DA JANELA ---
customtkinter.set_appearance_mode("light")
PaginaPrincipal = customtkinter.CTk()

PaginaPrincipal.iconbitmap("icone.ico")

PaginaPrincipal.title("Bingo Festa Junina Matriz")
# Um tamanho inicial maior para o novo layout
PaginaPrincipal.geometry("800x600") 

jogo = BingoGame()

# ===================================================================
# NOVA ESTRUTURA COM GRID
# ===================================================================

# --- 1. CONFIGURANDO O COMPORTAMENTO DA GRADE ---
# Damos "peso" às colunas e linhas para que elas se expandam com a janela
PaginaPrincipal.grid_columnconfigure(0, weight=1) # Coluna da esquerda (todos os números)
PaginaPrincipal.grid_columnconfigure(1, weight=1) # Coluna da direita (último e últimos 5)
PaginaPrincipal.grid_rowconfigure(0, weight=1)    # Linha de cima
PaginaPrincipal.grid_rowconfigure(1, weight=1)    # Linha de baixo
PaginaPrincipal.grid_rowconfigure(2, weight=0)    # Linha do input (não expande)


# --- 2. WIDGETS (COMPONENTES VISUAIS) ---

# --- SEÇÃO DA ESQUERDA (TODOS OS NÚMEROS) ---
frame_esquerda = customtkinter.CTkFrame(PaginaPrincipal)
# sticky="nsew" faz o frame se esticar para preencher toda a célula da grade
frame_esquerda.grid(row=0, column=0, padx=10, pady=10, rowspan=2, sticky="nsew")

frame_esquerda.grid_rowconfigure(1, weight=1)
frame_esquerda.grid_columnconfigure(0, weight=1)

label_titulo_todos = customtkinter.CTkLabel(frame_esquerda, text="Todos os Números Sorteados", font=("Arial", 50, "bold"))
label_titulo_todos.grid(row=0, column=0, padx=10, pady=10)

textbox_todos_numeros = customtkinter.CTkTextbox(frame_esquerda, font=("Arial", 60))
textbox_todos_numeros.grid(row=1, column=0, padx=10, pady=10, sticky="nsew")
textbox_todos_numeros.configure(state="disabled")


# --- SEÇÃO DA DIREITA ---
frame_direita = customtkinter.CTkFrame(PaginaPrincipal)
frame_direita.grid(row=0, column=1, padx=10, pady=10, rowspan=2, sticky="nsew")
frame_direita.grid_rowconfigure(0, weight=1)
frame_direita.grid_rowconfigure(1, weight=1)
frame_direita.grid_columnconfigure(0, weight=1)


# SUB-SEÇÃO: ÚLTIMO NÚMERO (TOP-RIGHT)
frame_ultimo = customtkinter.CTkFrame(frame_direita, fg_color="#E0E0E0")
frame_ultimo.grid(row=0, column=0, padx=10, pady=10, sticky="nsew")
frame_ultimo.grid_rowconfigure(1, weight=1)
frame_ultimo.grid_columnconfigure(0, weight=1)

label_titulo_ultimo_numero = customtkinter.CTkLabel(frame_ultimo, text="Último Sorteado", font=("Arial", 50, "bold"))
label_titulo_ultimo_numero.grid(row=0, column=0, pady=(10,0))

label_ultimo_numero = customtkinter.CTkLabel(frame_ultimo, text="...", font=("Arial Black", 200), text_color="#2E2E2E")
label_ultimo_numero.grid(row=1, column=0, sticky="nsew")


# SUB-SEÇÃO: ÚLTIMOS 5 NÚMEROS (BOTTOM-RIGHT)
frame_ultimos5 = customtkinter.CTkFrame(frame_direita, fg_color="#E0E0E0")
frame_ultimos5.grid(row=1, column=0, padx=10, pady=10, sticky="nsew")
frame_ultimos5.grid_rowconfigure(1, weight=1)
frame_ultimos5.grid_columnconfigure(0, weight=1)

label_titulo_ultimos = customtkinter.CTkLabel(frame_ultimos5, text="Últimos 5 Sorteados", font=("Arial", 60, "bold"))
label_titulo_ultimos.grid(row=0, column=0, pady=(10,0))

label_ultimos_numeros = customtkinter.CTkLabel(frame_ultimos5, text="...", font=("Arial", 80), wraplength=350) # wraplength quebra a linha
label_ultimos_numeros.grid(row=1, column=0, sticky="nsew")


# --- SEÇÃO INFERIOR (INPUT E BOTÕES) ---
frame_input = customtkinter.CTkFrame(PaginaPrincipal)
frame_input.grid(row=2, column=0, columnspan=2, padx=10, pady=10, sticky="ew") # sticky="ew" para esticar apenas na horizontal

input_numero = customtkinter.CTkEntry(frame_input, placeholder_text="Digite o número sorteado", font=("Arial", 16), height=40)
input_numero.pack(side="left", fill="x", expand=True, padx=10, pady=10)

botao_adicionar = customtkinter.CTkButton(frame_input, text="Adicionar", command=adicionar_numero_funcao, height=40)
botao_adicionar.pack(side="left", padx=10, pady=10)

botao_reiniciar = customtkinter.CTkButton(frame_input, text="Reiniciar", command=Reiniciar_Bingo, fg_color="#D9534F", hover_color="#C9302C", height=40)
botao_reiniciar.pack(side="left", padx=10, pady=10)


# Chama a atualização inicial para que os textos de "..." apareçam
atualizar_telas()
PaginaPrincipal.mainloop()