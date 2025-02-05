from typing import override
from PaymentInterface import PaymentInterface

class BitPayment(PaymentInterface):

    def __init__(self, account: str):
        self.account = account

    @override
    def pay(self, amount: float):
        print(f"Paid {amount: .2f} using Bit account {self.account}")