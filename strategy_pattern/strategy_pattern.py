from PaymentInterface import PaymentInterface

class PaymentContext:

    def __init__(self, strategy: PaymentInterface):
        self.strategy = strategy

    @property
    def strategy(self):
        return self.__strategy

    @strategy.setter
    def strategy(self, new_strategy: PaymentInterface):
        self.__strategy = new_strategy

    def execute_payment(self, amount):
        self.strategy.pay(amount)


