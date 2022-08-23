class Account:
    def __init__(self, a_id, balance, customer_id, type):
        self.id = a_id,
        self.balance = balance,
        self.customer_id = customer_id,
        self.type = type;

    def to_dict(self):
        return {
            "a_id": self.id,
            "balance": self.balance,
            "customer_id": self.customer_id,
            "type": self.type
        }