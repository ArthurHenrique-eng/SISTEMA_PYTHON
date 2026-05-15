from dataclasses import dataclass
 
 
@dataclass
class User:
    username: str
    password: str
 
    def verificar_senha(self, senha_informada: str) -> bool:
        return self.password == senha_informada
 
    def __repr__(self) -> str:
        return f"User(username='{self.username}')"