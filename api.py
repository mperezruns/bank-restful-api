from flask import Flask
from controller.customer_controller import cc
from controller.account_controller import ac

if __name__ == '__main__':
    api = Flask(__name__)   # Instanciating an api object

    api.register_blueprint(cc)
    api.register_blueprint(ac)

    api.run(port=8080, debug=True)
