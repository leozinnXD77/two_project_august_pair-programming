import io
import tkinter as tk
from tkinter import menssagebox
import requests
from PIL import Image, ImageTk

COLOR_VERM_ESC  = "#5d0202"
COLOR_CINZA     = "#4B4B4B"
COLOR_BRANCO    = "#fffafa"
COLOR_VERM_MED  = "#ff0000"
COLOR_VERM_CLA  = "#E86666"
COLOR_CINZA_ESC = "#1e1e1e"
COLOR_CINZA_MED = "#1e1e1e"


def mostrar_fato(detalhe):
    menssagebox.showinfo("Curiosidade Eufrasia", detalhe)

janela = tk.Tk()
janela.title("História Financeira: Eufrásia Teixeira Leite")
janela.geometry("500x580")
janela.configure(bg=COLOR_CINZA_ESC)

lbl_titulo = tk.Label(
    janela,
    text="Eufrásia Teixeira Leite",
    font=('Helvetica', 12, "bold"),
    bg=COLOR_CINZA_ESC,
    fg=COLOR_BRANCO",
)
lbl_titulo.pack(pady=7)
lbl_subtitulo = tk.Label(
    janela,
    text="A primeira mulher investidora global do Brasil"
    font=('Helvetica', -14, 'bold italic'),
    bg=COLOR_CINZA_MED,
    fg=COLOR_BRANCO
)
lbl_subtitulo.pack(pady=2)