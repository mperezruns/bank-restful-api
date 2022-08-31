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
                    customer_phone = customer[4],
                    customer_city = customer[5],
                    username = customer[6],
                    active = customer[7]

                    my_customer_obj = Customer(c_id, customername, first_name, last_name, customer_phone, customer_city, username, active)
                    my_list_of_customer_objs.append(my_customer_obj)

                return my_list_of_customer_objs

    def get_customer_by_id(self, customer_id):
        with psycopg.connect(host="127.0.0.1", port="5432", dbname="prj_api", user="postgres",
                             password="@zul@6") as conn:
            # Automatically close the cursor
            with conn.cursor() as cur:
                cur.execute("SELECT * FROM customers WHERE id = %s", (customer_id,))

                customer_row = cur.fetchone()
                if not customer_row:
                    return None

                c_id = customer_row[0]
                customername = customer_row[1],
                first_name = customer_row[2],
                last_name = customer_row[3],
                customer_phone = customer_row[4],
                customer_city = customer_row[5],
                username = customer_row[6],
                active = customer_row[7]

                return Customer(c_id, customername, first_name, last_name, customer_phone, customer_city, username, active)

# customer_row = CustomerDao()
# print(customer_row.get_customer_by_id)

    def add_customer(self, customer_object):
        cn_to_add = customer_object.customername    #1
        fn_to_add = customer_object.first_name  #2
        ln_to_add = customer_object.last_name   #3
        phone_to_add = customer_object.customer_phone   #4
        city_to_add = customer_object.customer_city     #5
        username_to_add = customer_object.username  #6

        with psycopg.connect(host="127.0.0.1", port="5432", dbname="prj_api", user="postgres",
                             password="@zul@6") as conn:
            # Automatically close the cursor
            with conn.cursor() as cur:
                cur.execute("INSERT INTO customers (customername, first_name, last_name, customer_phone, customer_city, username) VALUES (%s, %s, %s, %s, %s, %s) RETURNING *", (cn_to_add, fn_to_add,
                                                                                                                                                                                 ln_to_add, phone_to_add,
                                                                                                                                                                                 city_to_add, username_to_add))

                cr_that_was_just_inserted = cur.fetchone()

                conn.commit()

                return Customer(cr_that_was_just_inserted[0], cr_that_was_just_inserted[1],
                                cr_that_was_just_inserted[2], cr_that_was_just_inserted[3],
                                cr_that_was_just_inserted[4], cr_that_was_just_inserted[5],
                                cr_that_was_just_inserted[6], cr_that_was_just_inserted[7])
