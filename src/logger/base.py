class BaseLogger:
    def __init__(self) -> None:
        self.info = print
        self.error = print
        self.warning = print
        self.debug = print
