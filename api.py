from flask import Flask
from controller.customer_controller import cc

if __name__ == '__main__':
    api = Flask(__name__)   # Instanciating an api object

    api.register_blueprint(cc)

    api.run(port=8080, debug=True)
