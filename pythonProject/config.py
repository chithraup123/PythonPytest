class Config:
    def __init__(self, env):
        self.baseUrl = {
            'dev': 'https://www.google.com',
            'qa': 'https://www.saucedemo.com/'
        }[env]

        self.app_port = {
            'dev': 8080,
            'qa': 8088
        }[env]
