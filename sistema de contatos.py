import tkinter as tk
from tkinter import messagebox, ttk, simpledialog
from datetime import datetime
import json
import os
import re

def validar_data(data_str):
    try:
        datetime.strptime(data_str, "%d/%m/%Y")
        return True
    except ValueError:
        return False

def validar_whatsapp(numero):
    numero = re.sub(r'[^\d]', '', numero)
    return len(numero) >= 10 and len(numero) <= 13

def limpar_campos():
    nome_entry.delete(0, tk.END)
    data_entry.delete(0, tk.END)
    whatsapp_entry.delete(0, tk.END)
    linkedin_entry.delete(0, tk.END)
    github_entry.delete(0, tk.END)
    tree.selection_remove(tree.selection())

def preencher_campos_selecionados(event):
    selecionado = tree.selection()
    if selecionado:
        item = tree.item(selecionado)
        valores = item['values']
        
        limpar_campos()
        
        nome_entry.insert(0, valores[1])
        data_entry.insert(0, valores[2])
        whatsapp_entry.insert(0, valores[3] if valores[3] != "Não informado" else "")
        linkedin_entry.insert(0, valores[4] if valores[4] != "Não informado" else "")
        github_entry.insert(0, valores[5] if valores[5] != "Não informado" else "")

def adicionar_contato():
    global id_counter
    nome = nome_entry.get().strip()
    data_nasc = data_entry.get().strip()
    whatsapp = whatsapp_entry.get().strip()
    linkedin = linkedin_entry.get().strip()
    github = github_entry.get().strip()
    
    if not nome:
        messagebox.showerror("Erro", "O campo Nome é obrigatório!")
        return
    
    if data_nasc and not validar_data(data_nasc):
        messagebox.showerror("Erro", "Data de nascimento inválida! Use o formato DD/MM/AAAA.")
        return
    
    if whatsapp and not validar_whatsapp(whatsapp):
        messagebox.showerror("Erro", "Número de WhatsApp inválido!")
        return
    
    contatos[id_counter] = {
        "nome": nome,
        "data_nascimento": data_nasc if data_nasc else "Não informado",
        "whatsapp": whatsapp if whatsapp else "Não informado",
        "linkedin": linkedin if linkedin else "Não informado",
        "github": github if github else "Não informado"
    }
    
    id_counter += 1
    salvar_dados()
    messagebox.showinfo("Sucesso", "Contato adicionado com sucesso!")
    limpar_campos()
    atualizar_treeview()

def atualizar_contato():
    selecionado = tree.selection()
    if not selecionado:
        messagebox.showerror("Erro", "Nenhum contato selecionado!")
        return
    
    id_contato = int(tree.item(selecionado)['values'][0])
    
    nome = nome_entry.get().strip()
    data_nasc = data_entry.get().strip()
    whatsapp = whatsapp_entry.get().strip()
    linkedin = linkedin_entry.get().strip()
    github = github_entry.get().strip()
    
    if not nome:
        messagebox.showerror("Erro", "O campo Nome é obrigatório!")
        return
    
    if data_nasc and not validar_data(data_nasc):
        messagebox.showerror("Erro", "Data de nascimento inválida! Use o formato DD/MM/AAAA.")
        return
    
    contatos[id_contato] = {
        "nome": nome,
        "data_nascimento": data_nasc if data_nasc else "Não informado",
        "whatsapp": whatsapp if whatsapp else "Não informado",
        "linkedin": linkedin if linkedin else "Não informado",
        "github": github if github else "Não informado"
    }
    
    salvar_dados()
    messagebox.showinfo("Sucesso", "Contato atualizado com sucesso!")
    limpar_campos()
    atualizar_treeview()

def excluir_contato():
    """Função para excluir um contato selecionado na Treeview"""
    selecionado = tree.selection()
    if not selecionado:
        messagebox.showerror("Erro", "Nenhum contato selecionado!")
        return
    
    try:
        # Obtém o ID do contato selecionado
        id_contato = int(tree.item(selecionado)['values'][0])
        
        # Verifica se o contato existe
        if id_contato not in contatos:
            messagebox.showerror("Erro", "Contato não encontrado!")
            return
            
        # Pede confirmação
        resposta = messagebox.askyesno(
            "Confirmar Exclusão",
            f"Tem certeza que deseja excluir o contato:\n\n"
            f"Nome: {contatos[id_contato]['nome']}\n"
            f"ID: {id_contato}"
        )
        
        if resposta:
            # Remove o contato
            del contatos[id_contato]
            salvar_dados()
            messagebox.showinfo("Sucesso", "Contato excluído com sucesso!")
            
            # Atualiza a interface
            limpar_campos()
            atualizar_treeview()
            
    except Exception as e:
        messagebox.showerror("Erro", f"Falha ao excluir contato: {str(e)}")

def excluir_contato_teclado(event):
    """Função para excluir com a tecla Delete"""
    excluir_contato()

def localizar_contato():
    termo = simpledialog.askstring("Localizar", "Digite o nome ou parte do nome:")
    if termo:
        termo = termo.lower()
        encontrados = False
        
        for item in tree.get_children():
            tree.delete(item)
        
        for id_contato, contato in contatos.items():
            if termo in contato['nome'].lower():
                tree.insert("", tk.END, values=(
                    id_contato,
                    contato['nome'],
                    contato['data_nascimento'],
                    contato['whatsapp'],
                    contato['linkedin'],
                    contato['github']
                ))
                encontrados = True
        
        if not encontrados:
            messagebox.showinfo("Localizar", "Nenhum contato encontrado com esse termo.")
            atualizar_treeview()

