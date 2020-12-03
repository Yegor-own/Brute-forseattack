class BaseStrategy:
    def generate(self):
        raise NotImplementedError


class DumbStrategy(BaseStrategy):
    def __init__(self, login_generator, password_generator, query):
        self.login_generator = login_generator
        self.password_generator = password_generator
        self.query = query

    def run(self):
        login = self.login_generator.generate()

        while True:
            password = self.password_generator.generate()
            if self.query*(login, password):
                print("success", login, password)
                break