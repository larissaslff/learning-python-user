class User:
    def __init__(self, first_name, last_name, nickname):
        self.first_name = first_name
        self.last_name = last_name
        self.nickname = nickname
    
    
    def describe_user(self):
        print(f'{self.nickname}: {self.first_name} {self.last_name}')
        
    
    def greet_user(self):
        print(f'Olá, {self.nickname}!')


user01 = User('Ana', 'Morais', 'anamorais')
user02 = User('Beatriz', 'Sousa', 'biasousa')
user01.describe_user()
user02.greet_user()