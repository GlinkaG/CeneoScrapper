#import bibliotek
from flask import Flask

#utworzenie instancji(obiektu) klasy Flask reprezentującego aplikacje
app = Flask(__name__)

from app import routes

if __name__ == "__main__":
    app.run(debug=True)