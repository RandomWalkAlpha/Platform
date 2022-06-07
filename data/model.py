class DataModel:
    """
    This class is used to save the data status and corresponding information during computing.
    """
    def __init__(self, signal: str, expression: str):
        self.signal = signal
        self.expression = expression
        self.status_list = ['pending', 'queuing', 'executing', 'failed', 'finished']
        self.status = 'pending'
        self.info = {}

    def update(self, new_status: str):
        assert new_status in self.status_list, "Illegal status assignment."
        self.status = new_status

    def set_info(self, key: str, info: str):
        self.info[key] = info

    def disabled(self):
        self.status = 'failed'

    def get_status(self):
        return self.status
