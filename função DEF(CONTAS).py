import tkinter as tk #"as" atribui um apelido ao import.
import tkinter as ttk
from tkinter import messagebox

janelaconta = tk.Tk()
janelaconta.title('Minha Calculadora')
janelaconta.geometry("800x600")



# Criando um frame centralizado para organizar melhor os widgets
frame = ttk.Frame(janelaconta, padding="20")
frame.pack(expand=True)

# Título centralizado
titulo = tk.Label(frame, text="Calculadora", font=("Helvetica", 20, "bold"))
titulo.grid(row=0, column=0, columnspan=2, pady=20)

labelnum1 = tk.Label(janelaconta, text="primeiro numero")
labelnum1.pack(padx=5,pady=10)
entrynum1 = tk.Entry(janelaconta)
entrynum1.pack(padx=5,pady=5)

labelnum2 = tk.Label(janelaconta, text="segundo numero")
labelnum2.pack(padx=5,pady=10)
entrynum2 = tk.Entry(janelaconta)
entrynum2.pack(padx=5,pady=5)

soma = float(entrynum1.get()) + float(entrynum2.get())
subtracao = float(entrynum1.get()) + float(entrynum2.get())
divisao = float(entrynum1.get()) + float(entrynum2.get())
multiplicacao = float(entrynum1.get()) + float(entrynum2.get())

# Função para Calcular(def: é uma função personalizada)
def Conta():
    soma          = entrynum1.get()
    subtracao     = entrynum2.get()
    divisao       = entrynum1.get()
    multiplicacao = entrynum2.get()
    #messagebox.showinfo("Cadastrado:"," Tutor: " +nome_tutor+ " Pet: " +nome_pet)
    messagebox.showinfo("Resultado:",f" Tutor: {nome_tutor} \n Pet: {nome_pet}")


# Botão para submeter o Soma.
botaoSoma = ttk.Button(frame, text="Soma", command=Conta, width=20)
botaoSoma.grid(row=3, column=0, columnspan=2, pady=20)

# Botão para submeter o Subtracao.
botaoSubtracao = ttk.Button(frame, text="Subtracao", command=Conta, width=20)
botaoSubtracao.grid(row=3, column=0, columnspan=2, pady=20)

# Botão para submeter o Divisao.
botaoDivisao = ttk.Button(frame, text="Divisao", command=Conta, width=20)
botaoDivisao.grid(row=3, column=0, columnspan=2, pady=20)

# Botão para submeter o Multiplicacao.
botaoMultiplicacao = ttk.Button(frame, text="Multiplicacao", command=Conta, width=20)
botaoMultiplicacao.grid(row=3, column=0, columnspan=2, pady=20)

janelaconta.mainloop()