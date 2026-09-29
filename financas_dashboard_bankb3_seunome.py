import tkinter as tk
from tkinter import messagebox, ttk

COLOR_AZUL_ESC = "#004d6e"  
COLOR_AZUL_MED = "#0081ab"  
COLOR_AZUL_CLA = "#00b1cd"  
COLOR_VERDE = "#a6c844"  
COLOR_ROSA = "#b83764"  
COLOR_AMARELO = "#edce01"  
COLOR_ACO = "#4a3336"  

saldo = 1000.00
cripto_btc = 0.0
historico = ["Saldo inicial depositado: R$ 1000.00"]


def atualizar_extrato():
    lst_extrato.delete(0, tk.END)
    for item in historico:
        lst_extrato.insert(tk.END, item)


def atualizar_tudo():
    lbl_saldo.config(text=f"Saldo Disponível: R$ {saldo:.2f}")
    lbl_btc.config(text=f"Seu Saldo BTC: {cripto_btc:.6f}")
    atualizar_extrato()


def creditar():
    global saldo
    try:
        v = float(ent_valor_conta.get())
        if v <= 0:
            messagebox.showwarning("Aviso", "Digite um valor positivo.")
            return

        saldo += v
        historico.append(f"Depósito: +R$ {v:.2f}")
        ent_valor_conta.delete(0, tk.END)
        atualizar_tudo()
    except ValueError:
        messagebox.showerror("Erro", "Valor inválido.")


def debitar():
    global saldo
    try:
        v = float(ent_valor_conta.get())
        if v <= 0:
            messagebox.showwarning("Aviso", "Digite um valor positivo.")
            return

        if v <= saldo:
            saldo -= v
            historico.append(f"Saque/Pagamento: -R$ {v:.2f}")
            ent_valor_conta.delete(0, tk.END)
            atualizar_tudo()
        else:
            messagebox.showwarning("Erro", "Saldo insuficiente.")
    except ValueError:
        messagebox.showerror("Erro", "Valor inválido.")


def comprar_btc():
    global saldo, cripto_btc
    custo = 100.00
    if saldo >= custo:
        saldo -= custo
        qtd = custo / 300000.0
        cripto_btc += qtd
        historico.append(
            f"Compra Cripto: R$ 100.00 em BTC ({qtd:.6f} BTC)"
        )
        atualizar_tudo()
    else:
        messagebox.showwarning(
            "Erro", "Saldo insuficiente para comprar R$ 100,00 em BTC."
        )


janela = tk.Tk()
janela.title("Simulador Financeiro - Padrão B3")
janela.geometry("600x480")
janela.configure(bg=COLOR_AZUL_ESC)

style = ttk.Style()
style.theme_use("default")
style.configure("TNotebook", background=COLOR_AZUL_ESC)
style.configure(
    "TNotebook.Tab",
    background=COLOR_AZUL_MED,
    foreground="white",
    padding=[12, 6],
    font=("Arial", 10, "bold"),
)
style.map(
    "TNotebook.Tab",
    background=[("selected", COLOR_AMARELO)],
    foreground=[("selected", COLOR_ACO)],
)

header = tk.Frame(janela, bg=COLOR_AZUL_ESC, height=50)
header.pack(fill="x")
lbl_titulo = tk.Label(
    header,
    text="B3 - SIMULADOR EDUCACIONAL",
    font=("Arial", 14, "bold"),
    fg="white",
    bg=COLOR_AZUL_ESC,
)
lbl_titulo.pack(pady=10)

notebook = ttk.Notebook(janela)
notebook.pack(fill="both", expand=True, padx=10, pady=10)

aba_conta = tk.Frame(notebook, bg="white")
aba_cripto = tk.Frame(notebook, bg="white")
aba_extrato = tk.Frame(notebook, bg="white")

notebook.add(aba_conta, text="Conta Corrente")
notebook.add(aba_cripto, text="Criptoativos")
notebook.add(aba_extrato, text="Extrato")

lbl_saldo = tk.Label(
    aba_conta,
    text=f"Saldo Disponível: R$ {saldo:.2f}",
    font=("Arial", 13, "bold"),
    fg=COLOR_AZUL_ESC,
    bg="white",
)
lbl_saldo.pack(pady=20)

lbl_instrucao = tk.Label(
    aba_conta,
    text="Valor da Operação (R$):",
    font=("Arial", 10),
    fg=COLOR_ACO,
    bg="white",
)
lbl_instrucao.pack()

ent_valor_conta = tk.Entry(
    aba_conta,
    font=("Arial", 11),
    relief="solid",
    bd=1,
    highlightbackground=COLOR_AZUL_MED,
)
ent_valor_conta.pack(pady=5)

btn_frame = tk.Frame(aba_conta, bg="white")
btn_frame.pack(pady=15)

btn_entrada = tk.Button(
    btn_frame,
    text="Entrada (+)",
    bg=COLOR_VERDE,
    fg="white",
    font=("Arial", 10, "bold"),
    width=12,
    relief="flat",
    command=creditar,
)
btn_entrada.grid(row=0, column=0, padx=8)

btn_saida = tk.Button(
    btn_frame,
    text="Saída (-)",
    bg=COLOR_ROSA,
    fg="white",
    font=("Arial", 10, "bold"),
    width=12,
    relief="flat",
    command=debitar,
)
btn_saida.grid(row=0, column=1, padx=8)

lbl_cripto_titulo = tk.Label(
    aba_cripto,
    text="Mercado Digital - Bitcoin (Simulado)",
    font=("Arial", 12, "bold"),
    fg=COLOR_AZUL_ESC,
    bg="white",
)
lbl_cripto_titulo.pack(pady=15)

lbl_cotacao = tk.Label(
    aba_cripto,
    text="Cotação Fixa: 1 BTC = R$ 300.000,00",
    font=("Arial", 9, "italic"),
    fg="gray",
    bg="white",
)
lbl_cotacao.pack()

lbl_btc = tk.Label(
    aba_cripto,
    text=f"Seu Saldo BTC: {cripto_btc:.6f}",
    font=("Arial", 11, "bold"),
    fg=COLOR_AZUL_MED,
    bg="white",
)
lbl_btc.pack(pady=15)

btn_comprar_btc = tk.Button(
    aba_cripto,
    text="Comprar R$ 100,00 em BTC",
    bg=COLOR_AMARELO,
    fg=COLOR_ACO,
    font=("Arial", 10, "bold"),
    relief="flat",
    padx=10,
    pady=5,
    command=comprar_btc,
)
btn_comprar_btc.pack(pady=10)

lst_extrato = tk.Listbox(
    aba_extrato,
    font=("Consolas", 10),
    fg=COLOR_ACO,
    bg="#F9F9F9",
    selectbackground=COLOR_AZUL_CLA,
    relief="solid",
    bd=1,
)
lst_extrato.pack(padx=15, pady=15, fill="both", expand=True)

atualizar_extrato()

janela.mainloop()