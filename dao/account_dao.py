import psycopg
from model.account import Account

class AccountDao:

    def get_accounts(self):
        with psycopg.connect(host="127.0.0.1", port="5432", dbname="prj_api", user="postgres",
                             password="@zul@6") as conn:
            # Automatically close the cursor
            with conn.cursor() as cur:
                cur.execute("SELECT * FROM accounts")

                account_list = []

                for row in cur:
                    account_list.append(Account(row[0], row[1], row[2], row[3]))

                return account_list