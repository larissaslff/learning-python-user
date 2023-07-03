class User:
    def __init__(self, first_name, last_name, nickname, login_attempts=0):
        self.first_name = first_name
        self.last_name = last_name
        self.nickname = nickname
        self.login_attempts = login_attempts
    
    
    def describe_user(self):
        print(f'{self.nickname}: {self.first_name} {self.last_name}')
        print(f'Tentativas de login: {self.login_attempts}')
    
    
    def increment_login_attempts(self):
        self.login_attempts += 1
        
    
    def reset_login_attempts(self):
        self.login_attempts = 0
    
    
    def greet_user(self):
        print(f'Olá, {self.nickname}!')


user01 = User('Ana', 'Morais', 'anamorais')
user02 = User('Beatriz', 'Sousa', 'biasousa')
user01.describe_user()
user02.greet_user()
user01.increment_login_attempts()
user01.increment_login_attempts()
user01.describe_user()
user01.reset_login_attempts()
user01.describe_user()