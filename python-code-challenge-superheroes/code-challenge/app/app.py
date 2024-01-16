#!/usr/bin/env python3

from flask import Flask, make_response
from flask_migrate import Migrate

from models import db, Hero
import os

abs_path = os.getcwd()

db_path = f"{abs_path}/db/heroes.db"
app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = f"sqlite:///{db_path}"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

migrate = Migrate(app, db)

db.init_app(app)


@app.route("/")
def home():
    return ""


@app.route("/add-hero")
def add_hero():
    hero = Hero(name="Clark Kent", super_name="Superman")
    db.session.add(hero)
    db.session.commit()
    return "Hero added!"


if __name__ == "__main__":
    app.run(port=5555, debug=True)
