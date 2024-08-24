# method vs @classmethod vs @staticmethod
# method - self, método de instância
# @classmethod - cls, método de classe
# @staticmethod - método estático (❌self, ❌cls)
class Conection:
    def __init__(self, host='localhost'):
        self.host = host
        self.user = None
        self.password = None
    
    def set_user(self, user):
        # setter
        self.user = user

    def set_password(self, password):
        self.password = password

    @classmethod
    def create_with_auth(cls, user, password):
        connection = cls()
        connection.user = user
        connection.password = password
        return connection
    
    @staticmethod
    def log(msg): # poderia fazer uma funcao connection _log de forma norma, funcionaria igual
        print('LOG:', msg)



# c1 = Conection()
c1 = Conection.create_with_auth('luiz', '1234')
# c1.set_user('luiz')
print(c1.user)
# c1.set_password('1a2b')
print(c1.password)
Conection.log('Essa é a mensagem de LOG')