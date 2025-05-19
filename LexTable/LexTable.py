class LexTable:
    def __init__(self):
        self.complete = []
        self.accept = ''
        self.productions = {}
        self.closure = {}
        self.transactions = {}
