from model.customer import Customer
import psycopg

class CustomerDao:
    # CRUD Operations
    # Create -- insert a new user into my "database"
    # Read -- Retrieve a user or users into my "database"
    # Update -- Update a user in my "database"
    # Delete -- Delete a user in my "database"

    def get_all_customers(self):
        with psycopg.connect(host="127.0.0.1", port="5432", dbname="prj_api", user="postgres",
                             password="@zul@6") as conn:
            # Automatically close the cursor
            with conn.cursor() as cur:
                cur.execute("SELECT * FROM customers")

                my_list_of_customer_objs = []

                for customer in cur:
                    c_id = customer[0]
                    customername = customer[1],
                    first_name = customer[2],
                    last_name = customer[3],
                    birthday = customer[4],
                    customer_phone = customer[5],
                    customer_city = customer[6],
                    username = customer[7],
                    active = customer[8]

                    my_customer_obj = Customer(c_id,customername,first_name,last_name,birthday,customer_phone,customer_city,username,active)
                    my_list_of_customer_objs.append(my_customer_obj)

                return my_list_of_customer_objs

# customer_dao = CustomerDao()
# print(customer_dao.get_all_customers)

    def get_customer_by_id(self, customer_id):
        with psycopg.connect(host="127.0.0.1", port="5432", dbname="prj_api", user="postgres",
                             password="@zul@6") as conn:
            # Automatically close the cursor
            with conn.cursor() as cur:
                cur.execute("SELECT * FROM customers WHERE id=%s", (customer_id,))

                customer_row = cur.fetchone()
                if not customer_row:
                    return None

            c_id = customer_row[0]
            customername = customer_row[1],
            first_name = customer_row[2],
            last_name = customer_row[3],
            birthday = customer_row[4],
            customer_phone = customer_row[5],
            customer_city = customer_row[6],
            username = customer_row[7],
            active = customer_row[8]

            return Customer(c_id, customername, first_name, last_name, birthday, customer_phone, customer_city, username, active)

# customer_row = CustomerDao()
# print(customer_row.get_all_customers_id)

