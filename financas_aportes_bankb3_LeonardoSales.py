import tkinter as tk
from tkinter import messagebox

COLOR_AZUL_ESC = "#004d6e"  
COLOR_AZUL_MED = "#0081ab"  
COLOR_AZUL_CLA = "#00b1cd"  
COLOR_VERDE    = "#a6c844"  
COLOR_ROSA     = "#b83764"  
COLOR_AMARELO  = "#edce01"  
COLOR_ACO      = "#4a3336"  

saldo = 0.0


def depositar():
    global saldo
    try:
        val = float(ent_valor.get())
        if val <= 0:
            messagebox.showwarning("Aviso", "Digite um valor maior que zero.")
            return

        saldo += val
        atualizar_saldo()
    except ValueError:
        messagebox.showerror("Erro", "Digite um valor numérico válido.")


def sacar():
    global saldo
    try:
        val = float(ent_valor.get())
        if val <= 0:
            messagebox.showwarning("Aviso", "Digite um valor maior que zero.")
            return

        if val > saldo:
            messagebox.showwarning("Aviso", "Saldo insuficiente!")
        else:
            saldo -= val
            atualizar_saldo()
    except ValueError:
        messagebox.showerror("Erro", "Digite um valor numérico válido.")


def atualizar_saldo():
    lbl_saldo.config(text=f"Saldo Atual: R$ {saldo:.2f}")
    ent_valor.delete(0, tk.END)


janela = tk.Tk()
janela.title("Simulador de Rendas")
janela.geometry("380x300")

lbl_saldo = tk.Label(
    janela, text="Saldo Atual: R$ 0.00", font=("Cooper black", 16, "bold"), fg=COLOR_ACO
)
lbl_saldo.pack(pady=20)

lbl_instrucao = tk.Label(janela, text="Valor da Operação (R$):")
lbl_instrucao.pack()

ent_valor = tk.Entry(janela, font=("Arial", 12))
ent_valor.pack(pady=5)

btn_frame = tk.Frame(janela)
btn_frame.pack(pady=15)

btn_depositar = tk.Button(
    btn_frame,
    text="Depositar (+)",
    bg=COLOR_AZUL_CLA,
    fg="white",
    width=12,
    command=depositar,
)
btn_depositar.grid(row=0, column=0, padx=5)

btn_sacar = tk.Button(
    btn_frame, text="Sacar (-)", bg=COLOR_ROSA, fg="white", width=12, command=sacar
)
btn_sacar.grid(row=0, column=1, padx=5)

janela.mainloop()