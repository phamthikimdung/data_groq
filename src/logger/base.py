class BaseLogger:
    def __init__(self) -> None:
        self.info = print
        self.error = print  # Thêm phương thức error
        self.warning = print  # Thêm phương thức warning nếu cần
        self.debug = print  # Thêm phương thức debug nếu cần
