import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

# Criando a janela principal(a função TK é paracriar uma janela)
janela = tk.Tk()
janela.geometry("800x600")
janela.title("Cadastro de Pet")
janela.config(bg="#f0f0f0")  # Cor de fundo mais clara

# Definindo uma fonte personalizada
font_title = ("Helvetica", 16, "bold")
font_labels = ("Arial", 12)

# Criando um frame centralizado para organizar melhor os widgets
frame = ttk.Frame(janela, padding="20")
frame.pack(expand=True)

# Título centralizado
titulo = ttk.Label(frame, text="Cadastro de Cliente e Pet", font=("Helvetica", 20, "bold"))
titulo.grid(row=0, column=0, columnspan=2, pady=20)

# Label e campo de entrada para o nome do tutor
labelNomeTutor = ttk.Label(frame, text="Nome do Tutor", font=font_labels)
labelNomeTutor.grid(row=1, column=0, sticky="e", padx=10, pady=5)
entryNomeTutor = ttk.Entry(frame, width=40, font=("Arial", 12))
entryNomeTutor.grid(row=1, column=1, padx=10, pady=5)

# Label e campo de entrada para o nome do pet
labelNomePet = ttk.Label(frame, text="Nome do Pet", font=font_labels)
labelNomePet.grid(row=2, column=0, sticky="e", padx=10, pady=5)
entryNomePet = ttk.Entry(frame, width=40, font=("Arial", 12))
entryNomePet.grid(row=2, column=1, padx=10, pady=5)

# Função para cadastrar(def: é uma função personalizada)
def cadastrar():
    nome_tutor = entryNomeTutor.get()
    nome_pet   = entryNomePet.get()
    #messagebox.showinfo("Cadastrado:"," Tutor: " +nome_tutor+ " Pet: " +nome_pet)
    messagebox.showinfo("Cadastrado:",f" Tutor: {nome_tutor} \n Pet: {nome_pet}")

# Botão para submeter o cadastro
botaoCadastrar = ttk.Button(frame, text="Cadastrar", command=cadastrar, width=20)
botaoCadastrar.grid(row=3, column=0, columnspan=2, pady=20)

# Rodapé com informações adicionais
rodape = ttk.Label(janela, text="© 2025 Cadastro de Pets", font=("Arial", 10), anchor="center")
rodape.pack(side="bottom", fill="x", pady=10)

# Iniciando a interface gráfica
janela.mainloop()