def mostrar_todos_contatos():
    # Remove todos os itens existentes na Treeview
    for item in tree.get_children():
        tree.delete(item)
    
    # Insere todos os contatos na Treeview
    for id_contato, contato in sorted(contatos.items(), key=lambda item: item[1]['nome']):
        tree.insert("", tk.END, values=(
            id_contato,
            contato['nome'],
            contato['data_nascimento'],
            contato['whatsapp'],
            contato['linkedin'],
            contato['github']
        ))

def salvar_dados():
    with open('contatos.json', 'w') as f:
        json.dump({'contatos': contatos, 'id_counter': id_counter}, f)

def carregar_dados():
    global contatos, id_counter
    if os.path.exists('contatos.json'):
        with open('contatos.json', 'r') as f:
            data = json.load(f)
            contatos = data.get('contatos', {})
            id_counter = data.get('id_counter', 1)

def atualizar_treeview():
    for item in tree.get_children():
        tree.delete(item)
    
    for id_contato, contato in sorted(contatos.items(), key=lambda item: item[1]['nome']):
        tree.insert("", tk.END, values=(
            id_contato,
            contato['nome'],
            contato['data_nascimento'],
            contato['whatsapp'],
            contato['linkedin'],
            contato['github']
        ))

# Configuração inicial
root = tk.Tk()
root.title("Sistema de Contatos")
root.geometry("900x650")

# Base de dados
contatos = {}
id_counter = 1
carregar_dados()

# Interface gráfica
main_frame = tk.Frame(root, padx=20, pady=20)
main_frame.pack(fill=tk.BOTH, expand=True)

# Frame de formulário
form_frame = tk.LabelFrame(main_frame, text="Dados do Contato", padx=10, pady=10)
form_frame.pack(fill=tk.X, pady=(0, 10))

# Campos do formulário
tk.Label(form_frame, text="Nome:").grid(row=0, column=0, sticky=tk.W)
nome_entry = tk.Entry(form_frame, width=50)
nome_entry.grid(row=0, column=1, padx=5, pady=5)

tk.Label(form_frame, text="Data Nasc. (DD/MM/AAAA):").grid(row=1, column=0, sticky=tk.W)
data_entry = tk.Entry(form_frame, width=50)
data_entry.grid(row=1, column=1, padx=5, pady=5)

tk.Label(form_frame, text="WhatsApp:").grid(row=2, column=0, sticky=tk.W)
whatsapp_entry = tk.Entry(form_frame, width=50)
whatsapp_entry.grid(row=2, column=1, padx=5, pady=5)

tk.Label(form_frame, text="LinkedIn:").grid(row=3, column=0, sticky=tk.W)
linkedin_entry = tk.Entry(form_frame, width=50)
linkedin_entry.grid(row=3, column=1, padx=5, pady=5)

tk.Label(form_frame, text="GitHub:").grid(row=4, column=0, sticky=tk.W)
github_entry = tk.Entry(form_frame, width=50)
github_entry.grid(row=4, column=1, padx=5, pady=5)

# Frame de botões
button_frame = tk.Frame(main_frame)
button_frame.pack(fill=tk.X, pady=(0, 10))

tk.Button(button_frame, text="Adicionar", width=15, command=adicionar_contato).grid(row=0, column=0, padx=5)
tk.Button(button_frame, text="Atualizar", width=15, command=atualizar_contato).grid(row=0, column=1, padx=5)
tk.Button(button_frame, text="Excluir", width=15, command=excluir_contato).grid(row=0, column=2, padx=5)
tk.Button(button_frame, text="Limpar", width=15, command=limpar_campos).grid(row=0, column=3, padx=5)
tk.Button(button_frame, text="Localizar", width=15, command=localizar_contato).grid(row=0, column=4, padx=5)
tk.Button(button_frame, text="Todos", width=15, command=mostrar_todos_contatos).grid(row=0, column=5, padx=5)

# Configuração da Treeview
tree = ttk.Treeview(main_frame, columns=("ID", "Nome", "Nascimento", "WhatsApp", "LinkedIn", "GitHub"), 
                   show="headings", selectmode="browse")

# Configuração dos cabeçalhos
colunas = [
    ("ID", 50),
    ("Nome", 200),
    ("Nascimento", 100),
    ("WhatsApp", 150),
    ("LinkedIn", 200),
    ("GitHub", 200)
]

for col, width in colunas:
    tree.heading(col, text=col)
    tree.column(col, width=width, anchor=tk.W)

tree.pack(fill=tk.BOTH, expand=True)

# Barra de rolagem
scrollbar = ttk.Scrollbar(tree, orient="vertical", command=tree.yview)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
tree.configure(yscrollcommand=scrollbar.set)

# Vinculação de eventos
tree.bind("<<TreeviewSelect>>", preencher_campos_selecionados)
root.bind("<Delete>", excluir_contato_teclado)

# Barra de status
status_bar = tk.Label(root, text="Pronto", bd=1, relief=tk.SUNKEN, anchor=tk.W)
status_bar.pack(side=tk.BOTTOM, fill=tk.X)

root.mainloop()