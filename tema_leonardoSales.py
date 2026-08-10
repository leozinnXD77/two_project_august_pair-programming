import io
import tkinter as tk
from tkinter import messagebox, simpledialog
from PIL import Image, ImageTk
from faker import Faker

data_faker = Faker('pt_BR')

class TelaAutenticacao:
    def __init__(self, root):
        self.root = root
        self.root.title("Banco Python - Acesso")
        self.root.geometry("400x500")
        self.root.config(bg="#0F172A")
        self.root.resizable(False, False)

        # Banco de dados em memória para as contas
        self.contas_cadastradas = []
        
        # Criar uma conta padrão para testes rápidos
        self.contas_cadastradas.append({
            'nome': 'João Silva',
            'conta': '12345',
            'senha': '123',
            'saldo': 1500.00,
            'email': 'joao@email.com',
            'tel': '(11) 98888-7777',
            'end': 'Rua Exemplo, 100 - São Paulo/SP'
        })

        self.criar_tela_login()

    def limpar_tela(self):
        for widget in self.root.winfo_children():
            widget.destroy()

    def criar_tela_login(self):
        self.limpar_tela()

        lbl_titulo = tk.Label(self.root, text="Banco Digital", fg="#10B981", bg="#0F172A", font=("Arial", 22, "bold"))
        lbl_titulo.pack(pady=(50, 30))

        frame = tk.Frame(self.root, bg="#1E293B", padx=20, pady=20)
        frame.pack(padx=30, fill="x")

        # Dica rápida na tela para teste
        lbl_dica = tk.Label(frame, text="Dica teste: Conta '12345' | Senha '123'", fg="#64748B", bg="#1E293B", font=("Arial", 8))
        lbl_dica.pack(anchor="w", pady=(0, 10))

        tk.Label(frame, text="Número da Conta:", fg="#94A3B8", bg="#1E293B", font=("Arial", 10)).pack(anchor="w")
        self.entry_conta = tk.Entry(frame, font=("Arial", 12), bg="#334155", fg="#FFFFFF", bd=0, insertbackground="white")
        self.entry_conta.pack(fill="x", pady=(5, 15), ipady=5)

        tk.Label(frame, text="Senha:", fg="#94A3B8", bg="#1E293B", font=("Arial", 10)).pack(anchor="w")
        self.entry_senha = tk.Entry(frame, show="*", font=("Arial", 12), bg="#334155", fg="#FFFFFF", bd=0, insertbackground="white")
        self.entry_senha.pack(fill="x", pady=(5, 20), ipady=5)

        btn_entrar = tk.Button(frame, text="Entrar na Conta", bg="#10B981", fg="#FFFFFF", font=("Arial", 11, "bold"), bd=0, cursor="hand2", command=self.fazer_login)
        btn_entrar.pack(fill="x", ipady=8)

        btn_criar_tela = tk.Button(self.root, text="Não tem conta? Criar Perfil", bg="#334155", fg="#94A3B8", font=("Arial", 10), bd=0, cursor="hand2", command=self.criar_tela_cadastro)
        btn_criar_tela.pack(pady=20)

    def criar_tela_cadastro(self):
        self.limpar_tela()

        lbl_titulo = tk.Label(self.root, text="Criar Novo Perfil", fg="#10B981", bg="#0F172A", font=("Arial", 18, "bold"))
        lbl_titulo.pack(pady=(30, 20))

        frame = tk.Frame(self.root, bg="#1E293B", padx=20, pady=20)
        frame.pack(padx=30, fill="x")

        tk.Label(frame, text="Nome Completo:", fg="#94A3B8", bg="#1E293B", font=("Arial", 10)).pack(anchor="w")
        self.entry_nome_cad = tk.Entry(frame, font=("Arial", 11), bg="#334155", fg="#FFFFFF", bd=0, insertbackground="white")
        self.entry_nome_cad.pack(fill="x", pady=(3, 10), ipady=4)
        self.entry_nome_cad.insert(0, data_faker.name())

        tk.Label(frame, text="Senha de Acesso (para não esquecer):", fg="#94A3B8", bg="#1E293B", font=("Arial", 10)).pack(anchor="w")
        self.entry_senha_cad = tk.Entry(frame, font=("Arial", 11), bg="#334155", fg="#FFFFFF", bd=0, insertbackground="white")
        self.entry_senha_cad.pack(fill="x", pady=(3, 15), ipady=4)
        self.entry_senha_cad.insert(0, "1234")

        btn_salvar = tk.Button(frame, text="Cadastrar Conta", bg="#10B981", fg="#FFFFFF", font=("Arial", 10, "bold"), bd=0, cursor="hand2", command=self.salvar_novo_perfil)
        btn_salvar.pack(fill="x", ipady=8)

        btn_voltar = tk.Button(self.root, text="Voltar ao Login", bg="#334155", fg="#94A3B8", font=("Arial", 10), bd=0, cursor="hand2", command=self.criar_tela_login)
        btn_voltar.pack(pady=15)

    def salvar_novo_perfil(self):
        nome = self.entry_nome_cad.get()
        senha = self.entry_senha_cad.get()

        if not nome or not senha:
            messagebox.showerror("Erro", "Preencha todos os campos!")
            return

        num_conta_gerado = str(data_faker.random_int(min=10000, max=99999))

        nova_conta = {
            'nome': nome,
            'conta': num_conta_gerado,
            'senha': senha,
            'saldo': 1000.00,
            'email': data_faker.email(),
            'tel': data_faker.phone_number(),
            'end': data_faker.address()
        }

        self.contas_cadastradas.append(nova_conta)
        
        # TELA DE SEGURANÇA: Exibe explicitamente os dados para o usuário não esquecer
        aviso_importante = (
            f"CONTA CRIADA COM SUCESSO!\n\n"
            f"Anote seus dados de acesso:\n"
            f"• Número da Conta: {num_conta_gerado}\n"
            f"• Senha: {senha}\n\n"
            f"Guarde bem esses dados para conseguir entrar depois!"
        )
        messagebox.showwarning("⚠️ IMPORTANTE - Anote seus dados", aviso_importante)
        
        self.criar_tela_login()

    def fazer_login(self):
        num_conta = self.entry_conta.get()
        senha = self.entry_senha.get()

        conta_encontrada = None
        for c in self.contas_cadastradas:
            if c['conta'] == num_conta and c['senha'] == senha:
                conta_encontrada = c
                break

        if conta_encontrada:
            BancoApp(self.root, conta_encontrada, self.criar_tela_login)
        else:
            messagebox.showerror("Erro", "Número de conta ou senha incorretos!")


