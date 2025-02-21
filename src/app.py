from flask import Flask, url_for, flash, render_template
from flask_pymongo import PyMongo
from dotenv import load_dotenv
import os

from routes.auth.auth_bp import auth_bp
from routes.users.users import uses_bp


load_dotenv()


app = Flask(__name__)
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY')
app.config['MONGO_URI'] = os.getenv('MONGO_URI')

mongo = PyMongo(app)

app.register_blueprint( auth_bp(mongo) )
app.register_blueprint( uses_bp(mongo) )





@app.route('/', methods=['GET'])
def root():
    return render_template('index.html'), 200





if __name__ == '__main__':
    app.run(debug=True)