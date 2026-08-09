class PaymentProcessor:
    def __init__(self, strategy):
        self.strategy = strategy

    def pay(self, amount):
        self.strategy.pay(amount)

processor = PaymentProcessor(CreditCard())
processor.pay(50)
processor = PaymentProcessor(PayPal())
processor.pay(50)
