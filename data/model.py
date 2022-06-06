class DataModel:
    """
    This class is used to save the data status and corresponding information during computing.
    """
    def __init__(self, name: str, expression: str):
        self.name = name
        self.expression = expression
        self.status = 'init'

    def update(self, new_status: str):
        self.status = new_status