class BancoApp:
    def __init__(self, root, dados_conta, callback_sair):
        self.root = root
        self.dados_conta = dados_conta
        self.callback_sair = callback_sair

        self.limpar_tela_janela()
        self.root.geometry("450x650")

        self.criar_avatar_imediato()
        self.criar_widgets()

    def limpar_tela_janela(self):
        for widget in self.root.winfo_children():
            widget.destroy()

    def criar_avatar_imediato(self):
        """Gera um avatar instantaneamente via PIL sem delay de requisição web"""
        img = Image.new('RGB', (70, 70), color="#10B981")
        self.avatar_img = ImageTk.PhotoImage(img)

    def criar_widgets(self):
        header_frame = tk.Frame(self.root, bg="#1E293B", height=100)
        header_frame.pack(fill="x", padx=15, pady=15)
        header_frame.pack_propagate(False)

        lbl_avatar = tk.Label(header_frame, image=self.avatar_img, bg="#1E293B")
        lbl_avatar.pack(side="left", padx=15)

        info_frame = tk.Frame(header_frame, bg="#1E293B")
        info_frame.pack(side="left", fill="y", pady=10)

        lbl_bv = tk.Label(info_frame, text="Bem-vindo(a),", fg="#94A3B8", bg="#1E293B", font=("Arial", 10))
        lbl_bv.pack(anchor="w")

        lbl_nome = tk.Label(info_frame, text=self.dados_conta['nome'], fg="#F8FAFC", bg="#1E293B", font=("Arial", 12, "bold"))
        lbl_nome.pack(anchor="w")

        card_frame = tk.Frame(self.root, bg="#10B981", height=140)
        card_frame.pack(fill="x", padx=15, pady=5)
        card_frame.pack_propagate(False)

        lbl_saldo_titulo = tk.Label(card_frame, text="Saldo Disponível", fg="#064E3B", bg="#10B981", font=("Arial", 11, "bold"))
        lbl_saldo_titulo.pack(anchor="w", padx=20, pady=(15, 0))

        self.lbl_saldo_valor = tk.Label(card_frame, text=f"R$ {self.dados_conta['saldo']:,.2f}".replace(",", "X").replace(".", ",").replace("X", "."), fg="#FFFFFF", bg="#10B981", font=("Arial", 22, "bold"))
        self.lbl_saldo_valor.pack(anchor="w", padx=20, pady=5)

        lbl_conta = tk.Label(card_frame, text=f"Conta Nº: {self.dados_conta['conta']}", fg="#D1FAE5", bg="#10B981", font=("Arial", 9))
        lbl_conta.pack(anchor="w", padx=20)

        acoes_frame = tk.Frame(self.root, bg="#0F172A")
        acoes_frame.pack(fill="both", expand=True, padx=15, pady=10)

        lbl_menu = tk.Label(acoes_frame, text="Ações Rápidas", fg="#94A3B8", bg="#0F172A", font=("Arial", 11, "bold"))
        lbl_menu.pack(anchor="w", pady=(0, 10))

        btn_depositar = tk.Button(acoes_frame, text="Depositar", bg="#334155", fg="#FFFFFF", font=("Arial", 10, "bold"), bd=0, cursor="hand2", command=self.depositar)
        btn_depositar.pack(fill="x", pady=5, ipady=8)

        btn_sacar = tk.Button(acoes_frame, text="Sacar", bg="#334155", fg="#FFFFFF", font=("Arial", 10, "bold"), bd=0, cursor="hand2", command=self.sacar)
        btn_sacar.pack(fill="x", pady=5, ipady=8)

        btn_perfil = tk.Button(acoes_frame, text="Dados Cadastrais (Faker)", bg="#334155", fg="#FFFFFF", font=("Arial", 10, "bold"), bd=0, cursor="hand2", command=self.mostrar_dados_faker)
        btn_perfil.pack(fill="x", pady=5, ipady=8)

        btn_sair = tk.Button(acoes_frame, text="Sair / Trocar de Conta", bg="#EF4444", fg="#FFFFFF", font=("Arial", 10, "bold"), bd=0, cursor="hand2", command=self.callback_sair)
        btn_sair.pack(fill="x", pady=(20, 5), ipady=8)

    def atualizar_saldo_tela(self):
        texto_saldo = f"R$ {self.dados_conta['saldo']:,.2f}".replace(",", "X").replace(".", ",").replace("X", ".")
        self.lbl_saldo_valor.config(text=texto_saldo)

    def depositar(self):
        valor_str = simpledialog.askstring("Depósito", "Digite o valor que deseja depositar (R$):", parent=self.root)
        if valor_str:
            try:
                valor = float(valor_str.replace(",", "."))
                if valor > 0:
                    self.dados_conta['saldo'] += valor
                    self.atualizar_saldo_tela()
                    messagebox.showinfo("Sucesso", f"Depósito de R$ {valor:.2f} realizado com sucesso!")
                else:
                    messagebox.showerror("Erro", "O valor deve ser maior que zero.")
            except ValueError:
                messagebox.showerror("Erro", "Valor inválido digitado.")

    def sacar(self):
        valor_str = simpledialog.askstring("Saque", "Digite o valor que deseja sacar (R$):", parent=self.root)
        if valor_str:
            try:
                valor = float(valor_str.replace(",", "."))
                if 0 < valor <= self.dados_conta['saldo']:
                    self.dados_conta['saldo'] -= valor
                    self.atualizar_saldo_tela()
                    messagebox.showinfo("Sucesso", f"Saque de R$ {valor:.2f} realizado com sucesso!")
                elif valor > self.dados_conta['saldo']:
                    messagebox.showwarning("Atenção", "Saldo insuficiente para esta operação.")
                else:
                    messagebox.showerror("Erro", "O valor deve ser maior que zero.")
            except ValueError:
                messagebox.showerror("Erro", "Valor inválido digitado.")

    def mostrar_dados_faker(self):
        info = (
            f"E-mail: {self.dados_conta['email']}\n"
            f"Telefone: {self.dados_conta['tel']}\n"
            f"Endereço: {self.dados_conta['end']}"
        )
        messagebox.showinfo("Dados Cadastrais (Gerados por Faker)", info)

if __name__ == "__main__":
    root = tk.Tk()
    app = TelaAutenticacao(root)
    root.mainloop()