import tkinter as tk
import customtkinter
from PIL import Image, ImageTk


class TimerApp:
    def __init__(self, root, tempo_para_fechar):
        self.root = root
        self.tempo_para_fechar = tempo_para_fechar
        self.progresso = 0 

        self.image = Image.open(r"logo_ufg.png")

        self.image2 = Image.open(r"iris_carregamento.png")

        height = 500
        width = 500
        x = (self.root.winfo_screenwidth() // 2) - (width // 2)
        y = (self.root.winfo_screenheight() // 2) - (height // 2)
        self.root.geometry('{}x{}+{}+{}'.format(width, height, x, y))

        self.root.config(background="#000000")

        icone_path = r"cyclone_1f300.ico"
        self.root.iconbitmap(icone_path)

        customtkinter.set_appearance_mode("light")
        customtkinter.set_default_color_theme("blue")

        root.title("Íris - Assistente Virtual")


        texto = customtkinter.CTkLabel(root, text="Carregando...")
        texto.place(x=180, y=390)
        texto.configure(font=("Calibri",25))

        texto2 = customtkinter.CTkLabel(root, text="2023")
        texto2.place(x=230, y=470)
        texto2.configure(font=("Arial",15))

        imagem_redimensionada = self.image.resize((450, 150), Image.LANCZOS) #Por favor use caso de erro: Image.ANTIALIAS
        self.imagem_tk = ImageTk.PhotoImage(imagem_redimensionada)
        self.widget_imagem = tk.Label(root, image=self.imagem_tk, borderwidth=0)
        self.widget_imagem.pack_forget()
        self.widget_imagem.pack()
        self.widget_imagem.place(x=80, y=230)

        imagem_redimensionada2 = self.image2.resize((250, 145), Image.LANCZOS)
        self.imagem2_tk = ImageTk.PhotoImage(imagem_redimensionada2)
        self.widget_imagem2 = tk.Label(root, image=self.imagem2_tk, borderwidth=0)
        self.widget_imagem2.pack_forget()
        self.widget_imagem2.pack()
        self.widget_imagem2.place(x=180, y=30)

        self.progressbar = tk.Canvas(root, width=400, height=20, bg='black')
        self.progressbar.place(x=100, y=440)
        self.simular_progresso()

        # Função que fecha a janela após o tempo determinado
        #self.root.after(self.tempo_para_fechar, self.fechar_janela)

        self.root.resizable(False, False)
        self.root.mainloop()

    
    def simular_progresso(self):
        if self.progresso < 100:
            self.progresso += 1
            self.atualizar_progresso()
            self.root.after(50, self.simular_progresso)

    def atualizar_progresso(self):
        self.progressbar.delete("progress")
        x1, y1, x2, y2 = 0, 0, (self.progresso * 4), 20  # Aumenta o retângulo em 4 pixels a cada progresso
        self.progressbar.create_rectangle(x1, y1, x2, y2, fill='#015682', tags="progress")

    def fechar_janela(self):
        self.root.destroy()

# Tempo em milissegundos (exemplo: 5000 ms = 5 segundos)
tempo_para_fechar = 1000

root = customtkinter.CTk()

app = TimerApp(root, tempo_para_fechar)
