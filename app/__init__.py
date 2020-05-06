#import bibliotek
from flask import Flask
from flask_wtf.csrf import CSRFProtect

#utworzenie instancji(obiektu) klasy Flask reprezentującego aplikacje
app = Flask(__name__)
csrf = CSRFProtect(app)
app.config['SECRET_KEY'] = "secretkey"
app.config['WTF_CSRF_SECRET_KEY'] = "secretkey"
csrf.init_app(app)

from app import routes

if __name__ == "__main__":
    app.run(debug=True)