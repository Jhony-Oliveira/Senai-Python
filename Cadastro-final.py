import tkinter as tk
from tkinter import messagebox, ttk
from datetime import datetime
import re

def validar_nome(nome):
    """Valida se o nome contém apenas caracteres permitidos"""
    padrao = r'^[a-zA-ZÀ-ÿ\s\'-]+$'
    if re.match(padrao, nome):
        return True
    return False

def validar_whatsapp(numero):
    """Valida o número de WhatsApp no formato (XX) 99999-8888"""
    padrao = r'^\(\d{2}\) \d{5}-\d{4}$'
    if re.match(padrao, numero):
        return True
    return False

def validar_linkedin(perfil):
    """Valida o perfil do LinkedIn (formato básico: nome@linkedin.com)"""
    padrao = r'^[a-zA-Z0-9_.+-]+@linkedin\.com$'
    if re.match(padrao, perfil.lower()):
        return True
    return False

def validar_github(perfil):
    """Valida o perfil do GitHub (formato básico: nome@github.com)"""
    padrao = r'^[a-zA-Z0-9_.+-]+@github\.com$'
    if re.match(padrao, perfil.lower()):
        return True
    return False

def formatar_data(data_str):
    """Valida e formata a data para o formato dd/mm/aaaa."""
    if not data_str or data_str == "Não informado":
        return "Não informado"
    
    try:
        # Tenta converter a string para data
        data = datetime.strptime(data_str, "%d/%m/%Y")
        # Retorna a data formatada
        return data.strftime("%d/%m/%Y")
    except ValueError:
        messagebox.showerror("Erro", "Formato de data inválido! Use dd/mm/aaaa (ex: 12/04/2025).")
        return None

def atualizar_treeview():
    # Limpar treeview
    for item in tree.get_children():
        tree.delete(item)
    
    # Adicionar contatos ordenados por nome
    for id_contato, contato in sorted(contatos.items(), key=lambda item: item[1]['nome']):
        tree.insert("", tk.END, values=(
            id_contato,
            contato['nome'],
            contato['data_nascimento'],
            contato['whatsapp'],
            contato['linkedin'],
            contato['github']
        ))

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
    
    # Validar nome
    if not validar_nome(nome):
        messagebox.showerror("Erro", "Nome inválido! Use apenas letras, espaços, hífens e apóstrofos.")
        return
    
    # Formatar e validar a data
    data_formatada = formatar_data(data_nasc)
    if data_formatada is None:
        return
    
    # Validar WhatsApp
    if whatsapp and not validar_whatsapp(whatsapp):
        messagebox.showerror("Erro", "Formato de WhatsApp inválido! Use (XX) 99999-8888")
        return
    
    # Validar LinkedIn
    if linkedin and not validar_linkedin(linkedin):
        messagebox.showerror("Erro", "Formato de LinkedIn inválido! Use nome@linkedin.com")
        return
    
    # Validar GitHub
    if github and not validar_github(github):
        messagebox.showerror("Erro", "Formato de GitHub inválido! Use nome@github.com")
        return
    
    contatos[id_counter] = {
        "nome": nome,
        "data_nascimento": data_formatada,
        "whatsapp": whatsapp if whatsapp else "Não informado",
        "linkedin": linkedin if linkedin else "Não informado",
        "github": github if github else "Não informado"
    }
    
    id_counter += 1
    messagebox.showinfo("Sucesso", "Contato adicionado com sucesso!")
    limpar_campos()
    atualizar_treeview()

def atualizar_contato():
    selected_item = tree.selection()
    if not selected_item:
        messagebox.showerror("Erro", "Selecione um contato para atualizar!")
        return
    
    contato_id = tree.item(selected_item)['values'][0]
    
    nome = nome_entry.get().strip()
    data_nasc = data_entry.get().strip()
    whatsapp = whatsapp_entry.get().strip()
    linkedin = linkedin_entry.get().strip()
    github = github_entry.get().strip()
    
    if not nome:
        messagebox.showerror("Erro", "O campo Nome é obrigatório!")
        return
    
    # Validar nome
    if not validar_nome(nome):
        messagebox.showerror("Erro", "Nome inválido! Use apenas letras, espaços, hífens e apóstrofos.")
        return
    
    # Formatar e validar a data
    data_formatada = formatar_data(data_nasc)
    if data_formatada is None:
        return
    
    # Validar WhatsApp
    if whatsapp and not validar_whatsapp(whatsapp):
        messagebox.showerror("Erro", "Formato de WhatsApp inválido! Use (XX) 99999-8888")
        return
    
    # Validar LinkedIn
    if linkedin and not validar_linkedin(linkedin):
        messagebox.showerror("Erro", "Formato de LinkedIn inválido! Use nome@linkedin.com")
        return
    
    # Validar GitHub
    if github and not validar_github(github):
        messagebox.showerror("Erro", "Formato de GitHub inválido! Use nome@github.com")
        return
    
    contatos[contato_id] = {
        "nome": nome,
        "data_nascimento": data_formatada,
        "whatsapp": whatsapp if whatsapp else "Não informado",
        "linkedin": linkedin if linkedin else "Não informado",
        "github": github if github else "Não informado"
    }
    
    messagebox.showinfo("Sucesso", "Contato atualizado com sucesso!")
    limpar_campos()
    atualizar_treeview()

