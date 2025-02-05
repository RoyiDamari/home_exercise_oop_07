from typing import override
from PaymentInterface import PaymentInterface

class BitcoinPayment(PaymentInterface):

    def __init__(self, wallet_address: str):
        self.wallet_address = wallet_address

    @override
    def pay(self, amount: float):
        print(f"Paid {amount: .2f} using Bitcoin wallet {self.wallet_address[-6:]}")