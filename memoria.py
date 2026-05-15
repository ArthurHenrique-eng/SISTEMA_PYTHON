from usuario import User
 
 
class UserRepository:
    """
    Repositório in-memory de usuários.
    Em produção, substitua _db por uma conexão real com banco de dados.
    """
 
    def __init__(self):
        self._db: dict[str, User] = {
            "arthur": User(username="arthur", password="senha123"),
            "admin":  User(username="admin",  password="admin@2024"),
            "user":   User(username="user",   password="1234"),
        }
 
    def buscar_por_username(self, username: str) -> User | None:
        return self._db.get(username)
 
    def listar_usernames(self) -> list[str]:
        return list(self._db.keys())
