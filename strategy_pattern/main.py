from BitcoinPayment import BitcoinPayment
from PayPalPayment import PayPalPayment
from CreditCardPayment import CreditCardPayment
from BitPayment import BitPayment
from strategy_pattern import PaymentContext

def main():
    credit_card = CreditCardPayment("1234-5678-9876-5432", "123")
    paypal = PayPalPayment("user@example.com")
    bitcoin = BitcoinPayment("3J98t1WpEZ73CNmQviecrnyiWrnqRhWNLy")
    bit = BitPayment("123456")

    mobile_app = PaymentContext(credit_card)
    mobile_app.execute_payment(180.5)
    mobile_app.strategy = paypal
    mobile_app.execute_payment(220)
    mobile_app.strategy = bitcoin
    mobile_app.execute_payment(1050)
    mobile_app.strategy = bit
    mobile_app.execute_payment(500)

if __name__ == "__main__":
     main()