def limpar_campos():
    nome_entry.delete(0, tk.END)
    data_entry.delete(0, tk.END)
    whatsapp_entry.delete(0, tk.END)
    linkedin_entry.delete(0, tk.END)
    github_entry.delete(0, tk.END)

def preencher_campos_selecionados(event):
    item_selecionado = tree.selection()
    
    if item_selecionado:
        valores = tree.item(item_selecionado)['values']
        
        limpar_campos()
        
        nome_entry.insert(0, valores[1])
        data_entry.insert(0, valores[2])
        whatsapp_entry.insert(0, valores[3])
        linkedin_entry.insert(0, valores[4])
        github_entry.insert(0, valores[5])

def remover_contato():
    selected_item = tree.selection()
    if not selected_item:
        messagebox.showerror("Erro", "Selecione um contato para remover!")
        return
    
    contato_id = tree.item(selected_item)['values'][0]
    
    if messagebox.askyesno("Confirmação", "Tem certeza que deseja remover este contato?"):
        del contatos[contato_id]
        messagebox.showinfo("Sucesso", "Contato removido com sucesso!")
        limpar_campos()
        atualizar_treeview()

def localizar_contato():
    termo_busca = nome_entry.get().strip().lower()
    
    if not termo_busca:
        messagebox.showwarning("Aviso", "Digite um nome para buscar!")
        return
    
    for item in tree.selection():
        tree.selection_remove(item)
    
    encontrados = False
    
    for item in tree.get_children():
        nome = tree.item(item)['values'][1].lower()
        
        if termo_busca in nome:
            tree.selection_add(item)
            tree.focus(item)
            tree.see(item)
            encontrados = True
    
    if not encontrados:
        messagebox.showinfo("Busca", "Nenhum contato encontrado com esse nome.")

# Configuração inicial
root = tk.Tk()
root.title("Sistema de Contatos")
root.geometry("1000x600")

contatos = {}
id_counter = 1 

main_frame = tk.Frame(root, padx=20, pady=20)
main_frame.pack(fill=tk.BOTH, expand=True)

form_frame = tk.LabelFrame(main_frame, text="Dados do Contato", padx=10, pady=10)
form_frame.pack(fill=tk.X, pady=(0, 10))

tk.Label(form_frame, text="Nome (apenas letras e espaços):").grid(row=0, column=0, sticky=tk.W)
nome_entry = tk.Entry(form_frame, width=40)
nome_entry.grid(row=0, column=1, padx=5, pady=5)

tk.Label(form_frame, text="Data Nasc. (DD/MM/AAAA):").grid(row=1, column=0, sticky=tk.W)
data_entry = tk.Entry(form_frame, width=40)
data_entry.grid(row=1, column=1, padx=5, pady=5)

tk.Label(form_frame, text="WhatsApp (ex: (16) 99999-8888):").grid(row=2, column=0, sticky=tk.W)
whatsapp_entry = tk.Entry(form_frame, width=40)
whatsapp_entry.grid(row=2, column=1, padx=5, pady=5)

tk.Label(form_frame, text="LinkedIn (ex: nome@linkedIn.com):").grid(row=3, column=0, sticky=tk.W)
linkedin_entry = tk.Entry(form_frame, width=40)
linkedin_entry.grid(row=3, column=1, padx=5, pady=5)

tk.Label(form_frame, text="GitHub (ex: nome@github.com):").grid(row=4, column=0, sticky=tk.W)
github_entry = tk.Entry(form_frame, width=40)
github_entry.grid(row=4, column=1, padx=5, pady=5)

button_frame = tk.Frame(main_frame)
button_frame.pack(fill=tk.X, pady=(0, 15))

tk.Button(button_frame, text="Adicionar", width=21, command=adicionar_contato).grid(row=0, column=0, padx=15)
tk.Button(button_frame, text="Atualizar", width=21, command=atualizar_contato).grid(row=0, column=1, padx=15)
tk.Button(button_frame, text="Remover Contato", width=21, command=remover_contato).grid(row=0, column=2, padx=15)
tk.Button(button_frame, text="Limpar", width=21, command=limpar_campos).grid(row=0, column=3, padx=15)
tk.Button(button_frame, text="Localizar Contato", width=21, command=localizar_contato).grid(row=0, column=4, padx=15)

tree = ttk.Treeview(main_frame, columns=("ID", "Nome", "Nascimento", "WhatsApp", "LinkedIn", "GitHub"), show="headings")

tree.heading("ID", text="ID")
tree.heading("Nome", text="Nome")
tree.heading("Nascimento", text="Nascimento")
tree.heading("WhatsApp", text="WhatsApp")
tree.heading("LinkedIn", text="LinkedIn")
tree.heading("GitHub", text="GitHub")

tree.column("ID", width=50)
tree.column("Nome", width=150)
tree.column("Nascimento", width=100)
tree.column("WhatsApp", width=120)
tree.column("LinkedIn", width=150)
tree.column("GitHub", width=150)

tree.pack(fill=tk.BOTH, expand=True)

scrollbar = ttk.Scrollbar(tree, orient="vertical", command=tree.yview)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
tree.configure(yscrollcommand=scrollbar.set)

tree.bind("<<TreeviewSelect>>", preencher_campos_selecionados)

root.mainloop()