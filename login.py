import tkinter as tk
from typing import Callable
from config import CORES, JANELA_LARGURA, JANELA_ALTURA, APP_NAME, APP_VERSION
 
 
class LoginWindow:
    """
    Janela de login pura — só apresentação.
 
    Parâmetros
    ----------
    on_submit : Callable[[str, str], None]
        Função chamada quando o usuário clica em "Entrar".
        Recebe (username, senha) e não retorna nada.
        Quem trata o resultado é o App controller (ui/app.py).
    """
 
    def __init__(self, on_submit: Callable[[str, str], None]):
        self._on_submit = on_submit
 
        self.root = tk.Tk()
        self.root.title(APP_NAME)
        self.root.geometry(f"{JANELA_LARGURA}x{JANELA_ALTURA}")
        self.root.resizable(False, False)
        self.root.configure(bg=CORES["fundo"])
        self.root.eval("tk::PlaceWindow . center")
 
        self._construir_interface()
  
    def _construir_interface(self):
        canvas = tk.Canvas(
            self.root, width=344, height=414,
            bg=CORES["fundo"], highlightthickness=0
        )
        canvas.place(relx=0.5, rely=0.5, anchor="center")
        canvas.create_rectangle(0, 0, 344, 414, outline=CORES["borda"], width=1)

        frame = tk.Frame(self.root, bg=CORES["painel"])
        frame.place(relx=0.5, rely=0.5, anchor="center", width=340, height=410)
 
        tk.Label(
            frame, text="⬡", font=("Courier", 38),
            bg=CORES["painel"], fg=CORES["destaque"]
        ).pack(pady=(36, 4))
 
        tk.Label(
            frame, text="ACESSO AO SISTEMA", font=("Courier", 11, "bold"),
            bg=CORES["painel"], fg=CORES["texto"]
        ).pack()
 
        tk.Label(
            frame, text="Insira suas credenciais", font=("Courier", 9),
            bg=CORES["painel"], fg=CORES["texto_muted"]
        ).pack(pady=(2, 24))
 
        self._criar_label(frame, "USUÁRIO")
        self.campo_usuario = self._criar_entry(frame)
        self.campo_usuario.pack(fill="x", padx=30, ipady=8, pady=(4, 16))
        self.root.after(10, self.campo_usuario.focus_set)
 
        self._criar_label(frame, "SENHA")
        self.campo_senha = self._criar_entry(frame, show="•")
        self.campo_senha.pack(fill="x", padx=30, ipady=8, pady=(4, 20))
        self.campo_senha.bind("<Return>", lambda _: self._disparar_submit())
 
        self.label_status = tk.Label(
            frame, text="", font=("Courier", 8),
            bg=CORES["painel"], fg=CORES["erro"]
        )
        self.label_status.pack(pady=(0, 8))
 
        tk.Button(
            frame, text="ENTRAR", font=("Courier", 11, "bold"),
            bg=CORES["destaque"], fg=CORES["fundo"],
            activebackground=CORES["botao_hover"],
            activeforeground=CORES["fundo"],
            relief="flat", cursor="hand2",
            command=self._disparar_submit,
        ).pack(fill="x", padx=30, ipady=10)
 
        tk.Label(
            self.root,
            text=f"Usuários: arthur / admin / user  •  v{APP_VERSION}",
            font=("Courier", 7), bg=CORES["fundo"], fg="#333333"
        ).place(relx=0.5, rely=0.97, anchor="s")
 
    def _criar_label(self, parent, texto: str):
        tk.Label(
            parent, text=texto, font=("Courier", 8, "bold"),
            bg=CORES["painel"], fg=CORES["destaque"], anchor="w"
        ).pack(fill="x", padx=30)
 
    def _criar_entry(self, parent, show: str = "") -> tk.Entry:
        return tk.Entry(
            parent, font=("Courier", 12),
            bg=CORES["fundo"], fg=CORES["texto"],
            insertbackground=CORES["destaque"],
            relief="flat", show=show,
            highlightthickness=1,
            highlightbackground=CORES["borda"],
            highlightcolor=CORES["destaque"],
        )
  
    def exibir_erro(self, mensagem: str):
        self.label_status.config(text=f"✗  {mensagem}", fg=CORES["erro"])
        self.limpar_senha()
 
    def exibir_sucesso(self, mensagem: str):
        self.label_status.config(text=f"✓  {mensagem}", fg="#00ff88")
 
    def limpar_senha(self):
        self.campo_senha.delete(0, tk.END)
 
    def fechar(self):
        self.root.destroy()
 
    def ocultar(self):
        self.root.withdraw()
 
    def iniciar(self):
        self.root.mainloop()
  
    def _disparar_submit(self):
        username = self.campo_usuario.get()
        senha    = self.campo_senha.get()
        self._on_submit(username, senha)
