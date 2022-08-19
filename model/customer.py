class Customer:
    def __init__(self, c_id, customername, first_name, last_name, birthday, customer_phone, customer_city, username, active):
        self.id = c_id,
        self.customername = customername,
        self.first_name = first_name,
        self.last_name = last_name,
        self.birthday = birthday,
        self.customer_phone = customer_phone,
        self.customer_city = customer_city
        self.username = username
        self.active = active

    def to_dict(self):
        return {
        "id": self.id,
        "customername": self.customername,
        "first_name": self.first_name,
        "last_name": self.last_name,
        "birth_date": self.birthday,
        "customer_phone": self.customer_phone,
        "customer_city": self.customer_city,
        "username": self.username,
        "active": self.active
        }