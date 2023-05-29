class Login:
    def __init__(self, page):
        self.username = page.get_by_placeholder("Your username")
        self.password = page.get_by_placeholder("Your password")
