from dataclasses import dataclass
from memoria import UserRepository
 
 
@dataclass
class ResultadoLogin:
    sucesso:   bool
    mensagem:  str
    username:  str = ""
 
 
class AuthService:

 
    def __init__(self, repositorio: UserRepository):
        self._repo = repositorio
 
    def autenticar(self, username: str, senha: str) -> ResultadoLogin:
        username = username.strip().lower()
 
        if not username or not senha:
            return ResultadoLogin(sucesso=False, mensagem="Preencha todos os campos.")
 
        usuario = self._repo.buscar_por_username(username)
 
        if usuario is None:
            return ResultadoLogin(sucesso=False, mensagem="Usuário não encontrado.")
 
        if not usuario.verificar_senha(senha):
            return ResultadoLogin(sucesso=False, mensagem="Senha incorreta.")
 
        return ResultadoLogin(
            sucesso=True,
            mensagem=f"Bem-vindo, {username}!",
            username=username,
        )
