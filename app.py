from tkinter import messagebox

from memoria import UserRepository
from validacao import AuthService
from login import LoginWindow
from navegador import abrir_url
from config import URL_DESTINO, MAX_TENTATIVAS


class App:
    """
    Controlador principal.

    Responsabilidades:
      - Instanciar e conectar todas as dependências.
      - Reagir ao evento de login (sucesso / falha / bloqueio).
      - Nunca conter regras de negócio nem código de UI diretamente.
    """

    def __init__(self):
        repositorio  = UserRepository()
        self._auth   = AuthService(repositorio)
        self._janela = LoginWindow(on_submit=self._handle_login)

        self._tentativas = 0

    def iniciar(self):
        self._janela.iniciar()

    def _handle_login(self, username: str, senha: str):
        resultado = self._auth.autenticar(username, senha)

        if resultado.sucesso:
            self._ao_autenticar(resultado.mensagem)
        else:
            self._ao_falhar(resultado.mensagem)

    def _ao_autenticar(self, mensagem: str):
        self._janela.ocultar()
        messagebox.showinfo("Acesso liberado", mensagem)
        abrir_url(URL_DESTINO)
        self._janela.fechar()

    def _ao_falhar(self, mensagem: str):
        self._tentativas += 1
        restantes = MAX_TENTATIVAS - self._tentativas

        if self._tentativas >= MAX_TENTATIVAS:
            messagebox.showerror(
                "Acesso bloqueado",
                "Número máximo de tentativas atingido.\nO sistema será encerrado."
            )
            self._janela.fechar()
            return

        self._janela.exibir_erro(f"{mensagem} ({restantes} tentativa(s) restante(s))")
